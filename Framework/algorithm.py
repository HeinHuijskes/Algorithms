from controller import Controller

class Algorithm():
    def __init__(self, controller: Controller) -> None:
        self.controller = controller

    def log(self, text):
        self.controller.ui.log(text)
