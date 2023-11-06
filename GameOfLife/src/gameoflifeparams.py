from Framework.src.parameters import Parameters

class GameOfLifeParams(Parameters):
    def __init__(self, parallel=False) -> None:
        super().__init__(title="Game of life", parallel=parallel)