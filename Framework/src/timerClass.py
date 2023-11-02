import pygame

class Timer():
    def __init__(self) -> None:
        pass

    runTimer = False
    time = 0
    
    def setTime(self, time):
        self.time = time
    
    def getGameTime(self):
        return pygame.time.get_ticks()

    def getElapsedTime(self):
        if self.time == 0:
            return self.time
        return (self.getGameTime()-self.time) // 100 / 10

    def getTimeString(self, seconds):
        string = ''
        if seconds < 99:
            string += str(self.decimal(seconds)) + ' seconds'
        elif seconds < 3600:
            string += str(self.decimal(seconds/60)) + ' minutes'
        elif seconds < 86400:
            string += str(self.decimal(seconds/3600)) + ' hours'
        elif seconds < 604800:
            string += str(self.decimal(seconds/86400)) + ' days'
        elif seconds < 31449600:
            string += str(self.decimal(seconds/604800)) + ' weeks'
        elif seconds < 3144960000:
            string += str(self.decimal(seconds/31449600)) + ' years'
        elif seconds < 314496000000:
            string += str(self.decimal(seconds/3144960000)) + ' centuries'
        else:
            string += '>100 centuries'
        return string
    
    def decimal(self, seconds):
        return int(seconds*10)/10
