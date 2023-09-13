import sys
import os

from .internal_command import AbsInternalCommand


class CommandLs(AbsInternalCommand):
    """
    Command ls.
    """
    def execute(self):
        """
        List files in directory.
        :return: None
        """
        if(len(self.args) == 1):
            oput = os.listdir(sys.path[0])
        elif(len(self.args) == 2):
            oput = os.listdir(self.args[1])
        else:
            oput = ["ls: too many arguments"]
        
        for i in oput:
            self.stdout.add(i + "   ")
        self.stdout.add("\n")
        
        
        