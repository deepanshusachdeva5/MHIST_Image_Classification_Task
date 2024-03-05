## For Data Loader
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.io import read_image
from torch.utils.data import Dataset
from torchvision.transforms.functional import to_tensor
import torch

import os


class MHIST_Dataset(Dataset):
    def __init__(self, dataframe, img_dir, transform=None, target_transform=None):
        self.img_labels = dataframe
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform


    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        image = torch.tensor(image, dtype=torch.float32)

        if self.img_labels.iloc[idx, 1] == 'SSA':
          label = 0
        else:
          label = 1
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label