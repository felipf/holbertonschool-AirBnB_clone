#!/usr/bin/python3
"""
creating our user
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """ user from basemodel class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""