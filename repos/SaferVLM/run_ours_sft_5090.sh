#!/usr/bin/env bash
set -euo pipefail

cd /root/autodl-tmp/SightGuard/repos/SaferVLM/RLHF

unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY all_proxy ALL_PROXY
unset HF_HUB_OFFLINE
unset TRANSFORMERS_OFFLINE

export HF_ENDPOINT=https://hf-mirror.com
export HF_HOME=/root/autodl-tmp/hf_cache
export TRANSFORMERS_CACHE=/root/autodl-tmp/hf_cache/transformers
export HF_DATASETS_CACHE=/root/autodl-tmp/hf_cache/datasets
export PIP_CACHE_DIR=/root/autodl-tmp/pip_cache
export TMPDIR=/root/autodl-tmp/tmp
export CUDA_VISIBLE_DEVICES=0
export OMP_NUM_THREADS=1
export LD_LIBRARY_PATH=""
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

mkdir -p ../logs ../checkpoints/ours

torchrun \
  --master-addr localhost \
  --master-port 22041 \
  finetune_lora_sft.py \
  --do_train \
  --seed 42 \
  --bits 16 \
  --dataset /root/autodl-tmp/SightGuard/repos/SaferVLM/data/ours/ours_sft_train.json \
  --dataset_format v1 \
  --base_model_name liuhaotian/llava-v1.5-7b \
  --image_folder /root/autodl-tmp/SightGuard/repos/SaferVLM/data \
  --vision_tower openai/clip-vit-large-patch14 \
  --mm_vision_select_layer -2 \
  --mm_use_im_start_end False \
  --mm_use_im_patch_token False \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_train_epochs 3 \
  --learning_rate 2e-5 \
  --lr_scheduler_type cosine \
  --warmup_ratio 0.03 \
  --lora_r 16 \
  --lora_alpha 32 \
  --lora_dropout 0.05 \
  --model_max_length 1024 \
  --query_len 128 \
  --response_len 384 \
  --save_steps 250 \
  --save_total_limit 5 \
  --logging_steps 10 \
  --output_dir /root/autodl-tmp/SightGuard/repos/SaferVLM/checkpoints/ours/sft_5090_12k_ep3_lr2e-5_r16 \
  2>&1 | tee ../logs/train_ours_sft_5090_12k_ep3_lr2e-5_r16.log
