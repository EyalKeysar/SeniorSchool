
from .internal_command import InternalCommand

class EchoCommand(InternalCommand):

    name = "echo"
    description = "Print the given arguments"

    def __init__(self, args, redirect=None):
        self.args = args
        self.redirect = redirect
    
    def execute(self, arg):
        return str(arg)