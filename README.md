# EfficientNet Pytorch
*Have fun with your own data!*
## Quick Start
### Install Package
```bash
pip install efficientnet_pytorch
```
### Load Model
Load an EfficientNet:
```python
from efficientnet_pytorch import EfficientNet
model = EfficientNet.from_name('efficientnet-b0')
```
Load a pretrained model:
```python
from efficientnet_pytorch import EfficientNet
model = EfficientNet.from_pretrained('efficientnet-b0')
```

Details about the models are below:

|      *Name*       | *# Params* | *Top-1 Acc.* | *Pretrained?* |
| :---------------: | :--------: | :----------: | :-----------: |
| `efficientnet-b0` |    5.3M    |     76.3     |       ✓       |
| `efficientnet-b1` |    7.8M    |     78.8     |       ✓       |
| `efficientnet-b2` |    9.2M    |     79.8     |       ✓       |
| `efficientnet-b3` |    12M     |     81.1     |       ✓       |
| `efficientnet-b4` |    19M     |     82.6     |       ✓       |
| `efficientnet-b5` |    30M     |     83.3     |       ✓       |
| `efficientnet-b6` |    43M     |     84.0     |       ✓       |
| `efficientnet-b7` |    66M     |     84.4     |       ✓       |


### Run tests
```bash
python3 test.py --image test.png
```

## Train on Own Data
### Basic
First, you should make sure your dataset is in the following format.
If not, you can try [this repo](https://github.com/LovelyQuantum/dataset_formater) to help you reform it.
```
dataset/
├── train
│   ├── class00 (class name, can be string like bird, dog etc.)
│   ├── class01
│   ├── class02
│   ├── class03
│   ├── class04
│   └── ...
└── val
    ├── class00 (class name, should correspond to class names in the train set)
    ├── class01
    ├── class02
    ├── class03
    ├── class04
    └── ...
```


Then, run as following:
```bash
python3 train train.py --dataset (your dataset path) --model_save_path (path to save model weights)
```
Example:
```bash
python3 train train.py --dataset ./dataset --model_save_path ./weights
```
### Advanced
The `train.py` supports the following options:
|       *Name*        |              *Description*               |            *Usage*             |
| :-----------------: | :--------------------------------------: | :----------------------------: |
|     `--dataset`     |            your dataset path             |     `--dataset ./dataset`      |
| `--model_save_path` |        path to save model weights        | `--model_save_path ./weights`  |
|   `--batch_size`    |      depend on your gpu memory size      |        `--batch_size 8`        |
|   `--pretrained`    |     whether to use pretrained model      |         `--pretrained`         |
|   `--num_epochs`    |             epochs to train              |       `--num_epochs 40`        |
|   `--model_name`    |     which model to train(list above)     | `--model_name efficientnet-b7` |
|   `--load_weight`   | load your own weight as pretrained model |   `--load_weight ./best.pth`   |
| `--save_all_models` |        whether to save all models        |      `--save_all_models`       |
|   `--quiet_mode`    |       whether to run in quiet mode       |         `--quiet_mode`         |
