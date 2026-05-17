# 实验结果记录文档

项目题目：Reducing the Modality Gap and Improving Jailbreak Robustness in LLaVA-1.5-7B through Multimodal Safety Alignment

学生：Junhan Pu

目标模型：LLaVA-1.5-7B

当前状态：实验结果待填写。后续服务器跑完实验后，把所有 `待填写` 字段补上。

## 1. 实验总览

本文档用于记录最终报告所需的全部实验结果。主要比较以下三个模型：

1. 原始 LLaVA-1.5-7B 基线模型
2. Bridging-the-Gap 风格对比模型
3. 我们微调后的多模态安全对齐模型

评测包含两个 benchmark：

1. UnsafeConcepts
2. JailBreakV 固定 2000 样本分层子集

## 2. 实验环境

### 2.1 硬件与运行环境

| 项目 | 数值 / 说明 |
| --- | --- |
| 服务器 / GPU 型号 | 待填写 |
| GPU 数量 | 待填写 |
| GPU 显存 | 待填写 |
| CUDA 版本 | 待填写 |
| Python 版本 | 待填写 |
| PyTorch 版本 | 待填写 |
| Transformers 版本 | 待填写 |
| LLaVA 代码库 / commit | SaferVLM 仓库：`repos/SaferVLM`；JailBreakV 仓库：`repos/JailBreakV_28K` |
| 评测日期 | 待填写 |

### 2.2 目标模型

| 模型名称 | checkpoint / 路径 | 说明 |
| --- | --- | --- |
| 原始 LLaVA-1.5-7B | 待填写 | 基线模型 |
| Bridging-the-Gap 风格模型 | 待填写 | 对比模型 |
| 我们的微调模型 | 待填写 | SFT + preference optimization |

### 2.3 我们模型的训练配置

| 项目 | 数值 / 说明 |
| --- | --- |
| 训练数据规模 | 待填写 |
| boundary-aware 样本类别 | 待填写 |
| LoRA rank `r` | 待填写 |
| LoRA alpha | 待填写 |
| LoRA dropout | 待填写 |
| learning rate | 待填写 |
| epoch 数 | 待填写 |
| scheduler | 待填写 |
| warmup ratio | 待填写 |
| max length | 待填写 |
| per-device batch size | 待填写 |
| gradient accumulation steps | 待填写 |
| effective batch size | 待填写 |
| preference optimization 数据规模 | 待填写 |
| preference optimization 方法 | 待填写 |
| 最终 checkpoint 路径 | 待填写 |

## 3. 数据集与评测划分

### 3.1 UnsafeConcepts

| 项目 | 数值 / 说明 |
| --- | --- |
| 数据集路径 | `repos/SaferVLM/data/UnsafeConcepts` |
| 总样本数 | 1567 |
| unsafe categories | 待填写 |
| 评测设置 | Perception、Alignment、Text-only |
| judge / scoring 方法 | 待填写 |

### 3.2 JailBreakV 固定子集

| 攻击类型 | 样本数 |
| --- | ---: |
| Template | 740 |
| Persuade | 130 |
| Logic | 30 |
| figstep | 500 |
| SD | 200 |
| SD_typo | 200 |
| typo | 200 |
| 总计 | 2000 |

| 项目 | 数值 / 说明 |
| --- | --- |
| 数据集路径 | `repos/JailBreakV_28K/JailBreakV_28K` |
| 固定 2000 子集 CSV | `repos/JailBreakV_28K/JailBreakV_28K/JailBreakV_2K_report_subset_seed2024.csv` |
| 子集生成方式 | 固定分层采样 |
| 随机种子 | 2024 |
| judge / ASR 计算方法 | 待填写 |

## 4. 实验一：原始模型在 UnsafeConcepts 上的结果

实验目标：评估原始 LLaVA-1.5-7B 是否存在 unsafe visual perception 与最终安全对齐响应之间的 modality gap。

### 4.1 实验结果

| 评测设置 | 分数 |
| --- | ---: |
| Perception | 待填写 |
| Alignment | 待填写 |
| Text-only | 待填写 |

### 4.2 结果备注

- 主要观察：待填写
- 典型失败案例：待填写
- 日志 / 输出路径：待填写

## 5. 实验二：原始模型在 JailBreakV 上的结果

实验目标：测量原始模型在固定 JailBreakV 2000 样本 benchmark 上的 jailbreak vulnerability。

### 5.1 总体结果

| 模型 | 总样本数 | 攻击成功样本数 | ASR |
| --- | ---: | ---: | ---: |
| 原始 LLaVA-1.5-7B | 2000 | 待填写 | 待填写 |

### 5.2 分攻击类型结果

