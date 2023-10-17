
from .internal_command import InternalCommand

class EchoCommand(InternalCommand):
    def __init__(self):
        super().__init__("echo", "Print the given arguments")
    
    def execute(self, arg):
        return str(arg)