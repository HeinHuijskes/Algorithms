from random import random
from multiprocess import Process
import math

from Framework.algorithm import Algorithm
from Framework.controller import Controller

from AntColonyOptimization import ACOAlgorithm

def getRandomPosition(width: int, height: int, margin: int=0):
    return (random()*(width-2*margin)+margin, random()*(height-2*margin)+margin+50)

def getRandomPositions(width: int, height: int, amount:int , margin: int=0):
    positions = []
    for i in range(amount):
        positions.append(getRandomPosition(width, height, margin))
    return positions

def indexesToRoute(indexes: list[int], positions: list[tuple]):
    return [positions[indexes[i]] for i in range(len(positions))]

def getRouteLength(route: list, positions: list[tuple], ):
    # Use pythogoras to find the length between to positions
    prev = positions[route[-1]]
    length = 0
    for i in range(len(route)):
        curr = positions[route[i]]
        x = abs(curr[0] - prev[0])
        y = abs(curr[1] - prev[1])
        length += math.sqrt(x**2 + y**2)
        prev = positions[route[i]]
    return length

class TSMAlgorithm(Algorithm):
    numRoutes: int
    bestLength: int
    iterations: int
    positions: list[tuple]
    iteration: int
    updateTime: int
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
        self.aco = ACOAlgorithm(controller)
    
    def initialize(self, positions: list[tuple], firstRoute):
        self.iteration = 0
        self.numRoutes = math.factorial(len(positions)-1)
        self.bestLength = getRouteLength(firstRoute, positions)
        self.bestRoute = firstRoute
        self.positions = positions
        self.updateTime = self.controller.parameters.updateTime

    def bruteForce(self, positions: list[tuple]):
        if len(positions) <= 3:
            return positions    

        firstRoute = [i for i in range(len(positions))]
        self.initialize(positions, firstRoute)
        self.getAllRoutesRecurse(firstRoute, 1)

        self.log(f'Found the best route! It has length {self.bestLength}')
        return indexesToRoute(self.bestRoute, self.positions)
        
    def getAllRoutesRecurse(self, route: list[int], depth: int):
        if (depth == len(route)-1):
            self.updateBestRoute(route)
            return

        currentRoute = []
        self.getAllRoutesRecurse(route, depth+1)
        for i in range(depth+1, len(route)):
            currentRoute = [i for i in route]
            currentRoute[depth] = route[i]
            currentRoute[i] = route[depth]
            self.getAllRoutesRecurse(currentRoute, depth+1)
        return

    def updateBestRoute(self, route):
        self.iteration += 1
        if self.iteration % self.updateTime == 1:
            self.controller.displayTimeLeft(self.iteration, self.numRoutes)

        length = getRouteLength(route, self.positions)
        if self.bestLength > length:
            self.bestRoute = route
            self.bestLength = length
            self.controller.ui.drawSolution(indexesToRoute(route, self.positions))    
