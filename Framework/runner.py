from ui import UI
from console import Console
from button import Button

from uiparams import parameters as uiparams

class Runner():
    buttons: list[Button]
    def __init__(self, objects=None, params=None, buttons=None) -> None:
        self.objects = objects
        self.params = params
        self.buttons = buttons

    def run(self):
        self.params["buttons"] = self.buttons
        console = Console(UI(), self.params)
        console.setObjects(self.objects)
        console.run()
