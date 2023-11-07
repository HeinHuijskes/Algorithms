from Framework.src.algorithm import Algorithm
from Framework.src.controller import Controller
from Framework.src.drawable import Drawable
from Framework.src.tilemap import Tile, TileMap

from random import random
from math import floor

class GameOfLifeAlgorithm(Algorithm):
    field: list[list[bool]]
    tileMap: TileMap
    cellColour = "white"
    randomChance = 0.3
    showNeighboursAmount = False
    fast = True
    def __init__(self, controller: Controller, width, height, cells=75) -> None:
        super().__init__(controller)
        self.tileMap = TileMap(width, height, controller.ui)
        self.tileMap.setDimensions(cells, cells, fit=True)
        self.clearField()
        return
    
    def clearField(self):
        self.field = [[False for y in range(self.tileMap.tiles_y)] for x in range(self.tileMap.tiles_x)]
        return

    def changeFieldSize(self, amount):
        self.tileMap.changeDimensions(amount, amount, fit=True)
        self.field = [[tile.colour == self.cellColour for tile in column] for column in self.tileMap.tiles]
        self.redrawTileMap()
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
        self.updateTileMap()
        return
    
    def getNeighbours(self, x_index: int , y_index: int) -> int:
        neighbours = 0
        for x in range(max(0, x_index-1), min(len(self.field)-1, x_index+1)+1):
            for y in range(max(0, y_index-1), min(len(self.field[0])-1, y_index+1)+1):
                if self.field[x][y] and not (x_index == x and y_index == y):
                    neighbours += 1
        return neighbours
    
    def redrawTileMap(self):
        self.controller.ui.clearOutputScreen()
        self.tileMap.redrawTiles()
        return

    def updateTileMap(self):
        texts = []
        if self.showNeighboursAmount:
            texts = [[str(self.getNeighbours(x, y)) for y in range(self.tileMap.tiles_y)] for x in range(self.tileMap.tiles_x)]
        self.tileMap.updateTiles([[self.cellColour if cell else self.tileMap.bg_colour for cell in column] for column in self.field], texts)
        return
    
    def randomFillField(self):
        self.field = [[random() < self.randomChance for y in range(len(self.field[0]))] for x in range(len(self.field))]
        self.updateTileMap()
        return
    
    def toggleCell(self, x, y):
        x_index = floor(x / self.tileMap.cell_size)
        y_index = floor((y - self.tileMap.y_margin) / self.tileMap.cell_size)
        self.field[x_index][y_index] = not self.field[x_index][y_index]
        if self.field[x_index][y_index]:
            colour = self.cellColour
        else:
            colour = self.tileMap.bg_colour
        self.tileMap.setTile(colour, x_index, y_index, draw=True)
