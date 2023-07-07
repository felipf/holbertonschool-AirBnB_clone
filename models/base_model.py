#!/usr/bin/python3
""" Base Model """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ class construct """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
    def __str__(self):
        """string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update_at takes an update of the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary containing all keys/values of the instance"""
        auxDict = self.__dict__.copy()
        auxDict['__class__'] = self.__class__.__name__
        auxDict['created_at'] = self.created_at.isoformat()
        auxDict['updated_at'] = self.updated_at.isoformat()
        return auxDict
