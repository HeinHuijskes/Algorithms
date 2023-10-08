from threading import Thread, active_count
import pygame

from parameters import *
from TSMAlgorithm import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
buttons = []
positions = getRandomPositions(WIDTH-MENU_WIDTH, HEIGHT, DOT_NUM)
solution = [None]
threadStarted = [False]
bruteForceThread = None
timer = []

def run():
    running = True
    drawMenu()
    for position in positions:
        drawDot(position)

    while running:
        if solution[0] != None and threadStarted[0]:
            # bruteForceThread.join()
            threadStarted[0] = False
            print(f'Thread joined! Active threads: {active_count()}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                checkMouseEvent(pygame.mouse.get_pos())
        
        if threadStarted[0]:
            x = WIDTH-MENU_WIDTH+10
            y = 60
            pygame.draw.rect(screen, "white", pygame.Rect(x, y, 200, 30))
            screen.blit(pygame.font.SysFont('Corbel', 25).render(f'Time: {(pygame.time.get_ticks()-timer[0]) // 100 / 10} sec', True, "black"), (x, y))

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
        drawButton(WIDTH-MENU_WIDTH+10, 10, MENU_WIDTH-20, 40, "red")
        bruteForceThread = Thread(target=doBruteForce)
        threadStarted[0] = True
        timer.append(pygame.time.get_ticks())
        bruteForceThread.start()
        # doBruteForce()

def doBruteForce():
    solve, route = bruteForce(positions)
    solution[0] = solve
    # print(f'solution: {solution}, route: {route}')
    prev = solve[-1]
    for point in solve:
        pygame.draw.line(screen, "red", prev, point, 1)
        prev = point
    drawButton(WIDTH-MENU_WIDTH+10, 10, MENU_WIDTH-20, 40, "black")

def drawDot(position, screen=screen, color=DOT_COLOR, size=DOT_SIZE):
    pygame.draw.circle(screen, DOT_COLOR, position, DOT_SIZE)

def drawButton(left, top, width, height, colour):
    pygame.draw.rect(screen, colour, pygame.Rect(left, top, width, height), 4)

run()