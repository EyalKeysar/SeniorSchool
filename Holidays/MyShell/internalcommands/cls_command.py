import sys
import os

from .internal_command import AbsInternalCommand

class CommandCls(AbsInternalCommand):
    """
    Command cls.
    """
    def execute(self):
        """
        Clear screen.
        :return: None
        """
        os.system("cls")