| 攻击类型 | 样本数 | 攻击成功样本数 | ASR |
| --- | ---: | ---: | ---: |
| Template | 待填写 | 待填写 | 待填写 |
| Persuade | 待填写 | 待填写 | 待填写 |
| Logic | 待填写 | 待填写 | 待填写 |
| figstep | 待填写 | 待填写 | 待填写 |
| SD | 待填写 | 待填写 | 待填写 |
| SD_typo | 待填写 | 待填写 | 待填写 |
| typo | 待填写 | 待填写 | 待填写 |
| Overall | 2000 | 待填写 | 待填写 |

### 5.3 结果备注

- 最强攻击类型：待填写
- 最弱攻击类型：待填写
- 日志 / 输出路径：待填写

## 6. 实验三：Bridging-the-Gap 风格模型在 JailBreakV 上的结果

实验目标：测试以 modality-gap alignment 为主的对比模型是否能迁移到 jailbreak robustness。

### 6.1 总体结果

| 模型 | 总样本数 | 攻击成功样本数 | ASR |
| --- | ---: | ---: | ---: |
| Bridging-the-Gap 风格模型 | 2000 | 待填写 | 待填写 |

### 6.2 分攻击类型结果

| 攻击类型 | 样本数 | 攻击成功样本数 | ASR |
| --- | ---: | ---: | ---: |
| Template | 待填写 | 待填写 | 待填写 |
| Persuade | 待填写 | 待填写 | 待填写 |
| Logic | 待填写 | 待填写 | 待填写 |
| figstep | 待填写 | 待填写 | 待填写 |
| SD | 待填写 | 待填写 | 待填写 |
| SD_typo | 待填写 | 待填写 | 待填写 |
| typo | 待填写 | 待填写 | 待填写 |
| Overall | 2000 | 待填写 | 待填写 |

### 6.3 与原始模型的对比

| 攻击类型 | 原始模型 ASR | Bridging-the-Gap ASR | 绝对变化 |
| --- | ---: | ---: | ---: |
| Template | 待填写 | 待填写 | 待填写 |
| Persuade | 待填写 | 待填写 | 待填写 |
| Logic | 待填写 | 待填写 | 待填写 |
| figstep | 待填写 | 待填写 | 待填写 |
| SD | 待填写 | 待填写 | 待填写 |
| SD_typo | 待填写 | 待填写 | 待填写 |
| typo | 待填写 | 待填写 | 待填写 |
| Overall | 待填写 | 待填写 | 待填写 |

### 6.4 结果备注

- 改善明显的攻击类型：待填写
- 几乎没有改善的攻击类型：待填写
- 日志 / 输出路径：待填写

## 7. 实验四：我们的微调模型在 UnsafeConcepts 上的结果

实验目标：评估我们的多模态安全对齐方法是否能缩小 modality gap，同时尽量不损害 perception 和 text-only safety behavior。

### 7.1 实验结果

| 评测设置 | 原始模型分数 | 我们的微调模型分数 | 绝对变化 |
| --- | ---: | ---: | ---: |
| Perception | 待填写 | 待填写 | 待填写 |
| Alignment | 待填写 | 待填写 | 待填写 |
| Text-only | 待填写 | 待填写 | 待填写 |

### 7.2 结果备注

- 主要提升：待填写
- perception 是否下降：待填写
- text-only 是否下降：待填写
- 日志 / 输出路径：待填写

## 8. 实验五：我们的微调模型在 JailBreakV 上的结果

实验目标：评估我们的方法是否能在固定 JailBreakV benchmark 上提升 jailbreak robustness。

### 8.1 总体结果

| 模型 | 总样本数 | 攻击成功样本数 | ASR |
| --- | ---: | ---: | ---: |
| 我们的微调模型 | 2000 | 待填写 | 待填写 |

### 8.2 分攻击类型结果

| 攻击类型 | 样本数 | 攻击成功样本数 | ASR |
| --- | ---: | ---: | ---: |
| Template | 待填写 | 待填写 | 待填写 |
| Persuade | 待填写 | 待填写 | 待填写 |
| Logic | 待填写 | 待填写 | 待填写 |
| figstep | 待填写 | 待填写 | 待填写 |
| SD | 待填写 | 待填写 | 待填写 |
| SD_typo | 待填写 | 待填写 | 待填写 |
| typo | 待填写 | 待填写 | 待填写 |
| Overall | 2000 | 待填写 | 待填写 |

### 8.3 结果备注

- 微调后仍然最强的攻击类型：待填写
- 改善最大的攻击类型：待填写
- 日志 / 输出路径：待填写

## 9. 三个模型在 JailBreakV 上的总对比

### 9.1 总体对比

| 模型 | 攻击成功样本数 | ASR |
| --- | ---: | ---: |
| 原始 LLaVA-1.5-7B | 待填写 | 待填写 |
| Bridging-the-Gap 风格模型 | 待填写 | 待填写 |
| 我们的微调模型 | 待填写 | 待填写 |

### 9.2 分攻击类型对比

