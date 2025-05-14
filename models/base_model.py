#!/usr/bin/python3
import uuid
from datetime import datetime
import models  # this allows access to models.storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        val = datetime.fromisoformat(val)
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at and saves to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
