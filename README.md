# ImageInpaint-Tensorflow

图像修复

## 介绍


## 数据集
[图像修复高使用率数据集总结](https://zhuanlan.zhihu.com/p/359084085)

## 使用说明

### 安装环境

- Python3.6
- Tensorflow1.4或者更高的版本，除了tensorflow2.0
- Opencv
- numpy
- scipy
- easydict

### 训练
对于给定的数据集，训练阶段分为两部分。首先使用```confidence-driven reconstruction```损失预训练整个网络，然后在前一阶段收敛后使用```adversarial ```和```ID-MRF loss```进行训练。

1. pretrain
```
python train.py --dataset [DATASET_NAME] --data_file [DATASET_TRAININGFILE] --gpu_ids [NUM] --pretrain_network 1 --batch_size 16
```
2. finetune
```
python train.py --dataset [DATASET_NAME] --data_file [DATASET_TRAININGFILE] --gpu_ids [NUM] --pretrain_network 0 --load_model_dir [PRETRAINED_MODEL_PATH] --batch_size 8
```
参数说明：
- DATASET_TRAININGFILE：训练集文件，包含所有的训练图像的地址，可以使txt文件
- mask_type：掩膜类型

### 测试
1. 下载预训练模型：[paris_streetview](https://drive.google.com/file/d/1wgesxSUfKGyPwGQMw6IXZ9GLeZ7YNQxu/view)，[CelebA-HQ_256](https://drive.google.com/file/d/1zvMMzMCXNxzbYJ_6SEwt3hUShD3Xnz9W/view)，[CelebA-HQ_512](https://drive.google.com/file/d/1cp5e8XyXmHNZWj_piHH4eg4HFi3ICl0l/view)，[Places2](https://drive.google.com/file/d/1aakVS0CPML_Qg-PuXGE1Xaql96hNEKOU/view)。注意一点是这是谷歌云盘，需要科学上网。
2. 解压预训练模型到```./checkpoints```下，当然也可以选择其他文件夹
3. 调用```test.py```文件，然后设定```--dataset_path```和```--load_model_dir```后即可：
```
python test.py --dataset paris_streetview --data_file ./imgs/paris-streetview_256x256/ --load_model_dir ./checkpoints/paris-streetview_256x256_rect --random_mask 0
```


## TODO
- [x] 修改测试过程中的图像resize
- [ ] 修改训练过程中的训练数据显示
- [ ] 修改网络的输入过程：输入ground_true和gound true with mask，而不是random mask

## 参考
1. [Code: Image Inpainting via Generative Multi-column Convolutional Neural Networks](https://github.com/shepnerd/inpainting_gmcnn)
2. [Paper:Image Inpainting via Generative Multi-column Convolutional Neural Networks](https://arxiv.org/pdf/1810.08771.pdf)