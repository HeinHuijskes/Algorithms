import math
from random import randint, choices

from Framework.algorithm import Algorithm
from Framework.controller import Controller

class ACOAlgorithm(Algorithm):
    pheromoneTrails: dict = {}
    # Higher distance power makes the ant more likely to travel to nearby nodes
    distancePower = 5
    pheromonePower = 1
    ants = 50
    evaporationRate = 0.3
    pheromoneDeposit = 1
    initialPheromone = 1
    iterations = 100
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)

    def addIterations(self, change):
        self.iterations = max(1, self.iterations + change)

    def run(self, positions):
        self.initializePheromone(positions)
        initLength = self.getRouteLength(positions)
        bestRoute, bestLength = self.updateRoute([positions], [initLength], positions, initLength+1, 0)
        # Increase the number of ants for larger networks
        self.ants = max(50, len(positions))

        for i in range(self.iterations):
            routes = self.antsTravel(positions)
            scores = self.scoreRoutes(routes)
            self.updatePheromones(routes, scores)
            bestRoute, bestLength = self.updateRoute(routes, scores, bestRoute, bestLength, i+1)

        # self.log(f'Best found length: {bestLength}')
        return bestRoute, bestLength

    def updateRoute(self, routes, scores, bestRoute, bestLength, iteration):
        oldBest = bestLength
        bestRoute, bestLength = self.smallestRoute(routes, scores, bestRoute, bestLength)
        self.controller.ui.drawTopText(f'Iteration: {iteration}', 3)
        if oldBest != bestLength:
            self.controller.ui.drawSolution(bestRoute)
        if (iteration) % (max(self.iterations//10,1)) == 0:
            self.log(f'({iteration}): c={int(min(scores))} b={int(bestLength)}')
        return bestRoute, bestLength

    def smallestRoute(self, routes, scores, bestRoute, bestLength):
        for i, score in enumerate(scores):
            if score < bestLength:
                bestLength = score
                bestRoute = routes[i]
        return bestRoute, bestLength

    def initializePheromone(self, positions):
        # Link every node to every other node
        # This requires `n^2` memory, which is a lot better than `n!` memory for bruteforce
        for position in positions:
            for pos in positions:
                if pos == position:
                    continue
                self.pheromoneTrails[(position, pos)] = self.initialPheromone

    def antsTravel(self, positions: list[tuple]):
        routes = []
        for i in range(self.ants):
            current = positions[randint(0, len(positions)-1)]
            visited = [current]
            for i in range(len(positions)-1):
                possible = [x for x in positions if x not in visited]
                current = self.findNextNode(possible, current)
                visited.append(current)
            routes.append(visited)
        return routes

    def findNextNode(self, positions: list[tuple], current: tuple):
        desirabilities = []
        for node in positions:
            desirability = math.pow(1 / self.distance(current, node), self.distancePower)
            pheromoneStrength = math.pow(self.pheromoneTrails[(current, node)], self.pheromonePower)
            desirabilities.append(desirability * pheromoneStrength)
        total = sum(desirabilities)

        probabilities = [desire/total for desire in desirabilities]
        return choices(positions, weights=probabilities, k=1)[0]

    def scoreRoutes(self, routes):
        scores = []
        for route in routes:
            scores.append(self.getRouteLength(route))
        return scores
    
    def getRouteLength(self, route):
        length = 0
        prev = route[-1]
        for node in route:
            length += self.distance(prev, node)
            prev = node
        return length

    def distance(self, node1, node2):
        return math.sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)

    def updatePheromones(self, routes, scores):
        # Evaporate pheromones
        for direction, pheromone in self.pheromoneTrails.items():
            pheromone = (1 - self.evaporationRate) * pheromone
            self.pheromoneTrails[direction] = pheromone

        # Add new pheromone
        for i, route in enumerate(routes):
            score = scores[i]
            prev = route[-1]
            for j, node in enumerate(route):
                line = (prev, node)
                pheromone = self.pheromoneTrails[line] + self.pheromoneDeposit / score
                self.pheromoneTrails[line] = pheromone
                prev = node
