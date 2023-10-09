import pygame
from threading import Thread

from ui import UI
from TSMAlgorithm import *

class Console():
    ui: UI
    clock: pygame.time.Clock
    def __init__(self, ui, parameters) -> None:
        self.ui = ui
        self.parameters = parameters
        self.clock = pygame.time.Clock()
        self.buttons = []
        self.objects = {}
        self.timer = 0
        self.runTimer = False
        self.algorithmFinished = False

    def setObjects(self, objects):
        self.objects = objects
    
    def run(self):
        running = True
        pygame.init()
        # self.setButtons()
        self.setScreen()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkMouseEvent(pygame.mouse.get_pos())
            if self.algorithmFinished:
                self.algorithmFinished = False
                self.showSolution()
            if self.runTimer:
                self.showTimer()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    # def setButtons(self):
    #     for button in self.objects["buttons"]:
    #         self.buttons.append(button)

    def setScreen(self):
        self.ui.drawMenu()
        for position in self.objects["positions"]:
            self.ui.drawDot(position)
    
    def startTimer(self):
        self.timer = pygame.time.get_ticks()

    def showTimer(self):
        time = (pygame.time.get_ticks()-self.timer) // 100 / 10
        self.ui.drawTimer(time)

    def checkMouseEvent(self, position):
        action = ''
        x, y = position
        for button in self.ui.buttons:
            if not button["active"]:
                continue
            buttonPos = button["position"]
            if x > buttonPos[0] and x < buttonPos[2] and y > buttonPos[1] and y < buttonPos[3]:
                action = button["action"]
                break
        self.performAction(action)

    def performAction(self, action):
        if action == "bruteforce":
            # TODO: Move this to ui
            self.ui.drawButton((610, 10, 180, 40), "red")
            bruteForceThread = Thread(target=bruteForce, args=(self.objects["positions"], self))
            self.startTimer()
            self.runTimer = True
            bruteForceThread.start()
        
    def showSolution(self):
        solution = self.objects["solution"]
        # print(f'solution: {solution}, route: {route}')
        prev = solution[-1]
        for point in solution:
            self.ui.drawLine(prev, point, "red")
            prev = point
        # TODO: Move this to ui
        self.ui.drawButton((610, 10, 180, 40), "black")
