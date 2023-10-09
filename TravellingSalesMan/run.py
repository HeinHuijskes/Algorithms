import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")

from Framework.console import Console
from Framework.runner import Runner
from Framework.button import Button
from TSMAlgorithm import getRandomPositions, bruteForce

from Framework.uiparams import parameters as uiparams
from tsmparams import parameters

scr = uiparams["screen"]
width, height, amount = scr["width"]-scr["menu-width"], scr["height"], parameters["dots"]["amount"]

def bruteForceAction(console: Console, button: Button):
    positions = console.objects["positions"]
    console.startTimer()
    console.runTimer = True
    solution = bruteForce(positions, console)
    console.runTimer = False
    showSolution(console.ui, solution)
    button.active = False
    console.ui.drawButton(button)

def resetDots(console: Console, button: Button):
    positions = getRandomPositions(width, height, amount)
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

runner = Runner(objects={"positions": getRandomPositions(width, height, amount)}, params=parameters, buttons=buttons)
runner.run()
