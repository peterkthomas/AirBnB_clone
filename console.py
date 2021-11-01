#!/usr/bin/python3
"""
    File: console.py
"""
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """HBNB Console Class"""

    prompt = "(hbnb)"
    class_list = {
        "BaseModel": BaseModel, "UserModel": User, "State": State,
        "Review": Review, "City": City, "Amenity": Amenity, "Place": Place
    }

    def do_quit(self, arg):
        """Exits the program"""
        sys.exit()

    def do_EOF(self, arg):
        """Catches EOF keyboard entry"""
        print()
        return True

    def emptyline(self):
        """Makes it so an empty line doesn't do anything"""
        print("", end="")

    def do_create(self, arg):
        """Creates new instance of BaseModel"""
        new_arg = arg.split()
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            new_model = self.class_list[new_arg[0]]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Prints the string represenation of the object """
        new_arg = arg.split()
        class_id = ''
        if len(new_arg) >= 2:
            class_id = new_arg[0] + '.' + new_arg[1]
        if not arg:
            print("** class name missing **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        elif new_arg[0] not in self.class_list:
            print("** class doesn't exist **")
        try:
            models.storage.all()[class_id]
            models.storage.save()
        except Exception:
            return print("** no instance found **")

    def do_destroy(self, arg):
        new_arg = arg.split()
        class_id = ''
        if len(new_arg) >= 2:
            class_id = new_arg[0] + '.' + new_arg[1]
        if not arg:
            return print("** class name missing **")
        elif new_arg[0] not in self.class_list:
            return print("** class doesn't exist **")
        elif len(new_arg) < 2:
            return print("** instance id missing **")

        """ elif class_id not in models.storage.all:
           return print("** no instance found **")

         else:
            models.storage.all.delete(class_id)
            models.storage.save()
        """
        try:
            models.storage.all().delete(class_id)
            models.storage.save()
        except Exception:
            return print("** no instance found **")


    def do_all(self, arg):
        new_arg = arg.split()
        if len(new_arg) >= 1:
            if new_arg[0] not in self.class_list:
                print("*** class doesn't exist ***")
            else:
                for n in models.storage.all():
                    print(n)
        else:
            for n in models.storage.all():
                print(n)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
