from .internal_command import InternalCommand

from .commands import commands_list
from .helpers import handle_stdout

class HelpCommand(InternalCommand):

    name = "help"
    description = "Print this help message"

    def __init__(self, args, redirect=None):
        self.args = args
        self.redirect = redirect

    def execute(self):

        if("-a" in self.args): # Print all commands and their descriptions (flag -a)
            stdout = "\n".join([command.name + ": " + command.description for command in commands_list])
            handle_stdout(self.redirect, stdout)

        elif len(self.args) > 0: # Print the description of the given commands
            stdout = ""
            for arg in self.args:
                for command in commands_list:
                    if command.name.casefold() == arg.casefold():
                        stdout += command.name + ": " + command.description + "\n"
            if(stdout == ""):
                handle_stdout(self.redirect, f"help: {self.args[0]}: No command matches this name")
            else:
                handle_stdout(self.redirect, stdout)

        else: # Print the name of all commands (default)
            stdout = "\n".join([command.name for command in commands_list if command.name != "help"])
            handle_stdout(self.redirect, stdout)