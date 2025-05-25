from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        from models import storage  # ✅ Lazy import inside method

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        from models import storage  # ✅ Lazy import inside method
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
