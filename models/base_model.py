#!/usr/bin/python3
""" Base Model """
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ class construct """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update_at takes an update of the current time"""
        self.update_at = datetime.today()

    def to_dict(self):
        """dictionary containing all keys/values of the instance"""
        auxDict = self.__dict__
        auxDict["__class__"] = self.__class__
        auxDict['created_at'] = auxDict['created_at'].isoformat()
        auxDict['updated_at'] = auxDict['updated_at'].isoformat()
        return auxDict
