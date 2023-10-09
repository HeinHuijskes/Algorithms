import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")

from Framework.controller import Controller
from Framework.runner import Runner
from Framework.button import Button
from Framework.drawable import Drawable
from TSMAlgorithm import getRandomPositions, bruteForce

from Framework.uiSettings import UISettings
from tsmparams import TSMParameters

width, height, = UISettings.width - UISettings.menuWidth, UISettings.height
positions=getRandomPositions(width, height, TSMParameters.dots, UISettings.margin)

def bruteForceAction(controller: Controller, button: Button):
    positions = [drawable.value for drawable in controller.getDrawables()]
    controller.startTimer()
    controller.timer.toggle()
    solution = bruteForce(positions, controller)
    controller.timer.toggle()
    showSolution(controller.ui, solution)
    controller.deactivate(button)

def resetDots(controller: Controller, button: Button):
    positions = getRandomPositions(width, height, TSMParameters.dots, UISettings.margin)
    controller.setDrawables(Drawable.makeDrawables(positions, "dot"))
    controller.setScreen()
    controller.deactivate(button)

def showSolution(ui, solution):
    prev = solution[-1]
    for point in solution:
        ui.drawLine(prev, point, "red")
        prev = point

def plusOne(controller: Controller, button: Button):
    changeDots(1, controller, button)

def plusTen(controller: Controller, button: Button):
    changeDots(10, controller, button)
    
def minusOne(controller: Controller, button: Button):
    changeDots(-1, controller, button)
    
def minusTen(controller: Controller, button: Button):
    changeDots(-10, controller, button)

def changeDots(amount: int, controller: Controller, button: Button):
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
    controller.deactivate(button)

buttons = [
    Button(label="Brute force", action=bruteForceAction),
    Button(label="Reset", action=resetDots),
    Button(label="+1", action=plusOne, buttonSize=1, fontSize=20, textPadding=10),
    Button(label="+10", action=plusTen, buttonSize=1, fontSize=20, textPadding=5),
    Button(label="-10", action=minusTen, buttonSize=1, fontSize=20, textPadding=5),
    Button(label="-1", action=minusOne, buttonSize=1, fontSize=20, textPadding=10),
]

runner = Runner(Drawable.makeDrawables(positions, "dot"), parameters=TSMParameters(), buttons=buttons)
runner.run()
