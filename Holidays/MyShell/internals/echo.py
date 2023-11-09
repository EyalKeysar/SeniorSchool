
from .internal_command import InternalCommand
from .helpers import handle_stdout

class EchoCommand(InternalCommand):

    name = "echo"
    description = "Print the given arguments"

    def __init__(self, args, redirect=None):
        self.args = args
        self.redirect = redirect
    
    def execute(self):

        stdout_printable = " ".join(self.args)
        handle_stdout(self.redirect, stdout_printable)