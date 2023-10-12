class UISettings():
    def __init__(self, GUILogging=True) -> None:
        self.GUILogging = GUILogging

    width = 800
    height = 500
    menuWidth = 200
    margin = 50
    topbarWidth = 150

    fieldWidth = width - menuWidth
    fieldHeight = height - margin

    icon = "./Framework/hexagon.png"
    bgColour = "black"
    menuColour = "white"

    dotSize = 4
    dotColour = "white"

    font="Calibri"
    fontSize = 22
    fontColour = "white"

    logFont = "Consolas"
    logAmount = 11
    logFontSize = 10
    logFontColour = "black"
    logSize = (menuWidth, logAmount * logFontSize)
    logMargin = 10
