# MHIST_Image_Classification_Task

BEST RESULTS IN -  Training_without_augmentation.ipynb

DATA EXPLORATION IN - Training_without_augmentation.ipynb/Training_with_augmentation.ipynb

HEATMAP IN - Evaluation.ipynb

LOSS GRAPH - Training_without_augmentation.ipynb

There are 3 Training files:
1. Training_without_augmentation.ipynb
2. Training_with_augmentation.ipynb
3. Implementation_CNN_scratch.ipynb

The best test accuracy so far is 84% using Training_without_augmentation.ipynb where the following is done:
1. Since the data is imbalanced, we first check the ambigious labels, which can lead our model towards wrong prediction, to fight this challenge, we only take the datapoints which are highly confident i.e most voters predicted the same label.
2. Then we use this data to train our model using transfer learning
  In transfer learning, we used the following models:
    1. Resnet18
    2. Resnet50
    3. vgg_net
    4. efficient_net
    5. ViT

Hyperparameter Tuning is also implemented and L1 regularization is introduced using weight decay

TO CHECK THE RESULTS - open Evaluation.ipynb file

To download the models, you can refer to this link - https://drive.google.com/drive/folders/1SucPWwk6N2l-z1p88ZaEM1oUjtKQXTx_?usp=drive_link

### CHECK THE LOCATION OF ALL THE FILES IN THE DEFINE VARIABLE SECTION, IN CASE OF RETRAIN
