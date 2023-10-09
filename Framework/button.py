class Button():
    def __init__(self, label, action) -> None:
        self.label = label
        self.action = action

    active = False
    position = (610, 10)
    size = (180, 40)
    padding = 10
    
    borderColour = "black"
    borderSize = 4
    borderColourActive = "red"

    font = "Corbel"
    fontSize = 25
    fontColour = "black"