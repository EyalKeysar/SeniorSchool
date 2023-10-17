import os

from .internal_command import InternalCommand
from .helpers import handle_stdout

class LsCommand(InternalCommand):

    name = "ls"
    description = "Lists the contents of the current directory"

    def __init__(self, args, redirect=None):
        self.args = args
        self.stdout = ""
        self.redirect = redirect

    def execute(self):
        self.stdout = ""

        if(len(self.args) == 0):
            self.args.append(".")
        for arg in self.args:
            try:
                self.stdout += "\n" + str(os.listdir(arg)) + "\n"
            except FileNotFoundError:
                self.stdout += f"ls: {str(arg)}: No such file or directory\n"
            except NotADirectoryError:
                self.stdout += f"ls: {str(arg)}: Not a directory\n"
            except PermissionError:
                self.stdout += f"ls: {str(arg)}: Permission denied\n"

        handle_stdout(self.redirect, self.stdout)