import pygame
from threading import Thread

from ui import UI
from button import Button
from timerClass import Timer

class Console():
    ui: UI
    clock: pygame.time.Clock
    timer: Timer
    button: list[Button]
    def __init__(self, ui, parameters) -> None:
        self.ui = ui
        self.parameters = parameters
        self.objects = {}
        self.timer = Timer()
        self.clock = pygame.time.Clock()
        self.algorithmResult = None

    def getObjects(self):
        return self.objects

    def setObjects(self, objects):
        self.objects = objects
    
    def run(self):
        running = True
        pygame.init()
        pygame.display.set_caption(self.parameters.title)
        pygame.display.set_icon(pygame.image.load(self.ui.settings.icon))
        self.setScreen()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkMouseEvent(pygame.mouse.get_pos())
            if self.timer.runTimer:
                self.showTimer()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def setScreen(self):
        self.ui.drawScreen()
        for position in self.objects["positions"]:
            self.ui.drawDot(position)
    
    def startTimer(self):
        self.timer.setTime(pygame.time.get_ticks())

    def showTimer(self):
        time = (pygame.time.get_ticks()-self.timer.getTime()) // 100 / 10
        self.ui.drawTimer(time, self.timer)

    def checkMouseEvent(self, position):
        actionFound = False
        x, y = position
        for button in self.ui.buttons:
            if button.active:
                continue
            pos, size = button.position, button.size
            if x > pos[0] and x < pos[0]+size[0] and y > pos[1] and y < pos[1]+size[1]:
                actionFound = True
                break
        if actionFound:
            self.performAction(button)
        else:
            self.ui.log(f'Action not found!')

    def performAction(self, button: Button):
        button.active = True
        self.ui.drawButton(button)
        actionThread = Thread(target=button.action, args=(self, button))
        actionThread.start()

    def deactivate(self, button: Button):
        button.active = False
        self.ui.drawButton(button)
