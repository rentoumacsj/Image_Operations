# Image_Operations
* 图像处理常用操作的python实现，包括抠图、拼接、粘贴等操作。

## Requirements
* python 3.8 or newer
* torch and torchvision stable version (https://pytorch.org)

### 安装torch/torchvision
* 在官网https://pytorch.org 上安装pytorch。<br>
* pip安装指令（例）： pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 -f 

### 安装rembg模块
* pip install rembg

## remove_background_black.py
* 图像去背景并保存为黑色背景图片，jpg格式（RGB通道）。
* 批量实现：配置res_dir和des_dir路径。<br>
 ![image](https://github.com/rentoumacsj/Image_Operations/blob/main/sample_output/fg_black.png)

## remove_background_transparent.py
* 图像去背景并保存为透明背景图片，png格式（RGBA通道）。
* 批量实现：配置res_dir和des_dir路径。<br>
 ![image](https://github.com/rentoumacsj/Image_Operations/blob/main/sample_output/fg_transparent.png)

## image_concat.py
* 图像拼接处理，可用于论文图像对比实验。<br>
 ![image](https://github.com/rentoumacsj/Image_Operations/blob/main/concat_output/compare.png)

## image_paste.py
* 图像粘贴操作，用于将透明背景图像粘贴到给定底图上。<br>
 ![image](https://github.com/rentoumacsj/Image_Operations/blob/main/paste_output/sample.png)


