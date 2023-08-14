import math
import random
import time


class Map:
    class DIRECTIONS:
        RIGHT = 'RIGHT'
        LEFT = 'LEFT'
        UP = 'UP'
        DOWN = 'DOWN'

        def all(self):
            return [self.RIGHT, self.LEFT, self.UP, self.DOWN]

    class Tile:
        def __init__(self, name, frequency, colour):
            self.name = name
            self.frequency = frequency
            self.colour = colour

    def __init__(self):
        self.directions = self.DIRECTIONS()
        self.tiles = []
        self.set_tiles()
        self.ruleSet = []
        self.set_rules()
        self.size = 20
        self.cells = [[self.Cell(x, y, self) for x in range(0, self.size)] for y in range(0, self.size)]
        self.hasContradiction = False

    def reset(self):
        self.cells = [[self.Cell(x, y, self) for x in range(0, self.size)] for y in range(0, self.size)]
        self.hasContradiction = False

    def set_tiles(self):
        self.tiles.append(self.Tile('LAND', 50, '\033[92m'))
        self.tiles.append(self.Tile('SEA', 15, '\033[94m'))
        self.tiles.append(self.Tile('COAST', 15, '\033[93m'))
        self.tiles.append(self.Tile('MOUNTAIN', 50, '\033[90m'))

    def set_rules(self):
        # Allow all tiles next to themselves and others, except SEA and LAND
        [self.ruleSet.append(('LAND', 'LAND', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('LAND', 'COAST', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('COAST', 'COAST', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('COAST', 'SEA', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('SEA', 'SEA', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('MOUNTAIN', 'LAND', direction)) for direction in self.directions.all()]
        [self.ruleSet.append(('MOUNTAIN', 'MOUNTAIN', direction)) for direction in self.directions.all()]


    def is_solved(self):
        for row in self.cells:
            for cell in row:
                if not cell.collapsed:
                    return False
        return True

    def find_lowest_entropy(self):
        lowest = None
        for row in self.cells:
            for cell in row:
                if not cell.collapsed and (lowest is None or cell.entropy() < lowest.entropy()):
                    lowest = cell

        lows = []
        for row in self.cells:
            for cell in row:
                if not cell.collapsed and cell.entropy() == lowest.entropy():
                    lows.append(cell)
        lowest = lows[math.floor(random.random() * len(lows))]
        return lowest

    def collapse(self, cell):
        cell.pick_state()
        for neighbour in self.neighbours(cell):
            if not neighbour.collapsed:
                neighbour.restrict(cell)

    def neighbours(self, cell):
        neighbours = []
        if cell.x > 0:
            neighbours.append(self.cells[cell.y][cell.x - 1])
        if cell.x < self.size - 1:
            neighbours.append(self.cells[cell.y][cell.x + 1])
        if cell.y > 0:
            neighbours.append(self.cells[cell.y - 1][cell.x])
        if cell.y < self.size - 1:
            neighbours.append(self.cells[cell.y + 1][cell.x])
        return neighbours

    def run(self):
        fails = 0
        while not (self.is_solved() and fails < 5):
            cell = self.find_lowest_entropy()
            self.collapse(cell)
            if self.hasContradiction:
                self.reset()
                fails += 1

    class Cell:
        def __init__(self, x, y, cell_map):
            self.cell_map = cell_map
            self.states = [i for i in self.cell_map.tiles]
            self.collapsed = False
            self.state = ''
            self.x = x
            self.y = y

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

        def restrict(self, cell):
            possible = False
            direction = self.get_direction(cell)
            possible_states = []
            for state in self.states:
                for rule in self.cell_map.ruleSet:
                    if (rule[0] == state.name and rule[1] == cell.state.name and rule[2] == direction) or \
                            (rule[1] == state.name and rule[0] == cell.state.name and rule[2] == direction):
                        possible = True
                if possible:
                    possible_states.append(state)
                possible = False
            self.states = possible_states
            if len(self.states) == 0:
                self.cell_map.hasContradiction = True

        def get_direction(self, cell):
            if cell.x > self.x and cell.y == self.y:
                return self.cell_map.directions.RIGHT
            if cell.x < self.x and cell.y == self.y:
                return self.cell_map.directions.LEFT
            if cell.x == self.x and cell.y > self.y:
                return self.cell_map.directions.DOWN
            if cell.x == self.x and cell.y < self.y:
                return self.cell_map.directions.UP


def print_map(cell_map):
    for row in cell_map.cells:
        row_string = ''
        for cell in row:
            if cell.state not in cell_map.tiles:
                row_string += ' '
            else:
                row_string += cell.state.colour + cell.state.name[0] + '\033[0m'
        print(row_string)
    print('----------')


def run_algorithm():
    cell_map = Map()
    cell_map.run()
    if cell_map.is_solved():
        print('Solved!')
    else:
        print('Failed!')


def run_algorithm_print(print_stepwise_map=False):
    cell_map = Map()
    fails = 0
    while not (cell_map.is_solved() and fails < 5):
        if print_stepwise_map:
            print_map(cell_map)
        cell = cell_map.find_lowest_entropy()
        cell_map.collapse(cell)
        if cell_map.hasContradiction:
            cell_map.reset()
            print('fail!')
            print_map(cell_map)
            fails += 1

    if fails > 4:
        print('5 or more failures')
    if cell_map.is_solved():
        print('Solved!')
    print_map(cell_map)


# run_algorithm_print(print_stepwise_map=True)
run_algorithm_print()

# iterations = 100
# timer_start = time.perf_counter()
# [run_algorithm() for i in range(0, iterations)]
# timer_end = time.perf_counter()
# run_time = timer_end - timer_start
# print('Ran', iterations, 'iterations in', run_time, 'seconds')
