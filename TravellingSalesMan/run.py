from threading import Thread, active_count

from ui import UI
from console import Console
from TSMAlgorithm import getRandomPositions

from tsmparams import parameters

scr = parameters["screen"]
positions = getRandomPositions(scr["width"]-scr["menu-width"], scr["height"], parameters["dots"]["amount"])

def run():
    console = Console(UI(parameters), parameters)
    # button = {"active": True, "position": (), "action": "bruteForce"}
    console.setObjects({"positions": positions})  # , "buttons": [button]
    console.run()

run()