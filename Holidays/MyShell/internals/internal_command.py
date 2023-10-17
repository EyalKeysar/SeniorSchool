

class InternalCommand():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def execute(self, arg):
        raise NotImplementedError("execute method not implemented")