import pygame

from button import Button
from uiparams import parameters

# TODO: add overrides for things such as button colour, instead of always using the same colour from parameters

class UI():
    screen = None
    buttons: list[Button] = []
    def __init__(self, logging=True) -> None:
        # TODO: Add setting overrides
        self.screen = pygame.display.set_mode((parameters["screen"]["width"], parameters["screen"]["height"]))
        self.uiparams = parameters
        self.logging=logging
    
    def addButton(self, button: Button):
        # TODO: Add setting overrides
        for b in self.buttons:
            pos = button.position
            button.position = (pos[0], pos[1] + button.size[1] + button.padding)
        self.buttons.append(button)

    def drawDot(self, position):
        dot = self.uiparams["dots"]
        pygame.draw.circle(self.screen, dot["colour"], position, dot["size"])

    def drawButtonOutline(self, button: Button, colour):
        pos, size = button.position, button.size
        pygame.draw.rect(self.screen, colour, pygame.Rect(pos[0], pos[1], size[0], size[1]), button.borderSize)
        
    def drawButton(self, button: Button):
        if button.active:
            colour = button.borderColourActive
        else:
            colour = button.borderColour
        self.drawButtonOutline(button, colour)
        text = pygame.font.SysFont(button.font, button.fontSize).render(button.label, True, button.fontColour)
        # TODO: Find a way to center text
        self.screen.blit(text, (button.position[0]+10, button.position[1]+10))

    def clearOutputScreen(self):
        scr = self.uiparams["screen"]
        x, y, width, height = 0, 0, scr["width"]-scr["menu-width"], scr["height"]
        pygame.draw.rect(self.screen, scr["bg-colour"], pygame.Rect(x, y, width, height))

    def drawScreen(self):
        scr = self.uiparams["screen"]
        self.screen.fill(scr["bg-colour"])
        self.clearOutputScreen()
        pygame.draw.rect(self.screen, "white", pygame.Rect(scr["width"]-scr["menu-width"], 0, scr["menu-width"], scr["height"]))

        # Draw buttons
        for button in self.buttons:
            self.drawButton(button)

    def drawTimer(self, time):
        scr = self.uiparams["screen"]
        x = scr["width"] - scr["menu-width"]+10
        y = scr["height"] - 30
        pygame.draw.rect(self.screen, "white", pygame.Rect(x, y, 200, 30))
        self.screen.blit(pygame.font.SysFont('Corbel', 25).render(f'Time: {time} sec', True, "black"), (x, y))

    def drawLine(self, point1, point2, colour):
        pygame.draw.line(self.screen, colour, point1, point2, 1)

    def log(self, string):
        if self.logging:
            print(string)
