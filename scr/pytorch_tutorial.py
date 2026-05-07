import torch
import numpy as np

# type() function is used to find the type of variable
# size() function is used to find the shape of the tensor. 
    # TENSOR_VAR.size()


#Working with numpy array and tensors
a = torch.ones(5)
print(a)

# Convert the numpy array to a tensor using the TENSOR_VAR.numpy()
b = a.numpy()
print(b)
print(type(a))
print(type(b))
print(a.size())