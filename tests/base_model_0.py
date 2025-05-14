#!/usr/bin/python3
"""Test save() method of BaseModel"""

import sys
import os
from datetime import datetime
from time import sleep

# Add models path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel

my_model = BaseModel()
prev_updated_at = my_model.updated_at
sleep(0.01)
my_model.save()

if my_model.updated_at > prev_updated_at:
    print("OK")
else:
    print("Failed")
