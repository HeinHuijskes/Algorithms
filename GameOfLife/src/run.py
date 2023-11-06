import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")
sys.path.append("../Algorithms/Framework/src")

from Framework.src.controller import Controller
from Framework.src.button import Button
from GameOfLifeAlgorithm import GameOfLifeAlgorithm
from gameoflifeparams import GameOfLifeParams

from time import sleep

algorithm: GameOfLifeAlgorithm

def clear(controller: Controller):
    controller.ui.log('Cleared field')

def randomFill(controller: Controller):
    algorithm.randomFillField()
    algorithm.showField(clear=True)
    controller.ui.log('Randomly filled field')

def step(controller: Controller):
    algorithm.updateField()
    algorithm.showField()
    controller.ui.log('Step')

def setCell(controller: Controller, position: tuple):
    x, y = position
    algorithm.toggleCell(x, y)
    algorithm.showField()
    controller.ui.log(f'Added cell at ({x},{y})')

def showNeighboursAmount(controller: Controller):
    algorithm.showNeighboursAmount = not algorithm.showNeighboursAmount
    algorithm.showField()

def runSteps(controller: Controller, steps=10):
    controller.ui.log(f'Running {steps} steps')
    controller.ui.drawTopText('Step: 0', 1)
    controller.startTimer()
    for i in range(steps):
        algorithm.updateField()
        if not algorithm.fast:
            sleep(0.1)
        controller.ui.drawTopText(f'Step: {i+1}', 1)
        algorithm.showField()
    controller.stopTimer()

def runManySteps(controller: Controller):
    runSteps(controller, steps=100)

def changeSpeed(controller: Controller):
    algorithm.fast = not algorithm.fast
    if algorithm.fast:
        controller.ui.log('Set algorithm to fast speed')
    else:
        controller.ui.log('Set algorithm to normal speed')

def changeFieldSize(controller: Controller, amount):
    algorithm.changeFieldSize(amount)
    algorithm.showField(clear=True)
    controller.ui.log(f'Changed field size to ({algorithm.cells_x},{algorithm.cells_y})')

def increaseFieldSize(controller: Controller):
    changeFieldSize(controller, amount=1)
def increaseFieldSizeMore(controller: Controller):
    changeFieldSize(controller, amount=10)
def decreaseFieldSize(controller: Controller):
    changeFieldSize(controller, amount=-1)
def decreaseFieldSizeMore(controller: Controller):
    changeFieldSize(controller, amount=-10)

buttons = [
    Button(label="Clear field", action=clear),
    Button(label="Random", action=randomFill),
    Button(label="s+", action=increaseFieldSize, buttonSize=1),
    Button(label="s++", action=increaseFieldSizeMore, buttonSize=1),
    Button(label="s-", action=decreaseFieldSize, buttonSize=1),
    Button(label="s--", action=decreaseFieldSizeMore, buttonSize=1),
    Button(label="Step", action=step),
    Button(label="Text", action=showNeighboursAmount),
    Button(label="Run 10", action=runSteps),
    Button(label="Run 100", action=runManySteps),
    Button(label="Change speed", action=changeSpeed),
]

controller = Controller(GameOfLifeParams(), buttons=buttons, inFieldAction=setCell)
width, height = controller.ui.settings.fieldWidth, controller.ui.settings.fieldHeight
algorithm = GameOfLifeAlgorithm(controller, width, height)

controller.run()
