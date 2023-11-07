from math import floor

import pygame

from ui import UI

class Tile():
    text: str
    def __init__(self, colour, x, y, size_x, size_y) -> None:
        self.colour = colour
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.text = None
        return
    
    def draw(self, ui: UI, drawText=False):
        tile = pygame.Rect(self.x, self.y, self.size_x, self.size_y)
        pygame.draw.rect(ui.screen, self.colour, tile)
        if drawText:
            drawText()
        return
    
    def drawText(self, ui: UI, fontSize=12, colour="black"):
        font = pygame.font.SysFont(ui.settings.font, fontSize)
        text = font.render(self.text, True, colour)
        text_rect = text.get_rect(center=(self.x+self.size_x/2, self.y+self.size_y/2))
        ui.screen.blit(text, text_rect)
        return

class TileMap():
    width: float
    height: float
    y_margin = 50  # Based on UISettings.margin
    tiles_x: int
    tilex_y: int
    cell_size: float
    tiles: list[list[Tile]]
    bg_colour = "black"
    ui: UI
    def __init__(self, width, height, ui: UI) -> None:
        self.width = width
        self.height = height
        self.ui = ui
        return
    
    def setDimensions(self, tiles_x, tiles_y, fit=False):
        self.cell_size = min(self.width / tiles_x, self.height / tiles_y)
        if fit:
            self.tiles_x = floor(self.width / self.cell_size)
            self.tiles_y = floor(self.height / self.cell_size)
        else:
            self.tiles_x = self.tiles_x
            self.tiles_y = self.tiles_y
        self.tiles = [[Tile(self.bg_colour, x*self.cell_size, y*self.cell_size + self.y_margin, self.cell_size, self.cell_size) for y in range(self.tiles_y)] for x in range(self.tiles_x)]
        return
    
    def changeDimensions(self, change_x, change_y, fit=False):
        tiles_x = self.tiles_x
        tiles_y = self.tiles_y
        self.cell_size = max(1, min(self.width / (self.tiles_x + change_x), self.height / (self.tiles_y + change_y)))

        if fit:
            self.tiles_x = floor(self.width / self.cell_size)
            self.tiles_y = floor(self.height / self.cell_size)
        else:
            self.tiles_x = self.tiles_x + change_x
            self.tiles_y = self.tiles_y + change_y

        for x, column in enumerate(self.tiles):
            for y, tile in enumerate(column):
                tile.size_x = self.cell_size
                tile.size_y = self.cell_size
                tile.x = x*self.cell_size
                tile.y = y*self.cell_size + self.y_margin

        self.tiles = [[self.tiles[x][y] if y < tiles_y and x < tiles_x 
                       else Tile(self.bg_colour, x*self.cell_size, y*self.cell_size + self.y_margin, self.cell_size, self.cell_size) 
                       for y in range(self.tiles_y)] for x in range(self.tiles_x)]
        return
    
    def setTile(self, colour, x_index, y_index, text=None, draw=False):
        tile = Tile(colour, x_index*self.cell_size, y_index*self.cell_size + self.y_margin, self.cell_size)
        if text != None:
            tile.text = text
        if draw:
            tile.draw(self.ui)
        self.tiles[x_index][y_index] = tile
        return
    
    def redrawTiles(self, showText=False):
        for column in self.tiles:
            for tile in column:
                tile.draw(self.ui)
                if showText:
                    tile.drawText(self.ui)
        return

    
    def updateTiles(self, colours, texts=[]):
        updateTexts = len(texts) > 0
        for x, column in enumerate(colours):
            for y, colour in enumerate(column):
                redraw, drawText = False, False
                tile = self.tiles[x][y]
                if tile.colour != colour:
                    tile.colour = colour
                    redraw = True

                if updateTexts and tile.text != texts[x][y]:
                    tile.text = texts[x][y]
                    redraw = True
                    drawText = True
                
                if redraw:
                    tile.draw(self.ui)
                if drawText:
                    tile.drawText(self.ui)