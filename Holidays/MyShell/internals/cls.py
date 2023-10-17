import os

from .internal_command import InternalCommand

class ClsCommand(InternalCommand):

    name = "cls"
    description = "Clears the screen"

    def __init__(self, args, redirect=None):
        self.args = args
        self.redirect = redirect
    
    def execute(self, arg):
        os.system("cls")
        return ""