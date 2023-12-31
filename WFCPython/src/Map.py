import math
import random


class Map:
    class DIRECTIONS:
        RIGHT = 'RIGHT'
        LEFT = 'LEFT'
        UP = 'UP'
        DOWN = 'DOWN'

        def all(self):
            return [self.RIGHT, self.LEFT, self.UP, self.DOWN]

    class Tile:
        def __init__(self, name, frequency, colour_level, colour="black"):
            self.name = name
            self.frequency = frequency
            self.colour = colour
            self.colour_level = colour_level

    def __init__(self, size_x: int, size_y: int):
        self.directions = self.DIRECTIONS()
        self.tiles = []
        self.set_tiles()
        self.ruleSet = []
        self.set_rules()
        self.size_x = size_x
        self.size_y = size_y
        self.cells = [[self.Cell(x, y, self) for y in range(0, self.size_y)] for x in range(0, self.size_x)]
        self.hasContradiction = False

    def addCells(self, add_x, add_y):
        self.size_x += add_x
        self.size_y += add_y
        for x, column in enumerate(self.cells):
            for i in range(add_x):
                column.append(self.Cell(x + i, y, self))
        pass

    def removeCells(self, rem_x, rem_y):
        pass

    def reset(self):
        self.cells = [[self.Cell(x, y, self) for y in range(0, self.size_y)] for x in range(0, self.size_x)]
        self.hasContradiction = False

    def set_tiles(self):
        self.tiles.append(self.Tile('HEAVEN', 8, 0, colour="white"))
        self.tiles.append(self.Tile('MOUNTAIN', 15, 1, colour="grey"))
        self.tiles.append(self.Tile('LAND', 15, 2, colour="green"))
        self.tiles.append(self.Tile('COAST', 15, 3, colour="yellow"))
        self.tiles.append(self.Tile('SEA', 15, 4, colour="blue"))
        self.tiles.append(self.Tile('OCEAN', 8, 5, colour="purple"))

    def set_rules(self):
        [self.ruleSet.append(('HEAVEN', 'HEAVEN', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('HEAVEN', 'MOUNTAIN', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('MOUNTAIN', 'MOUNTAIN', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('MOUNTAIN', 'LAND', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('LAND', 'LAND', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('LAND', 'COAST', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('COAST', 'COAST', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('COAST', 'SEA', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('SEA', 'SEA', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('SEA', 'OCEAN', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('OCEAN', 'OCEAN', direction)) for direction in self.directions.all()]

    def is_solved(self):
        for row in self.cells:
            for cell in row:
                if not cell.collapsed:
                    return False
        return True

    def find_lowest_entropy_cell(self):
        lowest = None
        for column in self.cells:
            for cell in column:
                if not cell.collapsed and (lowest is None or cell.entropy < lowest.entropy):
                    lowest = cell

        lows = []
        for column in self.cells:
            for cell in column:
                if not cell.collapsed and cell.entropy == lowest.entropy:
                    lows.append(cell)
        index = math.floor(random.random() * len(lows))
        lowest = lows[index]

        return lowest

    def collapse(self, cell):
        cell.pick_state()
        for neighbour in self.neighbours(cell):
            if not neighbour.collapsed:
                neighbour.restrict(cell)
        # self.propagate_change(cell)

    def propagate_change(self, changedCell):
        change_queue = self.neighbours(changedCell)
        while change_queue:
            queue_cell = change_queue.pop(0)
            entropy = queue_cell.entropy
            [queue_cell.restrict(cell) for cell in self.neighbours(queue_cell)]
            if self.hasContradiction:
                print("Contradiction in propagation!")
                break
            if queue_cell.entropy < entropy:
                change_queue += self.neighbours(queue_cell)

    def neighbours(self, cell):
        neighbours = []
        if cell.x > 0:
            neighbours.append(self.cells[cell.x-1][cell.y])
        if cell.x < self.size_x-1:
            neighbours.append(self.cells[cell.x+1][cell.y])
        if cell.y > 0:
            neighbours.append(self.cells[cell.x][cell.y-1])
        if cell.y < self.size_y-1:
            neighbours.append(self.cells[cell.x][cell.y+1])
        return neighbours

    def create_map(self):
        fails = 0
        while fails < 5:
            if self.is_solved():
                break
            cell = self.find_lowest_entropy_cell()
            self.collapse(cell)
            if self.hasContradiction:
                self.reset()
                fails += 1
        return fails

    class Cell:
        def __init__(self, x, y, cell_map):
            self.cell_map = cell_map
            self.states = [i for i in self.cell_map.tiles]
            self.collapsed = False
            self.state = None
            self.x = x
            self.y = y
            self.entropy = len(self.states)

        def entropy(self):
            return len(self.states)

        def pick_state(self):
            total_weight = sum([tile.frequency for tile in self.states])
            random_value = random.random() * total_weight
            weight = 0
            index = len(self.states)-1
            for key, value in enumerate(self.states):
                weight += value.frequency
                if weight > random_value:
                    index = key
                    break

            self.state = self.states[index]
            self.collapsed = True
            self.states = [self.state]
            self.entropy = 1

        def restrict(self, cell):
            # possible = False
            direction = self.get_direction(cell)
            possible_states = []
            for state in self.states:
                for rule in self.cell_map.ruleSet:
                    if cell.state is None:
                        for cell_state in cell.states:
                            if rule[2] == direction and ((rule[0] == state.name and rule[1] == cell_state.name) or
                                                         (rule[1] == state.name and rule[0] == cell_state.name)):
                                possible_states.append(state)
                    else:
                        if (rule[0] == state.name and rule[1] == cell.state.name and rule[2] == direction) or \
                                (rule[1] == state.name and rule[0] == cell.state.name and rule[2] == direction):
                            possible_states.append(state)
                # if possible:
                #     possible_states.append(state)
                # possible = False
            changed = not (len(self.states) == len(possible_states))
            self.states = possible_states
            if len(self.states) == 0:
                self.cell_map.hasContradiction = True
            self.entropy = len(self.states)
            return changed

        def get_direction(self, cell):
            if cell.x > self.x and cell.y == self.y:
                return self.cell_map.directions.RIGHT
            if cell.x < self.x and cell.y == self.y:
                return self.cell_map.directions.LEFT
            if cell.x == self.x and cell.y > self.y:
                return self.cell_map.directions.DOWN
            return self.cell_map.directions.UP
