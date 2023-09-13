from .stdout import AbsStdout

class ScreenStdout(AbsStdout):
    def add(self, text):
        print(text, end="")