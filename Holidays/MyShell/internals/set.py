import os
from .internal_command import InternalCommand

class SetCommand(InternalCommand):
    def __init__(self):
        super().__init__("set", "Set environment variable, if no arguments are given, print all environment variables")

    def execute(self, arg):
        if(arg.count("=") != 1):
            return "\n".join([env for env in os.environ if env.startswith(arg)])
        env_name, env_value = arg.split("=")
        os.environ[env_name] = env_value
        return ""
