class Timer():
    def __init__(self) -> None:
        pass

    runTimer = False
    time = 0

    def toggle(self):
        self.runTimer = not self.runTimer
    
    def setTime(self, time):
        self.time = time
    
    def getTime(self):
        return self.time

    position = (10, 10)
    colour = "black"
    textColour = "white"
    font = "Corbel"
    fontSize = 25
    size = (200, 30)
