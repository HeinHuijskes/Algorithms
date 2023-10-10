import pygame

from button import Button
from timerClass import Timer
from uiSettings import UISettings
from drawable import Drawable

class UI():
    screen = None
    buttons: list[Button] = []
    def __init__(self, logging=True, settings=UISettings(), showSolution=None) -> None:
        self.screen = pygame.display.set_mode((settings.width, settings.height))
        self.logging = logging
        self.settings = settings
        self.showSolution = showSolution
    
    def setButtons(self, buttons: list[Button]):
        skipSize = Button.size[1] + Button.padding
        smallSize = Button.size[0]//4
        space = 4
        position = Button.position
        for button in buttons:
            # If there is not enough space for this button, skip to the next row
            if button.buttonSize > space:
                space = 4
                position = (Button.position[0], position[1] + skipSize)

            space -= button.buttonSize
            # Set the definitive position of this button
            button.position = position
            # Calculate and set the correct dimensions
            buttonWidth = Button.size[0] - (4-button.buttonSize)*(smallSize) - Button.padding // 2
            button.size = (buttonWidth, button.size[1])
            # Move the current position sideways by the size of the button and a margin
            position = (position[0] + button.buttonSize * smallSize, position[1])
        self.buttons = buttons
    
    def drawObject(self, drawable: Drawable):
        if drawable.drawType == "dot":
            self.drawDot(drawable.value)
        else:
            self.log(f'Unrecognized drawtype "{drawable.drawType}"')

    def drawDot(self, position):
        pygame.draw.circle(self.screen, self.settings.dotColour, position, self.settings.dotSize)

    def drawButtonOutline(self, button: Button, colour):
        pos, size = button.position, button.size
        pygame.draw.rect(self.screen, colour, pygame.Rect(pos[0], pos[1], size[0], size[1]), button.borderSize)

    def drawTopText(self, textString, x):
        rectangle = pygame.Rect(self.settings.width-x-self.settings.menuWidth, 0, x, 50)
        pygame.draw.rect(self.screen, self.settings.bgColour, rectangle)
        font = pygame.font.SysFont(self.settings.font, self.settings.fontSize)
        text = font.render(textString, True, self.settings.fontColour)
        text_rect = text.get_rect(center=(self.settings.width-x//2-self.settings.menuWidth, 25))
        self.screen.blit(text, text_rect)
        
    def drawButton(self, button: Button):
        if button.active:
            colour = button.borderColourActive
        else:
            colour = button.borderColour
        self.drawButtonOutline(button, colour)
        text = pygame.font.SysFont(button.font, button.fontSize).render(button.label, True, button.fontColour)
        text_rect = text.get_rect(center=(button.position[0]+button.size[0]//2, button.position[1]+button.size[1]//2))
        self.screen.blit(text, text_rect)

    def clearOutputScreen(self):
        x, y, width, height = 0, 50, self.settings.width - self.settings.menuWidth, self.settings.height - 50
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

    def drawSolution(self, solution):
        if self.showSolution != None:
            self.showSolution(self, solution)
        else:
            self.log(f'No "showSolution" method found, cannot draw solution')

    def log(self, string):
        if self.logging:
            print(string)
