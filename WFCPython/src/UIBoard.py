import sys
sys.path.append('./src/Framework')

from random import randint

from Framework.src.drawable import Drawable

# BOARD REPRESENTATION:
# board[x][y] = board[column][row]


TILE_COLOURS = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]

class UITile:
    x: float
    y: float
    size: float
    colour: str
    drawable: any
    def __init__(self, x=0.0, y=0.0, size=100, colour="white") -> None:
        self.x = x
        self.y = y
        self.size = size
        self.colour = TILE_COLOURS[randint(0, len(TILE_COLOURS)-1)]
    
    def draw(self, ui):
        self.drawable.draw(ui)


class UIBoard:
    tiles: list[list[UITile]]
    rows: int
    columns: int

    def __init__(self, rows, columns, ui) -> None:
        tiles = []
        self.rows = rows
        self.columns = columns
        self.width = ui.settings.fieldWidth
        self.height = ui.settings.fieldHeight
        self.x = 0
        self.y = ui.settings.margin
        self.resetTile = Drawable((self.x, self.y), "tile", size=self.height, value=ui.settings.bgColour)
        for i in range(columns):
            tiles.append([])
            for j in range(rows):
                tiles[-1].append(UITile())
        self.tiles = tiles
        resetTilePositions(self)
    
    def getDrawables(self):
        drawables = []
        for row in self.tiles:
            for tile in row:
                drawables.append(tile.drawable)
        return drawables


def resetTilePositions(board: UIBoard):
    tiles = board.tiles
    tiles_horizontal = len(tiles[0])
    tiles_vertical = len(tiles)
    tile_width = board.width / tiles_horizontal
    tile_height = board.height / tiles_vertical
    size = min(tile_width, tile_height)
    tile_y = board.y
    for row in tiles:
        tile_x = board.x
        for tile in row:
            tile.x = tile_x
            tile.y = tile_y
            tile.size = size
            tile.drawable = Drawable((tile.x, tile.y), "tile", tile.size, tile.colour)
            tile_x += size
        tile_y += size
    board.tiles = tiles
    return