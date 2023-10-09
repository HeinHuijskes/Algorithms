import pygame

from uiparams import parameters

# TODO: add overrides for things such as button colour, instead of always using the same colour from parameters

class UI():
    screen = None
    buttons = []
    def __init__(self, logging=True) -> None:
        # TODO: Add setting overrides
        self.screen = pygame.display.set_mode((parameters["screen"]["width"], parameters["screen"]["height"]))
        self.uiParams = parameters
        self.logging=logging
    
    def addButton(self, button):
        # TODO: Add setting overrides
        settings = self.uiParams["buttons"]
        button["settings"] = settings
        for b in self.buttons:
            button["settings"]["position"][1] += settings["padding"] + settings["size"][1]
        self.buttons.append(button)

    def drawDot(self, position):
        dot = self.uiParams["dots"]
        pygame.draw.circle(self.screen, dot["colour"], position, dot["size"])

    def drawButtonOutline(self, button, colour):
        pos, size = button["settings"]["position"], button["settings"]["size"]
        pygame.draw.rect(self.screen, colour, pygame.Rect(pos[0], pos[1], size[0], size[1]), button["settings"]["border"]["size"])
        
    def drawButton(self, button):
        if button["active"]:
            colour = button["settings"]["border"]["active-colour"]
        else:
            colour = button["settings"]["border"]["colour"]
        settings = button["settings"]
        pos, text = settings["position"], settings["text"]
        self.drawButtonOutline(button, colour)
        buttonText = pygame.font.SysFont(text["font"], text["fontsize"]).render(button["label"], True, text["colour"])
        # TODO: Find a way to center text
        self.screen.blit(buttonText, (pos[0]+10, pos[1]+10))

    def drawMenu(self):
        scr = self.uiParams["screen"]
        self.screen.fill(scr["bg-colour"])
        pygame.draw.rect(self.screen, "white", pygame.Rect(scr["width"]-scr["menu-width"], 0, scr["menu-width"], scr["height"]))

        # Draw buttons
        for button in self.buttons:
            self.drawButton(button)

    def drawTimer(self, time):
        scr = self.uiParams["screen"]
        x = scr["width"]-scr["menu-width"]+10
        y = 60
        pygame.draw.rect(self.screen, "white", pygame.Rect(x, y, 200, 30))
        self.screen.blit(pygame.font.SysFont('Corbel', 25).render(f'Time: {time} sec', True, "black"), (x, y))

    def drawLine(self, point1, point2, colour):
        pygame.draw.line(self.screen, colour, point1, point2, 1)

    def log(self, string):
        if self.logging:
            print(string)
