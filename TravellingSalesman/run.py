import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")

from Framework.console import Console
from Framework.runner import Runner
from Framework.button import Button
from TSMAlgorithm import getRandomPositions, bruteForce

from Framework.uiSettings import UISettings
from tsmparams import parameters

width, height, = UISettings.width - UISettings.menuWidth, UISettings.height, 
margin, amount = UISettings.margin, parameters["dots"]["amount"]

def bruteForceAction(console: Console, button: Button):
    positions = console.objects["positions"]
    console.startTimer()
    console.timer.toggle()
    solution = bruteForce(positions, console)
    console.timer.toggle()
    showSolution(console.ui, solution)
    button.active = False
    console.ui.drawButton(button)

def resetDots(console: Console, button: Button):
    positions = getRandomPositions(width, height, amount, margin)
    objects = console.getObjects()
    objects["positions"] = positions
    console.setObjects(objects)
    console.setScreen()
    button.active = False
    console.ui.drawButton(button)

def showSolution(ui, solution):
    prev = solution[-1]
    for point in solution:
        ui.drawLine(prev, point, "red")
        prev = point

buttons = [
    Button(label="Brute force", action=bruteForceAction),
    Button(label="Reset", action=resetDots)
]

runner = Runner(objects={"positions": getRandomPositions(width, height, amount, margin)}, params=parameters, buttons=buttons)
runner.run()
