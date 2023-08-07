from .text import Text

class Response:
    def __init__(self, type: int) -> None:
        self.type = type
    

class Pong(Response):
    def __init__(self) -> None:
        super().__init__(1)

    def __iter__(self) -> dict:
        return iter({"type": 1}.items())



class Answer(Response, Text):
    def __init__(self) -> None:
        Response.__init__(4)
        Text.__init__()


class Loading(Response):
    def __init__(self) -> None:
        super().__init__(5)


class Modal(Response):
    def __init__(self) -> None:
        super().__init__(9)