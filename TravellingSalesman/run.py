import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")

from Framework.console import Console
from Framework.runner import Runner
from Framework.button import Button
from TSMAlgorithm import getRandomPositions, bruteForce

from Framework.uiSettings import UISettings
from tsmparams import TSMParameters

width, height, = UISettings.width - UISettings.menuWidth, UISettings.height
objects={"positions": getRandomPositions(width, height, TSMParameters.dots, UISettings.margin)}

def bruteForceAction(console: Console, button: Button):
    positions = console.objects["positions"]
    console.startTimer()
    console.timer.toggle()
    solution = bruteForce(positions, console)
    console.timer.toggle()
    showSolution(console.ui, solution)
    console.deactivate(button)

def resetDots(console: Console, button: Button):
    positions = getRandomPositions(width, height, TSMParameters.dots, UISettings.margin)
    objects = console.getObjects()
    objects["positions"] = positions
    console.setObjects(objects)
    console.setScreen()
    console.deactivate(button)

def showSolution(ui, solution):
    prev = solution[-1]
    for point in solution:
        ui.drawLine(prev, point, "red")
        prev = point

def plusOne(console: Console, button: Button):
    changeDots(1, console, button)

def plusTen(console: Console, button: Button):
    changeDots(10, console, button)
    
def minusOne(console: Console, button: Button):
    changeDots(-1, console, button)
    
def minusTen(console: Console, button: Button):
    changeDots(-10, console, button)

def changeDots(amount: int, console: Console, button: Button):
    objects = console.getObjects()
    positions = objects["positions"]
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
    
    objects["positions"] = positions
    console.setObjects(objects)
    console.setScreen()
    added = abs(len(positions) - added)
    if amount > 0:
        console.ui.log(f'Added {added} dots')
    else: 
        console.ui.log(f'Removed {added} dots')
    console.deactivate(button)

buttons = [
    Button(label="Brute force", action=bruteForceAction),
    Button(label="Reset", action=resetDots),
    Button(label="+1", action=plusOne, buttonSize=1, fontSize=20, textPadding=10),
    Button(label="+10", action=plusTen, buttonSize=1, fontSize=20, textPadding=5),
    Button(label="-10", action=minusTen, buttonSize=1, fontSize=20, textPadding=5),
    Button(label="-1", action=minusOne, buttonSize=1, fontSize=20, textPadding=10),
]

runner = Runner(objects, parameters=TSMParameters(), buttons=buttons)
runner.run()
