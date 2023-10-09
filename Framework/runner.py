from ui import UI
from Framework.controller import Controller
from button import Button

class Runner():
    buttons: list[Button]
    def __init__(self, drawables=None, parameters=None, buttons=None) -> None:
        self.drawables = drawables
        self.parameters = parameters
        self.buttons = buttons

    def run(self):
        controller = Controller(UI(), self.parameters)
        controller.setDrawables(self.drawables)
        controller.ui.setButtons(self.buttons)
        controller.run()
