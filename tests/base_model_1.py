#!/usr/bin/python3
"""Test to_dict method of BaseModel"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
model_dict = my_model.to_dict()

required_keys = ["id", "created_at", "updated_at", "__class__"]
if all(key in model_dict for key in required_keys):
    print("OK")
