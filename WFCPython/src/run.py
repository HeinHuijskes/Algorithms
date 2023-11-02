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

def increaseDimensions(controller: Controller, rows=1, columns=1):
    board.rows = board.rows + columns
    board.columns = board.columns + rows
    for row in board.tiles:
        for i in range(columns):
            row.append(UITile())
    for i in range(rows):
        board.tiles.append([UITile() for i in range(board.rows)])
    resetTiles(controller)

def decreaseDimensions(controller: Controller, columns=1, rows=1):
    board.rows = max(1, board.rows - columns)
    board.columns = max(1, board.columns - rows)
    tiles = []
    for i in range(board.columns):
        tiles.append([])
        for j in range(board.rows):
            tiles[-1].append(board.tiles[i][j])
    board.tiles = tiles
    resetTiles(controller)

def largeIncrease(controller: Controller):
    increaseDimensions(controller, rows=10, columns=10)
def largeDecrease(controller: Controller):
    decreaseDimensions(controller, rows=10, columns=10)

def increaseX(controller: Controller, amount=1):
    increaseDimensions(controller, columns=amount, rows=0)
def decreaseX(controller: Controller, amount=1):
    decreaseDimensions(controller, columns=amount, rows=0)
def largeIncreaseX(controller: Controller):
    increaseX(controller, 10)
def largeDecreaseX(controller: Controller):
    decreaseX(controller, 10)

def increaseY(controller: Controller, amount=1):
    increaseDimensions(controller, columns=0, rows=amount)
def decreaseY(controller: Controller, amount=1):
    decreaseDimensions(controller, columns=0, rows=amount)
def largeIncreaseY(controller: Controller):
    increaseY(controller, 10)
def largeDecreaseY(controller: Controller):
    decreaseY(controller, 10)

sizeButtons = [
    Button(label="s+", action=increaseDimensions, buttonSize=1),
    Button(label="s++", action=largeIncrease, buttonSize=1),
    Button(label="s--", action=largeDecrease, buttonSize=1),
    Button(label="s-", action=decreaseDimensions, buttonSize=1),
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
