#!/usr/bin/python3
import cmd
import shlex
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[cls_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        args = shlex.split(arg)
        objs = storage.all()
        result = []
        if args and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for obj in objs.values():
                if not args or obj.__class__.__name__ == args[0]:
                    result.append(str(obj))
            print(result)

    def do_update(self, arg):
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print()
