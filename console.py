#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the program when EOF is reached (Ctrl+D)"""
        print()
        return True

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when the line is empty"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()