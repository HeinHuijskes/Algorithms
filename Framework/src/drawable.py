import pygame

class Drawable():
    def __init__(self, position, drawType="dot", size=None, value=None) -> None:
        self.position = position
        self.drawType = drawType
        self.size = size
        self.value = value

    def draw(self, ui):
        if self.drawType == "dot":
            ui.drawDot(self.position)
        elif self.drawType == "tile":
            ui.drawTile(self.position, self.size, self.value)
        elif self.drawType == "text":
            ui.drawText(self.position, self.size, self.value)
        else:
            self.log(f'Unrecognized drawtype "{self.drawType}"', warning=True)