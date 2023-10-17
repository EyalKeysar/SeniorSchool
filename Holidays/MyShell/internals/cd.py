import os

from .internal_command import InternalCommand

class CdCommand(InternalCommand):
    def __init__(self):
        super().__init__("cd", "Change directory")

    def execute(self, arg):
        try:
            os.chdir(arg.strip())
        except FileNotFoundError:
            return f"cd: {arg}: No such file or directory"
        return ""