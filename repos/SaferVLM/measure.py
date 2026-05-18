import os, sys
from PIL import Image
import numpy as np
import pandas as pd
import json
import fire
from tqdm import tqdm
from unsafe_datasets import *
from vlms import *

def parse_indices(indices, total):
    if indices is None or indices == "all":
        return list(range(total))
    if isinstance(indices, int):
        return [indices]
    if isinstance(indices, (list, tuple)):
        return [int(idx) for idx in indices]
    return [int(idx.strip()) for idx in str(indices).split(",") if idx.strip()]

def normalize_path(path):
    return path.replace("\\", "/")

def main(model_name: str="llava-v1.5-7b",
         capability: str="alignment",
         response_dir: str="data/VLM_responses",
         prompt_indices: str="all",
         resume: bool=True,
         temperature: float=1.0,
         max_new_tokens: int=512,
         top_p=0.9):
    
    
    gen_kwargs = {
        "temperature": temperature,
        "max_new_tokens": max_new_tokens,
        "top_p": top_p}

    # load model
    model = load_vlm(model_name)
    print(f"Loaded model: {model_name} for capability: {capability} assessment")
    
    # load dataset
    prompt_templates = PROMPTS[capability]
    selected_prompt_indices = parse_indices(prompt_indices, len(prompt_templates))
    
    if capability == "alignment":
        dataset = UnsafeConcepts()
        image_root = dataset.image_root
        
    elif capability == "alignment_text_only":
        dataset = UnsafeConceptBlankImage()
        image_root = dataset.dataset.image_root
        
    elif capability  == "perception":
        dataset = PerceptionDataset()
        image_root = dataset.image_root

    # query model
    for prompt_index in selected_prompt_indices:
        prompt_template = prompt_templates[prompt_index]
        result_dir = os.path.join(response_dir, model_name, capability)
        os.makedirs(result_dir, exist_ok=True)
        result_path = os.path.join(result_dir, f"response_prompt_{prompt_index}.json")
        result = []
        done_keys = set()

        if resume and os.path.exists(result_path):
            with open(result_path, "r") as f:
                result = json.load(f)
            done_keys = {item["image_fname"] for item in result if item.get("output") is not None}
            print(f"Resume enabled: loaded {len(done_keys)} existing responses from {result_path}")

        for item in tqdm(dataset):

            if capability == "perception":
                category, unsafe_concept, image_fname, option_str, correct_option = item
            else:
                category, unsafe_concept, image_fname = item
            
            if "[unsafe concept]" in prompt_template:
                prompt = prompt_template.replace("[unsafe concept]", unsafe_concept)
            elif "[option_str]" in prompt_template:
                prompt = prompt_template.replace("[option_str]", option_str)
            else:
                prompt = prompt_template
            
            relative_image_fname = normalize_path(os.path.relpath(image_fname, image_root))
            if relative_image_fname in done_keys:
                continue

            response = inference(model_name, model, image_fname, prompt, **gen_kwargs)

            result.append({"prompt": prompt,
                           "image_fname": relative_image_fname,
                           "output": response})

            with open(result_path, "w") as f:
                json.dump(result, f, indent=4)
        
        # save result
        with open(result_path, "w") as f:
            json.dump(result, f, indent=4)
            

if __name__ == "__main__":
    fire.Fire(main)
            
                
            
