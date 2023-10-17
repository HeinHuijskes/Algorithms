import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")
sys.path.append("../Algorithms/Framework/src")

from Framework.src.controller import Controller
from Framework.src.button import Button
from Framework.src.drawable import Drawable
from EXAlgorithm import EXAlgorithm
from exparams import ExampleParameters

algorithm: EXAlgorithm
buttons: list[Button]
width: int
height: int

def logAction(controller: Controller):
    controller.ui.log("Logged")

def inFieldAction(controller: Controller, position: tuple):
    drawables = controller.getDrawables()
    dot = Drawable(position, "dot")
    drawables.append(dot)
    controller.setDrawables(drawables)
    controller.ui.drawObject(dot)
    controller.ui.log(f'Added dot at {position}')
    controller.ui.drawTopText(f'{len(controller.getDrawables())} Dots', 0)


buttons = [Button(label="Log Test", action=logAction)]

controller = Controller(ExampleParameters(), buttons=buttons, inFieldAction=inFieldAction)
width, height = controller.ui.settings.fieldWidth, controller.ui.settings.fieldHeight
algorithm = EXAlgorithm(controller)

controller.run()
