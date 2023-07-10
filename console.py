#!/usr/bin/python3
""" Console """
import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    valid_classes = {'BaseModel': BaseModel, 'User': User,
                     'City': City, 'Place': Place, 'Review': Review,
                     'Amenity': Amenity, 'State': State}

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)
        models.storage.save()

    def do_show(self, arg):
        """Show the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()

        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()

        if key in instances:
            del instances[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances"""
        instances = models.storage.all()

        if not arg:
            print([str(instance) for instance in instances.values()])
            return

        class_name = arg
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        filtered_instances = [str(instance) for instance in instances.values()
                              if instance.__class__.__name__ == class_name]
        print(filtered_instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        instance = instances[key]
        setattr(instance, attr_name, attr_value)
        instance = models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
