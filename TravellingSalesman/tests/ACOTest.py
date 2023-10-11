import sys
sys.path.append("./TravellingSalesman")

from AntColonyOptimization import *
from Mocks import MockController
from time import perf_counter
from testVars import nodes, scores, routes


def benchMark(func, args=[], iterations=1000, repeats=5):
    # print(f'Calling function {name}')
    results = []
    for i in range(repeats):
        start = perf_counter()
        for j in range(iterations):
            func(*args)
        end = perf_counter()
        elapsed = end - start
        results.append(elapsed)
    return int(sum(results)/len(results)*100)/100


# testNodeNumber = [10, 25, 50, 99]
# testIterations = [10, 50, 99]
testNodeNumber = [99]
testIterations = [25]

def run():
    print()
    print(f'Benchmarking ACO.run()')
    for nodeNumber in testNodeNumber:
        algorithm = ACOAlgorithm(MockController())
        nodesSubset = nodes[:nodeNumber]
        for iterations in testIterations:
            algorithm.iterations = iterations
            # Here the number of iterations as an argument is 1, since the function internally uses self.iterations to perform more iterations
            result = benchMark(algorithm.run, args=[nodesSubset], iterations=1, repeats=1)
            print(f'> [Iter: {iterations}] [Nodes: {len(nodesSubset)}] Ran in {result} seconds')
    print()

### Each of the below functions are called "iteration" times per run

def scoreRoutes():
    # The benchmarks for scoreRoutes() and updatePheromones() are a bit too high, since they
    # consider routes and scores that can be higher than their nodesSubset counterpart.
    print(f'Benchmarking AOC.scoreRoutes()')
    for nodeNumber in testNodeNumber:
        algorithm = ACOAlgorithm(MockController())
        nodesSubset = nodes[:nodeNumber]
        for iterations in testIterations:
            result = benchMark(algorithm.scoreRoutes, args=[routes], iterations=iterations, repeats=1)
            print(f'> [Iter: {iterations}] [Nodes: {len(nodesSubset)}] Ran in {result} seconds')
    print()

def updatePheromones():
    print(f'Benchmarking AOC.updatePheromones()')
    for nodeNumber in testNodeNumber:
        algorithm = ACOAlgorithm(MockController())
        nodesSubset = nodes[:nodeNumber]
        algorithm.initializePheromone(nodes)
        for iterations in testIterations:
            result = benchMark(algorithm.updatePheromones, args=[routes, scores], iterations=iterations, repeats=1)
            print(f'> [Iter: {iterations}] [Nodes: {len(nodesSubset)}] Ran in {result} seconds')
    print()

def updateRoute():
    # The function updateRoute() is not benchmarked, since it is not computationally heavy, but instead only runs visuals.
    # It can be manually tested by opening the GUI, and running very high iterations on low node counts, and comparing this time to higher node counts.
    # If the difference is apparent, the GUI and therefore updateRoute() is not at fault :)
    print(f'Not benchmarking AOC.updateRoute()')
    print()

def antsTravel():
    print(f'Benchmarking AOC.antsTravel()')
    for nodeNumber in testNodeNumber:
        algorithm = ACOAlgorithm(MockController())
        nodesSubset = nodes[:nodeNumber]
        algorithm.ants = max(25, int(len(nodesSubset)*0.3))
        for iterations in testIterations:
            result = benchMark(algorithm.antsTravel, args=[nodesSubset], iterations=iterations, repeats=1)
            print(f'> [Iter: {iterations}] [Nodes: {len(nodesSubset)}] Ran in {result} seconds')
    print()

def findNextNode():
    # antsTravel() seems to take the longest time, so below it's inner workings are benchmarked
    # findNextNode() is called for each iteration, for each ant, for each position (-1)
    print(f'Benchmarking AOC.findNextNode()')
    for nodeNumber in testNodeNumber:
        algorithm = ACOAlgorithm(MockController())
        nodesSubset = nodes[:nodeNumber]
        algorithm.initializePheromone(nodes)
        ants = max(25, int(len(nodesSubset)*0.3))
        numPositions = len(nodesSubset)
        current = nodes[-1]
        # findNextNode() performs differently based on the amount of positions fed to it.
        # It searches through all positions linearly, and subsequently through all positions minus one, etc., until there is only the one position left.
        # This behaviour is approximated by letting it search through half of all positions every time, which is the average number of positions it should normally search.
        for i in [0, numPositions//2, numPositions-1]:
            positions = nodesSubset[i:]
            for iterations in testIterations:
                testIteration = iterations * ants * numPositions
                result = benchMark(algorithm.findNextNode, args=[positions, current], iterations=testIteration, repeats=1)
                print(f'> [Iter: {testIteration}] [Nodes: {len(positions)}] Ran in {result} seconds')
    print()

def test():
    run()
    scoreRoutes()
    updatePheromones()
    updateRoute()
    antsTravel()
    findNextNode()

test()
