#!/usr/bin/python3
"""Test __str__ method of BaseModel"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.base_model import BaseModel

my_model = BaseModel()
str_output = str(my_model)

if "[BaseModel]" in str_output and my_model.id in str_output:
    print("OK")
