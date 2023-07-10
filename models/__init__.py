#!/usr/bin/python3
""" module models """


from models.engine.file_storage import FileStorage

valid_classes = {'BaseModel': 'BaseModel', 'User': 'User',
                 'City': 'City', 'Place': 'Place', 'Review': 'Review',
                 'Amenity': 'Amenity', 'State': 'State'}
storage = FileStorage()
storage.reload()
