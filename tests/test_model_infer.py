import torch
from mypackage.model.models import SimpleCNN

def infer(x, num_class):
    cnn = SimpleCNN(num_class)
    output = cnn(x)
    return output
    
def test_infer():
    x = torch.randn(4, 3, 28, 28)
    num_class = 7
    assert infer(x, num_class).shape == (4, num_class)