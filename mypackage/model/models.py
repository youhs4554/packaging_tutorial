import torch.nn as nn

class SimpleCNN(nn.Sequential):
    def __init__(self, num_class=10):
        super().__init__()
        self.add_module('conv1', nn.Conv2d(3, 16, kernel_size=3))
        self.add_module('relu1', nn.ReLU(True))
        self.add_module('maxpool1', nn.MaxPool2d(2))
        self.add_module('conv2', nn.Conv2d(16, 32, kernel_size=3))
        self.add_module('relu2', nn.ReLU(True))
        self.add_module('maxpool2', nn.MaxPool2d(2))
        self.add_module('conv3', nn.Conv2d(32, 64, kernel_size=3))
        self.add_module('relu3', nn.ReLU(True))
        self.add_module('maxpool3', nn.MaxPool2d(2))
        self.add_module('avgpool', nn.AdaptiveAvgPool2d(1))
        self.add_module('flatten', nn.Flatten(1))
        self.add_module('classifier', nn.Linear(64, num_class))