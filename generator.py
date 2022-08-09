# https://github.com/kretovmk/gan_feature_matching_ssl/blob/master/pytorch_improved_gan_v_new.ipynb
import torch
from torch import nn

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.layer1 = nn.Linear(128, 128*5*5)
        self.layer2 = nn.Sequential(
            nn.ConvTranspose2d(128, 384, kernel_size=3, stride=2, padding=0, bias=False),
            nn.BatchNorm2d(384),
            nn.ELU(inplace=True),
            nn.Conv2d(384, 384, 1, 1, 0, bias=False),
            nn.BatchNorm2d(384),
            nn.ELU(inplace=True))
        self.layer3 = nn.Sequential(
            nn.ConvTranspose2d(384, 192, kernel_size=5, stride=2, padding=0, bias=False),
            nn.BatchNorm2d(192),
            nn.ELU(inplace=True),
            nn.Conv2d(192, 192, 1, 1, 0),
            nn.BatchNorm2d(192),
            nn.ELU(inplace=True))
        self.layer4 = nn.Sequential(
            nn.ConvTranspose2d(192, 96, kernel_size=3, stride=2, padding=2),
            nn.BatchNorm2d(96),
            nn.ELU(inplace=True),
            nn.ZeroPad2d((1,0,1,0)),
            nn.ConvTranspose2d(96, 3, 3, 1, 1),
            nn.Tanh())
  
    def forward(self, x):
        x = self.layer1(x)
        x = x.view(-1, 128, 5, 5)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
    
        return x

generator = Generator()