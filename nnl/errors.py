class NNLException(Exception):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(message, *args)


class UnclosedStringException(NNLException):
    def __init__(self, *args: object) -> None:
        super().__init__("Unclosed string", *args)
    