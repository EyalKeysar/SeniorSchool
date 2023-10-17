import os

from .internal_command import InternalCommand
from .helpers import handle_stdout
class CdCommand(InternalCommand):

    name = "cd"
    description = "Changes the current directory"

    def __init__(self, args, redirect=None):
        self.args = args
        self.stdout = ""
        self.redirect = redirect

    def execute(self):
        self.stdout = ""
        try:
            os.chdir(self.args[0])
        except FileNotFoundError:
            self.stdout = f"cd: {self.args[0]}: No such file or directory", True
        except NotADirectoryError:
            self.stdout = f"cd: {self.args[0]}: Not a directory", True
        except PermissionError:
            self.stdout = f"cd: {self.args[0]}: Permission denied", True

        handle_stdout(self.redirect, self.stdout)