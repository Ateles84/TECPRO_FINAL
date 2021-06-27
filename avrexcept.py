class AVRException(object):
    def __init__(self):
        self.BreakException = BreakException
        self.UnknownException = UnknownOpcodeException
        self.OutOfMemException = OutOfMemException

class BreakException(AVRException):
    pass

class UnknownOpcodeException(AVRException):
    pass
