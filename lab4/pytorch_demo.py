# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 18:41:46 2025

@author: Vaishali Siddeshwar
PyTorch Basics Exercise
------------------------
This script introduces tensors in PyTorch.
Students will practice:
- Creating tensors of different dimensions
- Reshaping tensors
- Performing mathematical operations
- Broadcasting
- Indexing and slicing
- converting between numpy, tensorflow and torch tensors
- Single-Layer Neural Network
"""

import torch
import numpy as np
import tensorflow as tf
# -----------------------------------------------------------
# Part 1: Tensor Creation
# -----------------------------------------------------------

# Scalar (0D tensor)
scalar = torch.tensor(5)
print("Scalar:\n", scalar)
print("Shape:", scalar.shape, " | Dimensions:", scalar.ndim, "\n")

# Vector (1D tensor)
vector = torch.rand(5)  # 5 random values
print("Vector:\n", vector)
print("Shape:", vector.shape, " | Dimensions:", vector.ndim, "\n")

# Matrix (2D tensor)
matrix = torch.ones((3, 3))  # 3x3 matrix of ones
print("Matrix:\n", matrix)
print("Shape:", matrix.shape, " | Dimensions:", matrix.ndim, "\n")

# 3D Tensor
tensor3D = torch.rand((2, 3, 4))  # 2x3x4 tensor
print("3D Tensor:\n", tensor3D)
print("Shape:", tensor3D.shape, " | Dimensions:", tensor3D.ndim, "\n")


# -----------------------------------------------------------
# Part 2: Reshaping Tensors
# -----------------------------------------------------------

# Create a tensor with values 0 to 11
x = torch.arange(12)
print("Original 1D Tensor:\n", x)

# Reshape to 3x4
x_reshaped = x.reshape(3, 4)
print("Reshaped to 3x4:\n", x_reshaped)

# Reshape to 2x2x3
x_reshaped_3d = x.reshape(2, 2, 3)
print("Reshaped to 2x2x3:\n", x_reshaped_3d)

# Note: Trying to reshape into incompatible dimensions (like 5x5) will throw an error.


# -----------------------------------------------------------
# Part 3: Mathematical Operations
# -----------------------------------------------------------

# Two random 2x2 matrices
a = torch.rand((2, 2))
b = torch.rand((2, 2))

print("Matrix A:\n", a)
print("Matrix B:\n", b)

# Elementwise addition
print("A + B (elementwise):\n", a + b)

# Elementwise multiplication
print("A * B (elementwise):\n", a * b)

# Matrix multiplication
print("A @ B (matrix multiplication):\n", torch.matmul(a, b))


# -----------------------------------------------------------
# Part 4: Broadcasting
# -----------------------------------------------------------

# Create a 3x3 matrix
M = torch.randint(1, 10, (3, 3))  # random integers between 1 and 9
v = torch.tensor([1, 2, 3])

print("Matrix M:\n", M)
print("Vector v:\n", v)

# Adding vector to matrix (broadcasting)
print("M + v (with broadcasting):\n", M + v)


# -----------------------------------------------------------
# Part 5: Indexing and Slicing
# -----------------------------------------------------------

# Create a 4x4 tensor with values 0 to 15
grid = torch.arange(16).reshape(4, 4)
print("4x4 Grid:\n", grid)

# First row
print("First row:\n", grid[0])

# Last column
print("Last column:\n", grid[:, -1])

# 2x2 submatrix from the center
print("Center 2x2 submatrix:\n", grid[1:3, 1:3])

# -----------------------------------------------------------
# Part 6: Conversions between numpy, pytorch and tensorflow arrays
# -----------------------------------------------------------


print("\n--- Conversions between PyTorch, NumPy, and TensorFlow ---\n")

# 1. PyTorch tensor → NumPy array
torch_tensor = torch.tensor([1, 2, 3, 4, 5])
numpy_array = torch_tensor.numpy()
print("PyTorch → NumPy:\n", numpy_array, type(numpy_array))

# 2. NumPy array → PyTorch tensor
numpy_array2 = np.array([10, 20, 30, 40])
torch_tensor2 = torch.from_numpy(numpy_array2)
print("NumPy → PyTorch:\n", torch_tensor2, type(torch_tensor2))

# 3. PyTorch tensor → TensorFlow tensor
torch_tensor3 = torch.rand(3, 3)
tf_tensor = tf.convert_to_tensor(torch_tensor3.numpy())
print("PyTorch → TensorFlow:\n", tf_tensor, type(tf_tensor))

# 4. TensorFlow tensor → PyTorch tensor
tf_tensor2 = tf.constant([[1.0, 2.0], [3.0, 4.0]])
torch_tensor4 = torch.from_numpy(tf_tensor2.numpy())
print("TensorFlow → PyTorch:\n", torch_tensor4, type(torch_tensor4))


# -----------------------------------------------------------
# Part 7: Single-Layer Neural Network Example
# -----------------------------------------------------------

import torch
import torch.nn as nn

print("\n--- Single-Layer Neural Network ---\n")

# Define a simple single-layer network
class SingleLayerNN(nn.Module):
    def __init__(self, input_size, output_size):
        super(SingleLayerNN, self).__init__()
        # Just one linear layer
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        # Pass input through the layer
        out = self.fc(x)
        return out

# Create model: input has 4 features, output has 2 classes
model = SingleLayerNN(input_size=4, output_size=2)

# Create a sample input tensor (batch of 3 samples, each with 4 features)
sample_input = torch.rand((3, 4))
print("Input Tensor Shape:", sample_input.shape, "\n", sample_input)

# Forward pass through the network
output = model(sample_input)

print("\nOutput Tensor Shape:", output.shape, "\n", output)