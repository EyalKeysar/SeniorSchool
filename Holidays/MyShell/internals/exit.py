import sys
from .internal_command import InternalCommand

class ExitCommand(InternalCommand):
    def __init__(self):
        super().__init__("exit", "Exit the shell")
    
    def execute(self, arg):
        sys.exit(0)