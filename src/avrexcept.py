class AVRException(object):
    def __init__(self):
        self.BreakException = BreakException
        self.UnknownException = UnknownOpcodeException

class BreakException(AVRException):
    pass

class UnknownOpcodeException(AVRException):
    pass
