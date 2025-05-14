#!/usr/bin/python3
"""Test script for BaseModel's to_dict method"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel

# Create instance and assign attributes
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Convert to dictionary
model_dict = my_model.to_dict()

# Print dictionary
print(model_dict)

# Print each key-value pair with type
print("Dictionary representation:")
for key, value in model_dict.items():
    print("\t{}: ({}) - {}".format(key, type(value), value))
