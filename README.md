# Can GNN be Good Adapter for LLMs?
This repository is an implementation of GraphAdapter - [Can GNN be Good Adapter for LLMs?](https://arxiv.org/abs/2402.12984) in WWW 2024.


## Overview

## Requirements
* python = 3.8
* numpy >= 1.19.5
* pytorch = 1 .10.2
* pyg = 2.3.1
* transformers >= 4.28.1 

For the largest dataset Arxiv, 300G storage are required
## Runing
The datasets this paper used can be downloaded from [here](https://arxiv.org/abs/2402.12984), please download them and put them in datasets to unzip.


### Step 1. Preprocess data for training
```
python3 preprocess.py --dataset_name instagram --gpu 0 --plm_path llama2_path --type pretrain
```
The preprocess.py will load the textual data of instagram and transform the token to embedding by Llama 2 and saved, it will used in training of GraphAdapter.


### Step 2. Training GraphAdapter
```
python3 pretrain.py --dataset_name instagram --hiddensize_gnn 64 --hiddensize_fusion 64 --learning_ratio 5e-4 --batch_size 32 --max_epoch 15 --save_path your_model_save_path
```

### Step 3. Finetuing for downstream task

GraphAdapter require prompt embedding for finetuning,

```
python3 preprocess.py --dataset_name instagram --gpu 0 --plm_path llama2_path --type prompt

```
After preprocess the dataset, now you can finetuning to downstream tasks.
```
python3 finetune.py --dataset_name instagram  --gpu 0  --metric roc --save_path your_model_save_path 
```
Note, your_model_save_path in pretrain.py and finetune.py should be same
