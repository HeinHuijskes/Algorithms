from PIL import Image


class TUI:
    grey_gradient = ['\033[48;5;240m', '\033[48;5;242m', '\033[48;5;244m', '\033[48;5;246m', '\033[48;5;248m',
                     '\033[48;5;250m']
    grey_gradient_2 = ['\033[48;5;240m', '\033[48;5;241m', '\033[48;5;242m', '\033[48;5;243m', '\033[48;5;244m',
                       '\033[48;5;245m']
    map_colours = ['\033[47m', '\033[40m', '\033[42m', '\033[43m', '\033[46m', '\033[44m']
    palette = [grey_gradient, grey_gradient_2, map_colours]

    def print_map(self, cell_map, palette_choice=0):
        colouring = self.palette[palette_choice]
        for row in cell_map.cells:
            row_string = '\033[1m\033[30m'
            for cell in row:
                if cell.state not in cell_map.tiles:
                    row_string += ' '
                else:
                    row_string += colouring[cell.state.colour_level] + '  '
            row_string += '\033[0m'
            print(row_string)
        print('----------')

    def print(self, message):
        print(message)
