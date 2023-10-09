from random import random
from threading import Thread
import math

def getRandomPosition(width, height, margin=0.05):
    return (random()*width, random()*height)

def getRandomPositions(width, height, amount):
    positions = []
    for i in range(amount):
        positions.append(getRandomPosition(width, height))
    return positions

def bruteForce(positions, console):
    # routeroutes = [[] for i in range(len(positions))]
    routes = []
    firstRoute = [i for i in range(len(positions))]
    # firstRoutes = []
    # for i in range(len(positions)):
        # firstRoute.append(i)
    
    # print(f'positions: {positions}')

    # threads = []
    # for i in range(len(positions)):
        # threads.append(Thread(target=getAllRoutesRecurse, args=(firstRoute, 1, routeroutes[i])))

    getAllRoutesRecurse(firstRoute, 1, routes)
    # print(f'Routes: {routes}')
    print(f'Checking {len(routes)} routes to find the best one')

    threads = []
    bestRoutes = []
    step = len(routes) // len(positions)
    for i in range(len(positions)):
        subset = routes[step*i:step*(i+1)]
        threads.append(Thread(target=findBestRoute, args=(subset, positions, bestRoutes)))
        threads[i].start()
        # bestRoute = findBestRoute(routes, positions)
    
    for i in range(len(threads)):
        threads[i].join()
        # print(f'Joined thread {i}')
    
    # print(f'bestRoutes has size {len(bestRoutes)}')
    bestRoute = findBestRoute(bestRoutes, positions)
    
    print(f'Found the best route! It has length {getRouteLength(positions, bestRoute)}')
    orderedPositions = []
    for i in range(len(positions)):
        orderedPositions.append(positions[bestRoute[i]])
    
    # TODO: move this to console somehow
    console.objects["solution"] = orderedPositions
    console.algorithmFinished = True
    console.runTimer = False
    return
    
def getAllRoutesRecurse(route, depth, routes):
    if (depth == len(route)-1):
        routes.append(route)
        return

    currentRoute = []
    getAllRoutesRecurse(route, depth+1, routes)
    for i in range(depth+1, len(route)):
        currentRoute = [i for i in route]
        # print(f'Current route: {currentRoute}')
        currentRoute[depth] = route[i]
        currentRoute[i] = route[depth]
        getAllRoutesRecurse(currentRoute, depth+1, routes)

def findBestRoute(routes, positions, bestRoutes=[]):
    bestRoute = routes[0]
    bestLength = getRouteLength(positions, bestRoute)
    for route in routes:
        length = getRouteLength(positions, route)
        if length < bestLength:
            bestLength = length
            bestRoute = route
    
    bestRoutes.append(bestRoute)
    return bestRoute

def getRouteLength(positions, route):
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
