#!/usr/bin/python3
""" Base Model """
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ class construct """

    def __init__(self):
        """initialization value"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update_at takes an update of the current time"""
        self.update_at = datetime.now()

    def to_dict(self):
        """dictionary containing all keys/values of the instance"""
        auxDict = self.__dict__.copy()
        auxDict['__class__'] = self.__class__.__name__
        auxDict['created_at'] = self.created_at.isoformat()
        auxDict['updated_at'] = self.update_at.isoformat()
        return auxDict
