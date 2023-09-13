

class AbsInternalCommand(object):
    """
    Abstract class for internal commands.
    """

    def __init__(self, args, stdin=None, stdout=None, stderr=None):
        """
        Constructor.
        :param args: arguments of command
        """
        self.args = args
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

    def execute(self):
        """
        Execute command.
        :return: None
        """
        raise NotImplementedError