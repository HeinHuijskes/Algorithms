from Framework.src.algorithm import Algorithm
from Framework.src.controller import Controller
from Framework.src.drawable import Drawable

from random import random
from math import floor

class GameOfLifeAlgorithm(Algorithm):
    field: list[list[bool]]
    width: float
    height: float
    tileSize: float
    yMargin: float
    cellColour = "white"
    voidColour = "black"
    randomChance = 0.3
    showNeighboursAmount = False
    fast = True
    def __init__(self, controller: Controller, width, height, cells=75) -> None:
        super().__init__(controller)
        self.width = width
        self.height = height
        self.yMargin = controller.ui.settings.margin
        self.setFieldSize(cells)
        return

    def setFieldSize(self, cells):
        self.tileSize = min(self.width / cells, self.height / cells)
        self.cells_x = floor(self.width / self.tileSize)
        self.cells_y = floor(self.height / self.tileSize)
        self.clearField()
        return
    
    def clearField(self):
        self.field = [[False for y in range(self.cells_y)] for x in range(self.cells_x)]
        return

    def changeFieldSize(self, amount):
        cells = self.cells_y + amount
        self.tileSize = self.height / max(1, cells)
        old_x = self.cells_x
        old_y = self.cells_y
        self.cells_x = floor(self.width / self.tileSize)
        self.cells_y = floor(self.height / self.tileSize)
        self.field = [[self.field[x][y] if y < old_y and x < old_x else False for y in range(self.cells_y)] for x in range(self.cells_x)]
        return

    def updateField(self):
        newField = []
        for x, column in enumerate(self.field):
            newField.append([])
            for y, alive in enumerate(column):
                neighbours = self.getNeighbours(x, y)
                if neighbours == 3 or (alive and neighbours == 2):
                    newField[-1].append(True)
                else:
                    newField[-1].append(False)
        self.field = newField
        return
    
    def getNeighbours(self, x_index: int , y_index: int) -> int:
        neighbours = 0
        for x in range(max(0, x_index-1), min(len(self.field)-1, x_index+1)+1):
            for y in range(max(0, y_index-1), min(len(self.field[0])-1, y_index+1)+1):
                if self.field[x][y] and not (x_index == x and y_index == y):
                    neighbours += 1
        return neighbours
    
    def showField(self, clear=False):
        tiles = []
        x = 0
        y = self.yMargin
        for i, column in enumerate(self.field):
            for j, row in enumerate(column):
                if row:
                    tiles.append(Drawable((x, y), "tile", self.tileSize, self.cellColour))
                    if self.showNeighboursAmount:
                        tiles.append(Drawable((x, y), "text", (self.tileSize, self.tileSize), str(self.getNeighbours(i, j))))
                else:
                    tiles.append(Drawable((x, y), "tile", self.tileSize, self.voidColour))
                    # tiles.append(Drawable((x, y), "text", (self.tileSize, self.tileSize), str(self.getNeighbours(i, j))))
                # tiles.append(tile)
                y += self.tileSize
            x += self.tileSize
            y = self.yMargin
        self.controller.setDrawables(tiles)
        if clear:
            self.controller.ui.clearOutputScreen()
        self.controller.drawDrawables()
        return
    
    def randomFillField(self):
        self.field = [[random() < self.randomChance for y in range(len(self.field[0]))] for x in range(len(self.field))]
        return
    
    def toggleCell(self, x, y):
        x_index = floor(x / self.tileSize)
        y_index = floor((y-self.yMargin) / self.tileSize)
        self.field[x_index][y_index] = not self.field[x_index][y_index]
