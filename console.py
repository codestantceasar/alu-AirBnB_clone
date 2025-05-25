import cmd
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
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            print(all_objs.get(key, "** no instance found **"))

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
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
        if arg and arg not in classes:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            result = []
            for key in objs:
                if not arg or key.startswith(arg + "."):
                    result.append(str(objs[key]))
            print(result)

    def do_update(self, arg):
        args = arg.split()
        if len(args) < 4:
            print("** class name missing **" if len(args) < 1 else
                  "** instance id missing **" if len(args) < 2 else
                  "** attribute name missing **" if len(args) < 3 else
                  "** value missing **")
            return
        cls_name, obj_id, attr_name, attr_val = args[0], args[1], args[2], args[3]
        key = f"{cls_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        try:
            attr_val = eval(attr_val)
        except Exception:
            pass
        setattr(obj, attr_name, attr_val)
        obj.save()

    def do_EOF(self, arg):
        return True

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
