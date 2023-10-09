from ui import UI
from Framework.controller import Controller
from button import Button

class Runner():
    buttons: list[Button]
    def __init__(self, objects=None, parameters=None, buttons=None) -> None:
        self.objects = objects
        self.parameters = parameters
        self.buttons = buttons

    def run(self):
        controller = Controller(UI(), self.parameters)
        controller.setObjects(self.objects)
        controller.ui.setButtons(self.buttons)
        controller.run()
