#!/usr/bin/python3
"""
creation of class review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review from basemodel"""
    place_id = ""
    user_id = ""
    text = ""
