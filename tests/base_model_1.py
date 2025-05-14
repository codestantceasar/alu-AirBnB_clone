#!/usr/bin/python3
"""Test to_dict() method of BaseModel"""

import sys
import os

# Add models path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel

my_model = BaseModel()
model_dict = my_model.to_dict()

# Check presence of expected keys
if isinstance(model_dict, dict) and all(k in model_dict for k in ["id", "created_at", "updated_at", "__class__"]):
    print("OK")
else:
    print("Failed")
