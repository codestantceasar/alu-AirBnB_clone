#!/usr/bin/python3
"""Test script for BaseModel's __str__ method"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel

# Create instance
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Print string representation
print(str(my_model))
