#!/usr/bin/python3
"""
    File: console.py
"""
import cmd
import sys
import models

class HBNBCommand(cmd.Cmd):
    """HBNB Console Class"""

    prompt = "(hbnb)"

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
    
    



















    def do_all(self,arg):
        new_arg = args.split()
        class_list =
        {
                "BaseModel": BaseModel
        }
        if new_arg[0] not in self.class_list:
            print("*** class doesn't exist ***")










if __name__ == '__main__':
    HBNBCommand().cmdloop()
