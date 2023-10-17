from .internal_command import InternalCommand

from .commands import commands_list

class HelpCommand(InternalCommand):


    def __init__(self):
        super().__init__("help", "Print this help message")

    def execute(self, arg):
        if(arg == ""):
            return "\n".join([command.name + " - " + command.description for command in commands_list])
        else:
            for command in commands_list:
                if(command.name == arg):
                    return command.description
            return "Command not found"