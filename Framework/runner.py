from ui import UI
from console import Console
from button import Button

class Runner():
    buttons: list[Button]
    def __init__(self, objects=None, parameters=None, buttons=None) -> None:
        self.objects = objects
        self.parameters = parameters
        self.buttons = buttons

    def run(self):
        console = Console(UI(), self.parameters)
        console.setObjects(self.objects)
        console.ui.setButtons(self.buttons)
        console.run()
