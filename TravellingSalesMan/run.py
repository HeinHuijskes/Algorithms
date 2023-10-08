from threading import Thread, active_count
import pygame

from parameters import *
from TSMAlgorithm import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
buttons = []
positions = getRandomPositions(WIDTH-MENU_WIDTH, HEIGHT, DOT_NUM)
solution = None
threadStarted = False
bruteForceThread = None

def run():
    running = True
    drawMenu()
    for position in positions:
        drawDot(position)

    while running:
        if solution != None and threadStarted:
            bruteForceThread.join()
            threadStarted = False
            print(f'Thread joined! Active threads: {active_count()}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                checkMouseEvent(pygame.mouse.get_pos())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def drawMenu():
    screen.fill('black')
    pygame.draw.rect(screen, 'white', pygame.Rect(WIDTH-MENU_WIDTH, 0, MENU_WIDTH, HEIGHT))
    
    # Bruteforce button
    left, top, width, height = WIDTH-MENU_WIDTH+10, 10, MENU_WIDTH-20, 40
    pygame.draw.rect(screen, 'black', pygame.Rect(left, top, width, height), 4)
    text = pygame.font.SysFont('Corbel', 25).render('Bruteforce', True, 'black')
    screen.blit(text, (left+35, top+10))
    buttons.append({"position": (left, top, left+width, top+height), "action": "bruteforce", "active": True})

def checkMouseEvent(position):
    action = ''
    x, y = position
    for button in buttons:
        if not button["active"]:
            continue
        buttonPos = button["position"]
        if x > buttonPos[0] and x < buttonPos[2] and y > buttonPos[1] and y < buttonPos[3]:
            action = button["action"]
            break
    performAction(action)

def performAction(action):
    if action == "bruteforce":
        bruteForceThread = Thread(target=doBruteForce)
        threadStarted = True
        bruteForceThread.start()
        # doBruteForce()

def doBruteForce():
    solution, route = bruteForce(positions)
    # print(f'solution: {solution}, route: {route}')
    prev = solution[-1]
    for point in solution:
        pygame.draw.line(screen, "red", prev, point, 1)
        prev = point

def drawDot(position, screen=screen, color=DOT_COLOR, size=DOT_SIZE):
    pygame.draw.circle(screen, DOT_COLOR, position, DOT_SIZE)

run()