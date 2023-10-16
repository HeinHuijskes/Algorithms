from Framework.src.parameters import Parameters

class TSMParameters(Parameters):
    def __init__(self) -> None:
        super().__init__(title="Travelling Salesman Algorithm")
    
    dots = 10
    updateTime = 50000