| 攻击类型 | 原始模型 ASR | Bridging-the-Gap ASR | 我们的微调模型 ASR |
| --- | ---: | ---: | ---: |
| Template | 待填写 | 待填写 | 待填写 |
| Persuade | 待填写 | 待填写 | 待填写 |
| Logic | 待填写 | 待填写 | 待填写 |
| figstep | 待填写 | 待填写 | 待填写 |
| SD | 待填写 | 待填写 | 待填写 |
| SD_typo | 待填写 | 待填写 | 待填写 |
| typo | 待填写 | 待填写 | 待填写 |
| Overall | 待填写 | 待填写 | 待填写 |

### 9.3 ASR 绝对下降

| 对比 | ASR 绝对下降 |
| --- | ---: |
| 原始模型 -> Bridging-the-Gap | 待填写 |
| 原始模型 -> 我们的微调模型 | 待填写 |
| Bridging-the-Gap -> 我们的微调模型 | 待填写 |

### 9.4 结果备注

- Bridging-the-Gap 是否能有效迁移到 jailbreak robustness：待填写
- 我们的方法是否改善 text-heavy attacks：待填写
- 我们的方法是否改善 vision-related / mixed attacks：待填写

## 10. 响应类型分布分析

实验目标：用 `SAFE`、`UNSAFE`、`BAD` 标签分析 alignment 前后生成回答的变化。

### 10.1 对齐前

| 响应类型 | 数量 | 比例 |
| --- | ---: | ---: |
| SAFE | 待填写 | 待填写 |
| UNSAFE | 待填写 | 待填写 |
| BAD | 待填写 | 待填写 |
| Total | 待填写 | 100% |

### 10.2 对齐后

| 响应类型 | 数量 | 比例 |
| --- | ---: | ---: |
| SAFE | 待填写 | 待填写 |
| UNSAFE | 待填写 | 待填写 |
| BAD | 待填写 | 待填写 |
| Total | 待填写 | 100% |

### 10.3 结果备注

- SAFE 响应增加幅度：待填写
- UNSAFE 响应下降幅度：待填写
- BAD 响应下降幅度：待填写
- 日志 / 输出路径：待填写

## 11. 需要生成的图

| 图编号 | 内容 | 数据来源 | 状态 |
| --- | --- | --- | --- |
| Figure 1 | 原始模型与 Bridging-the-Gap 在 JailBreakV 上的 motivation comparison | 第 5-6 节 | 待生成 |
| Figure 2 | 整体实验流程图 | 方法描述 | 待生成 |
| Figure 3 | 防御策略详细流程图 | 方法描述 | 待生成 |
| Figure 4 | UnsafeConcepts 微调前后对比 | 第 4 节和第 7 节 | 待生成 |
| Figure 5 | 三个模型在 JailBreakV 上的 ASR 对比 | 第 9 节 | 待生成 |
| Figure 6 | 对齐前后响应类型分布 | 第 10 节 | 待生成 |

## 12. 最终报告结论检查表

在写最终版本之前，需要用真实实验结果检查下面每个结论是否成立。

| 结论 | 是否支持 | 证据 |
| --- | --- | --- |
| 原始模型在 UnsafeConcepts 上 perception 高但 alignment 低 | 待填写 | 待填写 |
| 原始模型容易受到 JailBreakV 攻击 | 待填写 | 待填写 |
| Bridging-the-Gap 有一定改善，但总体仍不够 | 待填写 | 待填写 |
| Bridging-the-Gap 对 text-heavy attacks 改善有限 | 待填写 | 待填写 |
| 我们的方法提升 UnsafeConcepts alignment | 待填写 | 待填写 |
| 我们的方法基本保持 perception 稳定 | 待填写 | 待填写 |
| 我们的方法基本保持 text-only 行为稳定 | 待填写 | 待填写 |
| 我们的方法降低 JailBreakV 总体 ASR | 待填写 | 待填写 |
| Logic 仍然是较难防御的攻击类型之一 | 待填写 | 待填写 |
| 对齐后响应类型分布改善 | 待填写 | 待填写 |

## 13. 原始结果文件记录

从实验服务器拿到结果后，在这里记录每个文件的精确路径。

| 实验 | 文件路径 | 说明 |
| --- | --- | --- |
| 原始模型 UnsafeConcepts | 待填写 | 待填写 |
| 原始模型 JailBreakV | 待填写 | 待填写 |
| Bridging-the-Gap JailBreakV | 待填写 | 待填写 |
| 我们的模型 UnsafeConcepts | 待填写 | 待填写 |
| 我们的模型 JailBreakV | 待填写 | 待填写 |
| 响应类型分析 | 待填写 | 待填写 |
| 训练日志 | 待填写 | 待填写 |

## 14. 未解决问题

- 待填写

## 15. 最终总结草稿

所有结果填完后，在这里写最终报告可直接使用的简短总结。

待填写
