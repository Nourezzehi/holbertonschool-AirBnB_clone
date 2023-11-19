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

    def help_quit(self):
        """help quit command"""
        print("Quit command to exit the program\n")

    def do_create(self, arg=None):
        """Create an instance of BaseModel"""
        if not arg or arg != "BaseModel":
            print("** class name missing **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """show instance based on class name and ID"""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Destroy an instance based on class name and Id"""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Display all instances based on class name"""
        arg_list = parse(arg)
        if len(arg_list) > 0 and arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)

    def do_update(self, arg):
        """update an instance attribute"""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            instance = obj_dict[key]
            setattr(instance, arg_list[2], arg_list[3].strip('"'))
            storage.save()


def parse(arg):
    """Convert a series arguments to an argument list"""
    return list(map(str, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
