class Wumpus:
    def __init__(self, token: str) -> None:
        self.commands = {}
        self.__token = token

    def command(self, name: str) -> None:
        def decorator(func):
            self.commands[name] = func
            return func
        return decorator
    
    def run(self) -> None:
        pass