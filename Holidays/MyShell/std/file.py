from .stdout import AbsStdout

class FileStdout(AbsStdout):
    def __init__(self):
        super().__init__()
        