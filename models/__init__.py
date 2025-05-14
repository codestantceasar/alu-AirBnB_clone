class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            # This handles creation from a dictionary
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # don't set __class__ as an attribute
                if key in ('created_at', 'updated_at'):
                    # Convert string to datetime object
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            # Normal instance creation
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
