import sys
from .internal_command import InternalCommand

class ExitCommand(InternalCommand):

    name = "exit"
    description = "Exit the shell"

    def __init__(self, args, redirect=None):
        self.args = args
        self.redirect = redirect


    def execute(self, arg):
        sys.exit(0)