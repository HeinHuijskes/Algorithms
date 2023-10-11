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
    route = []
    for i in range(len(positions)):
        route.append(positions[indexes[i]])
    return route

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
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
        self.aco = ACOAlgorithm(controller)

    def bruteForce(self, positions: list[tuple]):
        if len(positions) <= 3:
            return positions

        routes = []
        firstRoute = [i for i in range(len(positions))]
        self.getAllRoutesRecurse(firstRoute, 1, routes)
        self.log(f'Checking {len(routes)} routes to find the best one')

        if self.controller.parameters.parallel:
            if __name__ == "__main__":
                routes = self.parallelSearch(routes, positions)

        # Find the best result out of all best results from different threads
        bestRoute = self.findBestRoute(routes, positions)
        self.log(f'Found the best route! It has length {getRouteLength(bestRoute, positions)}')
        return indexesToRoute(bestRoute, positions)
    
    def parallelSearch(self, routes: list[list[int]], positions: list[tuple]):
        processes = []
        numProcesses = len(positions)
        bestRoutes = [0 for i in range(numProcesses)]
        step = len(routes) // len(positions)
        self.log(f'Step: {str(step)}')
        self.log(f'Routes: {str(len(routes))}')
        self.log(f'Positions: {str(len(positions))}')
        for i in range(numProcesses):
            self.log(f': {str(step)}')
            subset = routes[step*i:step*(i+1)]
            process = Process(target=self.findBestRoute, args=(subset, positions, bestRoutes, i,))
            process.start()
            processes.append[process]
        for i in range(len(processes)):
            processes[i].join()
        return bestRoutes
        
    def getAllRoutesRecurse(self, route: list[int], depth: int, routes: list[list[int]]):
        if (depth == len(route)-1):
            routes.append(route)
            return

        currentRoute = []
        self.getAllRoutesRecurse(route, depth+1, routes)
        for i in range(depth+1, len(route)):
            currentRoute = [i for i in route]
            currentRoute[depth] = route[i]
            currentRoute[i] = route[depth]
            self.getAllRoutesRecurse(currentRoute, depth+1, routes)

    def findBestRoute(self, routes: list[list[int]], positions: list[tuple], bestRoutes: list[list[int]]=[], procesNum=None):
        # TODO: find out if "bestRoutes" is a necessary list
        bestRoute = routes[0]
        bestLength = getRouteLength(bestRoute, positions)
        for route in routes:
            length = getRouteLength(route, positions)
            if length < bestLength:
                bestLength = length
                bestRoute = route
                solution = indexesToRoute(bestRoute, positions)
                self.controller.ui.drawSolution(solution)
        
        if procesNum != None:
            bestRoutes[procesNum] = bestRoute
        return bestRoute
