import sys

sys.path.append("../Algorithms")
sys.path.append("../Algorithms/Framework")
sys.path.append("../Algorithms/Framework/src")

from Framework.src.controller import Controller
from Framework.src.button import Button
from Framework.src.drawable import Drawable
from WFCAlgorithm import WFCAlgorithm
from wfcparams import WFCParameters
from WFCPython.src.UIBoard import UITile, UIBoard, resetTilePositions
from Map import Map

start_rows = 25
start_columns = 42
allowedFails = 10

algorithm: WFCAlgorithm
buttons: list[Button]
board: UIBoard
cellMap: Map
width: int
height: int


def resetMap(controller: Controller):
    cellMap.reset()
    drawMap(cellMap, controller, redraw=True)

def runAlgorithm(controller: Controller):
    if not board.showProcess:
        quickRun(controller)
        return
    controller.startTimer()
    fails = 0
    drawMap(cellMap, controller, redraw=True)
    while not cellMap.is_solved() and fails < allowedFails:
        cell = cellMap.find_lowest_entropy_cell()
        cellMap.collapse(cell)
        drawMap(cellMap, controller)
        if cellMap.hasContradiction:
            cellMap.reset()
            controller.ui.log("Failed!")
            fails += 1
            drawMap(cellMap, controller, redraw=True)
    controller.stopTimer()
    if not cellMap.is_solved():
        controller.ui.log("Failed to solve map")
    else:
        controller.ui.log("Solved!")

def quickRun(controller: Controller):
    controller.startTimer()
    cellMap.create_map()
    controller.stopTimer()
    if cellMap.is_solved():
        controller.ui.log("Success!")
    else:
        controller.ui.log("Failed!")
    drawMap(cellMap, controller, redraw=True)

def toggleShowEntropy(controller: Controller):
    board.showEntropy = not board.showEntropy
    if board.showEntropy:
        controller.ui.log("Entropy toggled ON")
    else:
        controller.ui.log("Entropy toggled OFF")

def toggleProcess(controller: Controller):
    board.showProcess = not board.showProcess
    if board.showProcess:
        controller.ui.log("Process visuals toggled ON")
    else:
        controller.ui.log("Process visuals toggled OFF")

def drawMap(cellMap: Map, controller: Controller, redraw=False):
    tiles = []
    texts = []
    for row in cellMap.cells:
        tiles.append([])
        for cell in row:
            if cell.state != None:
                tiles[-1].append(UITile(colour=cell.state.colour))
            else:
                tiles[-1].append(UITile(colour="black"))
            if board.showEntropy:  # and cell.collapsed
                texts.append(str(cell.entropy))
    board.tiles = tiles
    resetTilePositions(board)
    drawDrawables(controller, redraw, texts)

def drawDrawables(controller: Controller, redraw: bool, texts: list[str]):
    drawables = board.getDrawables(getAll = redraw or board.showEntropy)
    if board.showEntropy:
        for i, text in enumerate(texts):
            tile = drawables[i]
            drawables.append(Drawable(tile.position, "text", (tile.size, tile.size), text))
    controller.setDrawables(drawables)
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
    cellMap.addCells(columns, rows)
    resetTiles(controller)

def decreaseDimensions(controller: Controller, rows=1, columns=1):
    board.rows = max(1, board.rows - columns)
    board.columns = max(1, board.columns - rows)
    tiles = []
    for i in range(board.columns):
        tiles.append([])
        for j in range(board.rows):
            tiles[-1].append(board.tiles[i][j])
    board.tiles = tiles
    cellMap.removeCells(columns, rows)
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
    Button(label="Reset", action=resetMap),
    Button(label="WFC", action=runAlgorithm),
    Button(label="Entropy", action=toggleShowEntropy),
    Button(label="Show updates", action=toggleProcess),
] + sizeButtons

controller = Controller(WFCParameters(), buttons=buttons)
width, height = controller.ui.settings.fieldWidth, controller.ui.settings.fieldHeight
algorithm = WFCAlgorithm(controller)
board = UIBoard(start_columns, start_rows, controller.ui)
controller.ui.drawTopText(f'Size: ({board.rows}, {board.columns})', 1)
controller.setDrawables(board.getDrawables())
cellMap = Map(start_columns, start_rows)

controller.run()
