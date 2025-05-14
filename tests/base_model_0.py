#!/usr/bin/python3
"""Test save method of BaseModel"""

import sys
import os
import time
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.base_model import BaseModel

my_model = BaseModel()
old_updated_at = my_model.updated_at

time.sleep(0.01)
my_model.save()

if my_model.updated_at > old_updated_at:
    print("OK")
