import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")
sys.path.append("../Algorithms/Framework/src")

from Framework.src.controller import Controller
from Framework.src.button import Button
from WFCAlgorithm import WFCAlgorithm
from wfcparams import WFCParameters
from WFCPython.src.UIBoard import UITile, UIBoard, resetTilePositions

algorithm: WFCAlgorithm
buttons: list[Button]
board: UIBoard
width: int
height: int


def resetBoard(controller: Controller):
    board.__init__(10, 10, controller.ui)
    controller.setDrawables(board.getDrawables())
    controller.drawDrawables()

def resetTiles(controller: Controller):
    resetTilePositions(board)
    controller.setDrawables(board.getDrawables())
    controller.drawDrawables()
    controller.ui.log(f'Tilemap size set to ({board.rows},{board.columns})')

def increaseDimensions(controller: Controller, x=1, y=1):
    board.rows = board.rows + y
    board.columns = board.columns + x
    for row in board.tiles:
        for i in range(y):
            row.append(UITile())
    for i in range(x):
        board.tiles.append([UITile() for i in range(board.rows)])
    resetTiles(controller)

def decreaseDimensions(controller: Controller, x=1, y=1):
    board.rows = max(1, board.rows - y)
    board.columns = max(1, board.columns - x)
    tiles = []
    for i in range(board.columns):
        tiles.append([])
        for j in range(board.rows):
            tiles[-1].append(board.tiles[i][j])
    board.tiles = tiles
    resetTiles(controller)

def largeIncrease(controller: Controller):
    increaseDimensions(controller, x=10, y=10)
def largeDecrease(controller: Controller):
    decreaseDimensions(controller, x=10, y=10)

def increaseX(controller: Controller, amount=1):
    increaseDimensions(controller, x=amount, y=0)
def decreaseX(controller: Controller, amount=1):
    decreaseDimensions(controller, x=amount, y=0)
def largeIncreaseX(controller: Controller):
    increaseX(controller, 10)
def largeDecreaseX(controller: Controller):
    decreaseX(controller, 10)

def increaseY(controller: Controller, amount=1):
    increaseDimensions(controller, x=0, y=amount)
def decreaseY(controller: Controller, amount=1):
    decreaseDimensions(controller, x=0, y=amount)
def largeIncreaseY(controller: Controller):
    increaseY(controller, 10)
def largeDecreaseY(controller: Controller):
    decreaseY(controller, 10)

sizeButtons = [
    Button(label="s+", action=increaseDimensions, buttonSize=1),
    Button(label="s++", action=largeIncrease, buttonSize=1),
    Button(label="s--", action=largeDecrease, buttonSize=1),
    Button(label="s-", action=increaseDimensions, buttonSize=1),
    Button(label="y+", action=increaseY, buttonSize=1),
    Button(label="y++", action=largeIncreaseY, buttonSize=1),
    Button(label="y--", action=largeDecreaseY, buttonSize=1),
    Button(label="y-", action=decreaseY, buttonSize=1),
    Button(label="x+", action=increaseX, buttonSize=1),
    Button(label="x++", action=largeIncreaseX, buttonSize=1),
    Button(label="x--", action=largeDecreaseX, buttonSize=1),
    Button(label="x-", action=decreaseX, buttonSize=1),
]

buttons = [
    Button(label="Reset", action=resetBoard),
] + sizeButtons

controller = Controller(WFCParameters(), buttons=buttons)
width, height = controller.ui.settings.fieldWidth, controller.ui.settings.fieldHeight
algorithm = WFCAlgorithm(controller)
board = UIBoard(10, 10, controller.ui)
controller.setDrawables(board.getDrawables())

controller.run()
