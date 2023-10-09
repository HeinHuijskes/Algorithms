import pygame

# TODO: add overrides for things such as button colour, instead of always using the same colour from parameters

class UI():
    screen = None
    buttons = []
    def __init__(self, params) -> None:
        self.params = params
        self.screen = pygame.display.set_mode((params["screen"]["width"], params["screen"]["height"]))

    def drawDot(self, position):
        dot = self.params["dots"]
        pygame.draw.circle(self.screen, dot["colour"], position, dot["size"])

    def drawButton(self, position, colour):
        left, top, width, height, = position
        pygame.draw.rect(self.screen, colour, pygame.Rect(left, top, width, height), 4)
        
    def drawMenu(self):
        scr = self.params["screen"]
        self.screen.fill(scr["bg-colour"])
        pygame.draw.rect(self.screen, "white", pygame.Rect(scr["width"]-scr["menu-width"], 0, scr["menu-width"], scr["height"]))

        # Bruteforce button
        left, top, width, height = scr["width"]-scr["menu-width"]+10, 10, scr["menu-width"]-20, 40
        pygame.draw.rect(self.screen, "black", pygame.Rect(left, top, width, height), 4)
        text = pygame.font.SysFont("Corbel", 25).render("Bruteforce", True, "black")
        self.screen.blit(text, (left+35, top+10))
        self.buttons.append({"position": (left, top, left+width, top+height), "action": "bruteforce", "active": True})

    def drawTimer(self, time):
        scr = self.params["screen"]
        x = scr["width"]-scr["menu-width"]+10
        y = 60
        pygame.draw.rect(self.screen, "white", pygame.Rect(x, y, 200, 30))
        self.screen.blit(pygame.font.SysFont('Corbel', 25).render(f'Time: {time} sec', True, "black"), (x, y))

    def drawLine(self, point1, point2, colour):
        pygame.draw.line(self.screen, colour, point1, point2, 1)
