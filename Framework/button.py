class Button():
    def __init__(self, label, action, buttonSize=4, fontSize=25, textPadding=10) -> None:
        self.label = label
        self.action = action
        self.buttonSize = buttonSize
        self.fontSize = fontSize
        self.textPadding = textPadding

    active = False
    position = (610, 10)
    size = (180, 40)
    padding = 10
    
    borderColour = "black"
    borderSize = 2
    borderColourActive = "red"

    font = "Corbel"
    fontColour = "black"