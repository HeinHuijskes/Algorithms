import time

from wfc import Map
from view import TUI, GUI


def run_algorithm(size):
    cell_map = Map(size)
    cell_map.run()
    return cell_map.is_solved()


def run_algorithm_print(size, print_stepwise_map=False):
    cell_map = Map(size)
    UI = TUI()
    fails = 0
    while not (cell_map.is_solved() and fails < 5):
        if print_stepwise_map:
            UI.print_map(cell_map)
        cell = cell_map.find_lowest_entropy()
        cell_map.collapse(cell)
        if cell_map.hasContradiction:
            cell_map.reset()
            UI.print('fail!')
            # print_map(cell_map)
            fails += 1

    if fails > 4:
        UI.print('5 or more failures')
    if cell_map.is_solved():
        UI.print('Solved!')
    UI.print_map(cell_map)


def time_test(size=20, iterations=100):
    timer_start = time.perf_counter()
    attempts = [run_algorithm(size) for i in range(0, iterations)]
    timer_end = time.perf_counter()
    run_time = timer_end - timer_start
    print('Ran', iterations, 'iterations of size', size**2, 'in', run_time, 'seconds')
    successes = sum(attempts)
    print(str(successes), 'successes and', str(iterations-successes), 'failures')


# run_algorithm_print(40, print_stepwise_map=True)
# run_algorithm_print(50)
run_algorithm(50)
# time_test()
