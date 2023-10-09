import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")

from Framework.console import Console
from Framework.runner import Runner
from TSMAlgorithm import getRandomPositions, bruteForce

from Framework.uiparams import parameters as uiparams
from tsmparams import parameters

scr = uiparams["screen"]
positions = getRandomPositions(scr["width"]-scr["menu-width"], scr["height"], parameters["dots"]["amount"])

def bruteForceAction(console: Console, button):
    console.startTimer()
    console.runTimer = True
    solution = bruteForce(positions, console)
    console.runTimer = False
    showSolution(console.ui, solution)
    button["active"] = False
    console.ui.drawButton(button)

def showSolution(ui, solution):
    prev = solution[-1]
    for point in solution:
        ui.drawLine(prev, point, "red")
        prev = point

buttons = [
    {
        "action": bruteForceAction,
        "active": False,
        "label": "Brute force",
    },
]

runner = Runner(objects={"positions": positions}, params=parameters, buttons=buttons)
runner.run()
