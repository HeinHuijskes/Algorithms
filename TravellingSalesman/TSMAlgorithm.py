from random import random
from threading import Thread
import math

def getRandomPosition(width, height, margin=0):
    return (random()*(width-2*margin)+margin, random()*(height-2*margin)+margin)

def getRandomPositions(width, height, amount, margin=0):
    positions = []
    for i in range(amount):
        positions.append(getRandomPosition(width, height, margin))
    return positions

def bruteForce(positions, controller=None):
    if len(positions) <= 3:
        return positions
    routes = []
    firstRoute = [i for i in range(len(positions))]

    getAllRoutesRecurse(firstRoute, 1, routes)
    if controller != None:
        controller.ui.log(f'Checking {len(routes)} routes to find the best one')

    threads = []
    bestRoutes = []
    step = len(routes) // len(positions)
    for i in range(len(positions)):
        subset = routes[step*i:step*(i+1)]
        threads.append(Thread(target=findBestRoute, args=(subset, positions, bestRoutes)))
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    # Find the best result out of all best results from different threads
    bestRoute = findBestRoute(bestRoutes, positions)

    if controller != None:
        controller.ui.log(f'Found the best route! It has length {getRouteLength(positions, bestRoute)}')
    orderedPositions = []
    for i in range(len(positions)):
        orderedPositions.append(positions[bestRoute[i]])

    return orderedPositions
    
def getAllRoutesRecurse(route, depth, routes):
    if (depth == len(route)-1):
        routes.append(route)
        return

    currentRoute = []
    getAllRoutesRecurse(route, depth+1, routes)
    for i in range(depth+1, len(route)):
        currentRoute = [i for i in route]
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
