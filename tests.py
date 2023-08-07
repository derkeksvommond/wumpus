from wumpus import *

discord = Wumpus("sehrcoolestoken")

@discord.command("/hallo")
def hallo():    
    return Answer("Hallo :)")

if __name__ == "__main__":
    Channel(123456789).send(Text("Ich bin jetzt aktiv."))