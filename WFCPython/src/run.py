import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")
sys.path.append("../Algorithms/Framework/src")

from Framework.src.controller import Controller
from Framework.src.button import Button
from WFCAlgorithm import WFCAlgorithm
from wfcparams import WFCParameters
from WFCPython.src.UIBoard import UITile, UIBoard, resetTilePositions
from Map import Map

start_rows = 25
start_columns = 40
allowedFails = 10

algorithm: WFCAlgorithm
buttons: list[Button]
board: UIBoard
cellMap: Map
width: int
height: int


def resetBoard(controller: Controller):
    board.__init__(10, 10, controller.ui)
    controller.setDrawables(board.getDrawables())
    controller.redrawDrawables()

def runAlgorithm(controller: Controller):
    controller.startTimer()
    cellMap = Map(board.columns, board.rows)
    fails = 0
    drawMap(cellMap)
    while not cellMap.is_solved() and fails < allowedFails:
        cell = cellMap.find_lowest_entropy_cell()
        cellMap.collapse(cell)
        if cellMap.hasContradiction:
            cellMap.reset()
            controller.ui.log("Failed!")
            fails += 1
        drawMap(cellMap, cellMap.hasContradiction)
    controller.stopTimer()
    if not cellMap.is_solved():
        controller.ui.log("Failed to solve map")
    else:
        controller.ui.log("Solved!")

def drawMap(cellMap: Map, redraw=True):
    tiles = []
    for row in cellMap.cells:
        tiles.append([])
        for cell in row:
            if cell.state != None:
                tiles[-1].append(UITile(colour=cell.state.colour))
            else:
                tiles[-1].append(UITile(colour="black"))
    board.tiles = tiles
    resetTilePositions(board)
    controller.setDrawables(board.getDrawables())
    if redraw:
        controller.redrawDrawables()
    else:
        controller.drawDrawables()

def resetTiles(controller: Controller):
    resetTilePositions(board)
    controller.setDrawables(board.getDrawables())
    controller.redrawDrawables()
    controller.ui.log(f'Tilemap size set to ({board.rows},{board.columns})')
    controller.ui.drawTopText(f'Size: ({board.rows}, {board.columns})', 1)

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
    Button(label="WFC", action=runAlgorithm)
] + sizeButtons

controller = Controller(WFCParameters(), buttons=buttons)
width, height = controller.ui.settings.fieldWidth, controller.ui.settings.fieldHeight
algorithm = WFCAlgorithm(controller)
board = UIBoard(start_columns, start_rows, controller.ui)
controller.ui.drawTopText(f'Size: ({board.rows}, {board.columns})', 1)
controller.setDrawables(board.getDrawables())

controller.run()
