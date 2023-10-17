from Framework.src.algorithm import Algorithm
from Framework.src.controller import Controller

class EXAlgorithm(Algorithm):
    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
