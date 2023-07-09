#!/usr/bin/python3
""" unittest for User """
import unittest
import models
from models.user import User


class TestUser(unittest.TestCase):
    """test for class User"""

    def test_str(self):
        """check if the output of str is in the specified format"""
        strObject = User()
        _dict = strObject.__dict__
        str1 = "[User] ({}) {}".format(strObject.id, _dict)
        str2 = str(strObject)
        self.assertEqual(str1, str2)

    def test_save(self):
        """ checks if date is updated if save """
        objectUpdate = User()
        firstUpd = objectUpdate.updated_at
        objectUpdate.save()
        secondUpd = objectUpdate.updated_at
        self.assertNotEqual(firstUpd, secondUpd)

    def test_to_dict(self):
        """ check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format """
        modelUpd = User()
        dictModelUpd = modelUpd.to_dict()
        self.assertIsInstance(dictModelUpd, dict)
        for key, value in dictModelUpd.items():
            flag = 0
            if dictModelUpd['__class__'] == 'User':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in dictModelUpd.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
