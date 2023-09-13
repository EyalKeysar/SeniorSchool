import os
import sys
import art

from std.screen import ScreenStdout

from internalcommands.ls_command import CommandLs
from internalcommands.cls_command import CommandCls

INTERNAL_COMMANDS_CONFIGURE = {
    "ls": CommandLs,
    "dir": CommandLs,
    "cls": CommandCls
}

def main():
    print("Welcome to Keysar Shell!\n" + art.text2art("KEYSAR\nSHELL"))
    while True:
        print(sys.path[0] + ">", end="")
        inp = input()
        args = inp.split(" ")
        
        out = check_redirection(args)
        if out:
            args.remove(">")
            args.remove(out)
            stdout = open(out, "w")
        else:
            stdout = ScreenStdout()
        
        if args[0] == "exit":
            break
        elif args[0] in INTERNAL_COMMANDS_CONFIGURE:
            INTERNAL_COMMANDS_CONFIGURE[args[0]](args, stdout=stdout).execute()

def check_redirection(args):
    """
    Check if there is redirection.
    :param args: arguments
    :return: tuple of (stdout, stderr)
    """
    stdout = None
    if ">" in args:
        stdout = args[args.index(">") + 1]
    return stdout

if __name__ == "__main__":
    main()