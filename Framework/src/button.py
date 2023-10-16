class Button():
    def __init__(self, label, action, buttonSize=4, fontSize=25) -> None:
        self.label = label
        self.action = action
        self.buttonSize = buttonSize
        self.fontSize = fontSize

    active = False
    padding = 10
    position = (padding, padding)
    size = (180, 40)
    
    borderColour = "black"
    borderSize = 2
    borderColourActive = "red"

    font = "Corbel"
    fontColour = "black"