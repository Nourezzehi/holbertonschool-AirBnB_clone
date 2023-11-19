#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNB for command line"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command to exit console"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit console"""
        return True

    def emptyline(self):
        """nothing to execute"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
