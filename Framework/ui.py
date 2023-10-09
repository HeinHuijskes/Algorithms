import pygame

from button import Button
from timerClass import Timer
from uiSettings import UISettings

class UI():
    screen = None
    buttons: list[Button] = []
    def __init__(self, logging=True, settings=UISettings()) -> None:
        self.screen = pygame.display.set_mode((settings.width, settings.height))
        self.logging = logging
        self.settings = settings
    
    def addButton(self, button: Button):
        for b in self.buttons:
            button.position = (button.position[0], button.position[1] + button.size[1] + button.padding)
        self.buttons.append(button)

    def drawDot(self, position):
        pygame.draw.circle(self.screen, self.settings.dotColour, position, self.settings.dotSize)

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
        x, y, width, height = 0, 0, self.settings.width - self.settings.menuWidth, self.settings.height
        pygame.draw.rect(self.screen, self.settings.bgColour, pygame.Rect(x, y, width, height))

    def drawScreen(self):
        self.screen.fill(self.settings.bgColour)
        self.clearOutputScreen()
        # Draw menu background
        x, y, width, height = self.settings.width - self.settings.menuWidth, 0, self.settings.menuWidth, self.settings.height
        pygame.draw.rect(self.screen, self.settings.menuColour, pygame.Rect(x, y, width, height))

        # Draw buttons
        for button in self.buttons:
            self.drawButton(button)

    def drawTimer(self, time, timer: Timer):
        x, y = timer.position 
        width, height = timer.size
        pygame.draw.rect(self.screen, timer.colour, pygame.Rect(x, y, width, height))
        text = pygame.font.SysFont(timer.font, timer.fontSize).render(f'Time: {time} sec', True, timer.textColour)
        self.screen.blit(text, (x, y))

    def drawLine(self, point1, point2, colour):
        pygame.draw.line(self.screen, colour, point1, point2, 1)

    def log(self, string):
        if self.logging:
            print(string)
