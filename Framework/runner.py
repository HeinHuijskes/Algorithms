from ui import UI
from Framework.controller import Controller
from button import Button

class Runner():
    buttons: list[Button]
    def __init__(self, drawables=None, parameters=None, buttons=None, inFieldAction=None) -> None:
        self.objects = drawables
        self.parameters = parameters
        self.buttons = buttons
        self.inFieldAction = inFieldAction

    def run(self):
        controller = Controller(UI(), self.parameters, self.inFieldAction)
        controller.setDrawables(self.objects)
        controller.ui.setButtons(self.buttons)
        controller.run()
