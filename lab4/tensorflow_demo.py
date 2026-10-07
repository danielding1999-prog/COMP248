import tensorflow as tf
from tensorflow import keras
import numpy as np

"""Section #1. Creating Tensors
A tensor is just a multi-dimensional array (like a NumPy array).
A scalar → 0D tensor (just one number)
A vector → 1D tensor (list of numbers)
A matrix → 2D tensor (rows × columns)
Higher dimensions → 3D, 4D, … tensors
In TensorFlow, everything (data, inputs, weights) is represented as tensors.
"""

# Scalar (0D tensor)
scalar = tf.constant(5)
print("Scalar:", scalar)

# Vector (1D tensor)
vector = tf.constant([1, 2, 3])
print("Vector:", vector)

# Matrix (2D tensor)
matrix = tf.constant([[1, 2], [3, 4]])
print("Matrix:", matrix)

# 3D Tensor
tensor3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Tensor:", tensor3d)

print("################################# End of Section 1 #################################")

"""Section #2. Tensor Properties
Tensors have a few important attributes:
"""

print("Shape:", matrix.shape)      # (2, 2)
print("Rank (dimensions):", tf.rank(matrix))
print("Data type:", matrix.dtype)

print("################################# End of Section 2 #################################")



"""Section #3. Load Data into Tensors"""

# You can load data in Python List to a tensor
data = [1, 2, 3, 4, 5]
tensor = tf.constant(data, dtype=tf.float32)
print(tensor)

# You can load data in NumPy Arrays Python List to a tensor 
np_array = np.array([[1, 2, 3], [4, 5, 6]])
tensor_from_np = tf.convert_to_tensor(np_array, dtype=tf.float32)
print(tensor_from_np)

# You can generate Random Tensors
random_tensor = tf.random.uniform(shape=(3, 3), minval=0, maxval=10)
print(random_tensor)


print("################################# End of Section 3 #################################")

''' Section #4. Basic Tensor Operations

# You can do math directly on tensors:
'''
    
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Matrix multiplication:", tf.matmul([[1, 2]], [[3], [4]]))  # [[1*3 + 2*4]]


print("################################# End of Section 4 #################################")

"""Sextion #5. Tensors in TensorFlow Models
When you build a neural network in TensorFlow, all the inputs, weights, and outputs are tensors.
Example: Input → Layer → Output

A Dense layer (also called a fully connected layer) is one of the most common building blocks in neural networks

Every neuron in a Dense layer is connected to every neuron in the previous layer and each connection has a weight, and each neuron has a bias.

Mathematically, for input x, weights W, bias b, and activation function f:

output=f(Wx+b)
"""

# Input tensor (batch of numbers)
X = tf.constant([[1.0], [2.0], [3.0]])

# Simple layer: one neuron with weight + bias

layer = keras.layers.Dense(units=1)

# Pass tensor through the layer
output = layer(X)   # Input tensor flows into model
print("Input tensor:\n", X)
print("Output tensor:\n", output)

print("################################# End of Section 5 #################################")




