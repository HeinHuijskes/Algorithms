class MockUI():
    def drawTopText(self, text, slot):
        pass

    def drawSolution(self, route):
        pass

    def log(self, text):
        # print(text)
        pass

class MockController():
    ui = MockUI()

    def displayTimeLeft(self, timeIteration, iterations):
        pass
