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

    def do_quit(self, line):
        """Exits the program"""
        sys.exit()

    def do_EOF(self, line):
        """Catches EOF keyboard entry"""
        print()
        return True

    def emptyline(self):
        """Makes it so an empty line doesn't do anything"""
        print("", end="")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
