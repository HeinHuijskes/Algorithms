import pygame

from button import Button
from timerClass import Timer
from uiSettings import UISettings
from drawable import Drawable

class UI():
    screen = None
    buttons: list[Button] = []
    logs = []
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

    def drawTopText(self, textString, slot):
        if slot >= self.settings.topbarSlots:
            slot = self.settings.topbarSlots-1
        # The top bar is divided into 5 slots for text. These can extend beyond their space if necessary
        width, height, slots = self.settings.fieldWidth, self.settings.margin, self.settings.topbarSlots
        position = (width / slots * slot, 0)
        size = (width / slots, height)
        rectangle = pygame.Rect(position[0], position[1], size[0], size[1])
        pygame.draw.rect(self.screen, self.settings.bgColour, rectangle)
        font = pygame.font.SysFont(self.settings.font, self.settings.fontSize)
        text = font.render(textString, True, self.settings.fontColour)
        text_rect = text.get_rect(center=(position[0]+size[0]/2, position[1]+size[1]/2))
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
        x, y, width, height = 0, self.settings.margin, self.settings.fieldWidth, self.settings.fieldHeight
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

    def drawLine(self, point1, point2, colour):
        pygame.draw.line(self.screen, colour, point1, point2, 1)

    def drawSolution(self, solution):
        if self.showSolution != None:
            self.showSolution(self, solution)
        else:
            self.log(f'No "showSolution" method found, cannot draw solution')
    
    def GUILog(self):
        width, height = self.settings.logSize
        margin = self.settings.logMargin
        x, y = self.settings.fieldWidth, self.settings.height - height
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, self.settings.menuColour, rectangle)

        font = pygame.font.SysFont(self.settings.logFont, self.settings.logFontSize)
        for i, log in enumerate(reversed(self.logs[-7:])):
            text = font.render(log, True, self.settings.logFontColour)
            # text_rect = text.get_rect(center=(x+width/2, y+height/2))
            self.screen.blit(text, (x+margin, y + i*(margin)))

    def cutLog(self, string):
        length = 0
        words = string.split(' ')
        print(words)
        logs = []
        log = ""
        for word in words:
            print(f'Length: {len(word)} + {length} = {len(word) + length}')
            if len(word) + length < 32:
                log += word + ' '
                length += len(word) + 1
            else:
                if length == 0:
                    logs.append(word)
                else:
                    print(f'log: {log}')
                    logs.append(log)
                    log = word + ' '
                    length = len(word) + 1
        if len(log) > 0:
            logs.append(log)
        print(logs)
        return logs

    def log(self, string):
        logs = self.cutLog('> ' + string)
        for log in reversed(logs):
            self.logs.append(log)
        if self.logging:
            if self.settings.GUILogging:
                self.GUILog()
            else:
                print(string)
