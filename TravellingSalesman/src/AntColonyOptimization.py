import sys
sys.path.append("../Algorithms/Framework/src")
sys.path.append("../Algorithms")

import math
from random import randint, choices

from Framework.src.algorithm import Algorithm
from Framework.src.controller import Controller

class ACOAlgorithm(Algorithm):
    positions: list[tuple]
    positionsSize: int
    pheromoneTrails: list[list[float]] = []
    distances: list[list[float]] = []
    ### Settings ###
    # Higher distance power makes the ant more likely to travel to nearby nodes
    distancePower = 10
    pheromonePower = 1
    # According to a paper, around 30% of the network size is an optimal number of ants (albeit for MMAS) (see the "Number of ants" source in README.md)
    ants: int
    antFraction = 0.3
    evaporationRate = 0.5
    pheromoneDeposit = 1
    initialPheromone = 1
    iterations = 100
    ### ###

    timeIteration: int
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)

    def addIterations(self, change: int):
        self.iterations = max(1, self.iterations + change)

    def initialize(self, positions: list[tuple]):
        self.positionsSize = len(positions)
        self.positions = positions
        self.initializePheromone()
        self.setDistances()
        self.timeIteration = 0
        initLength = self.getRouteLength([i for i in range(self.positionsSize)])
        self.ants = max(10, int(self.positionsSize*0.3))
        return self.updateRoute([[i for i in range(self.positionsSize)]], [initLength], [i for i in range(self.positionsSize)], initLength+1, 0)

    def setDistances(self):
        # Precalculate distances to reduce computation time later
        self.distances = [[self.distance(i, j) for i in range(self.positionsSize)] for j in range(self.positionsSize)]

    def initializePheromone(self):
        self.pheromoneTrails = [[self.initialPheromone for i in range(self.positionsSize)] for j in range(self.positionsSize)]

    def run(self, positions: list[tuple]):
        bestRoute, bestLength = self.initialize(positions)

        for i in range(self.iterations):
            routes = self.antsTravel()
            scores = self.scoreRoutes(routes)
            self.updatePheromones(routes, scores)
            bestRoute, bestLength = self.updateRoute(routes, scores, bestRoute, bestLength, i+1)

        # self.log(f'Best found length: {bestLength}')
        return bestRoute, bestLength

    def updateRoute(self, routes: list[list[int]], scores: list[float], bestRoute: int, bestLength: float, iteration: int):
        oldBest = bestLength
        bestRoute, bestLength = self.smallestRoute(routes, scores, bestRoute, bestLength)
        self.controller.ui.drawTopText(f'Iteration: {iteration}', 3)
        self.updateTime()
        if oldBest != bestLength:
            self.controller.ui.drawSolution([self.positions[bestRoute[i]] for i in range(self.positionsSize)])
        if self.iterations < 10 or iteration % (self.iterations//10) == 0:
            self.log(f'({iteration}): c={int(min(scores))} b={int(bestLength)}')
        return bestRoute, bestLength

    def smallestRoute(self, routes: list[list[int]], scores: list[float], bestRoute: int, bestLength: float):
        for i, score in enumerate(scores):
            if score < bestLength:
                bestLength = score
                bestRoute = routes[i]
        return bestRoute, bestLength

    def updateTime(self):
        self.controller.displayTimeLeft(self.timeIteration, self.iterations)
        self.timeIteration += 1

    def antsTravel(self):
        routes = []
        for i in range(self.ants):
            current = randint(0, self.positionsSize-1)
            visited = [current]
            for j in range(self.positionsSize-1):
                possible = [x for x in range(self.positionsSize) if x not in visited]
                current = self.findNextNode(possible, current)
                visited.append(current)
            routes.append(visited)
        return routes

    def findNextNode(self, nextPositions: list[int], current: int):
        desirabilities = []
        for node in nextPositions:
            desirability = math.pow(1 / self.distances[current][node], self.distancePower)
            pheromoneStrength = self.pheromoneTrails[current][node]
            if self.pheromonePower != 1:
                pheromoneStrength = math.pow(pheromoneStrength, self.pheromonePower)
            desirabilities.append(desirability * pheromoneStrength)
        total = sum(desirabilities)

        probabilities = [desire/total for desire in desirabilities]
        return choices(nextPositions, weights=probabilities)[0]

    def scoreRoutes(self, routes: list[list[int]]):
        return [self.getRouteLength(route) for route in routes]
    
    def getRouteLength(self, route: list[list[int]]):
        length = 0
        prev = route[-1]
        for node in route:
            length += self.distances[prev][node]
            prev = node
        return length

    def distance(self, node1: int, node2: int):
        len1 = (self.positions[node1][0]-self.positions[node2][0])
        len2 = (self.positions[node1][1]-self.positions[node2][1])
        return math.sqrt(len1*len1 + len2*len2)

    def updatePheromones(self, routes: list[list[int]], scores: list[float]):
        # Evaporate pheromones
        for i in range(self.positionsSize):
            for j in range(self.positionsSize):
                self.pheromoneTrails[i][j] = (1 - self.evaporationRate) * self.pheromoneTrails[i][j]

        # Add new pheromone
        for i, route in enumerate(routes):
            score = scores[i]
            prev = route[-1]
            for node in route:
                pheromone = self.pheromoneTrails[prev][node] + self.pheromoneDeposit / score
                self.pheromoneTrails[prev][node] = pheromone
                prev = node
