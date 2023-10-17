import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")
sys.path.append("../Algorithms/Framework/src")

from Framework.src.controller import Controller
from Framework.src.button import Button
from Framework.src.drawable import Drawable
from WFCAlgorithm import WFCAlgorithm
from wfcparams import WFCParameters

algorithm: WFCAlgorithm
buttons: list[Button]
width: int
height: int

def drawTile(controller: Controller):
    tile = Drawable((100,100), "tile", 50, "red")
    tile.draw(controller.ui)
    controller.ui.log("Logged")

buttons = [Button(label="Draw Tile", action=drawTile)]

controller = Controller(WFCParameters(), buttons=buttons)
width, height = controller.ui.settings.fieldWidth, controller.ui.settings.fieldHeight
algorithm = WFCAlgorithm(controller)

controller.run()
