import os

from .internal_command import InternalCommand

class ClsCommand(InternalCommand):
    def __init__(self):
        super().__init__("cls", "Clear the screen")
    
    def execute(self, arg):
        os.system("cls")
        return ""