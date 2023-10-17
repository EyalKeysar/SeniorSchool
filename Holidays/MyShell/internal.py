import os
import sys

def start(arg):
    os.system(f"start {arg}")
    return "", True

def mkdir(arg):
    try:
        os.mkdir(arg)
    except FileExistsError:
        return f"mkdir: cannot create directory '{arg}': File exists", True
    return "", True

def rename(arg):
    if(arg.count(" ") != 1):
        return "rename: invalid arguments", True
    old_name, new_name = arg.split(" ")
    try:
        os.rename(old_name, new_name)
    except FileNotFoundError:
        return f"rename: {old_name}: No such file or directory", True
    return "", True