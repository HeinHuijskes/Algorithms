import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")

from Framework.controller import Controller
from Framework.ui import UI
from Framework.button import Button
from Framework.drawable import Drawable
from TSMAlgorithm import TSMAlgorithm, getRandomPositions, getRouteLength

from Framework.uiSettings import UISettings
from tsmparams import TSMParameters

algorithm: TSMAlgorithm
buttons: list[Button]
width: int
height: int

def bruteForceAction(controller: Controller, button: Button):
    positions = [drawable.value for drawable in controller.getDrawables()]
    controller.startTimer()
    controller.timer.toggle()
    solution = algorithm.bruteForce(positions)
    controller.timer.toggle()
    showSolution(controller.ui, solution)
    controller.deactivate(button)

def resetDotsAction(controller: Controller, button: Button):
    positions = getRandomPositions(width, height, TSMParameters.dots, UISettings.margin)
    controller.setDrawables(Drawable.makeDrawables(positions, "dot"))
    controller.setScreen()
    controller.deactivate(button)

def toggleParallelAction(controller: Controller, button: Button):
    controller.parameters.parallel = not controller.parameters.parallel
    if controller.parameters.parallel:
        controller.ui.log("Parallel turned ON")
    else:
        controller.ui.log("Parallel turned OFF")
    controller.deactivate(button)

def plusOne(controller: Controller, button: Button):
    changeDotsAction(1, controller, button)

def plusTen(controller: Controller, button: Button):
    changeDotsAction(10, controller, button)
    
def minusOne(controller: Controller, button: Button):
    changeDotsAction(-1, controller, button)
    
def minusTen(controller: Controller, button: Button):
    changeDotsAction(-10, controller, button)

def changeDotsAction(amount: int, controller: Controller, button: Button):
    positions = Drawable.unMakeDrawables(controller.getDrawables())
    added = len(positions)
    
    if amount > 0:
        newPositions = getRandomPositions(width, height, amount, UISettings.margin)
        positions = positions + newPositions
    else:
        for i in range(-amount):
            if len(positions) > 0:
                positions = positions[1:]
            else:
                break

    controller.setDrawables(Drawable.makeDrawables(positions, "dot"))
    controller.setScreen()
    added = abs(len(positions) - added)
    if amount > 0:
        controller.ui.log(f'Added {added} dots')
    else: 
        controller.ui.log(f'Removed {added} dots')
    controller.ui.drawTopText(f'{len(controller.getDrawables())} Dots', 1)
    controller.deactivate(button)

def addDot(controller: Controller, position: tuple):
    drawables = controller.getDrawables()
    drawables.append(Drawable.makeDrawable(position, "dot"))
    controller.setDrawables(drawables)
    controller.setScreen()
    controller.ui.log(f'Added dot at {position}')
    controller.ui.drawTopText(f'{len(controller.getDrawables())} Dots', 1)

def showSolution(ui: UI, solution: list[tuple]):
    if len(solution) < 2:
        return
    ui.clearOutputScreen()
    prev = solution[-1]
    for point in solution:
        ui.drawLine(prev, point, "red")
        prev = point
    for point in solution:
        ui.drawDot(point)
    controller.ui.drawTopText(f'Length: {int(getRouteLength([i for i in range(len(solution))], solution))}', 2)

# Initialize everything
buttons = [
    Button(label="Brute force", action=bruteForceAction),
    Button(label="Reset", action=resetDotsAction),
    Button(label="+1", action=plusOne, buttonSize=1, fontSize=20),
    Button(label="+10", action=plusTen, buttonSize=1, fontSize=20, textPadding=5),
    Button(label="-10", action=minusTen, buttonSize=1, fontSize=20, textPadding=5),
    Button(label="-1", action=minusOne, buttonSize=1, fontSize=20),
    Button(label="Parallel", action=toggleParallelAction)
]

width, height, = UISettings.width - UISettings.menuWidth, UISettings.height
positions=getRandomPositions(width, height, TSMParameters.dots, UISettings.margin)

controller = Controller(TSMParameters(), ui=UI(showSolution=showSolution), 
                        drawables=Drawable.makeDrawables(positions, "dot"), buttons=buttons, inFieldAction=addDot)
algorithm = TSMAlgorithm(controller)

controller.run()
