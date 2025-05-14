#!/usr/bin/python3
"""Test script for BaseModel"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Print instance
print(my_model)

# Save the instance
my_model.save()
print(my_model)

# Convert to dict and print
my_model_json = my_model.to_dict()
print(my_model_json)

print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
