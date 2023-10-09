from ui import UI
from console import Console

from uiparams import parameters as uiparams

class Runner():
    def __init__(self, objects=None, params=None, buttons=None) -> None:
        self.objects = objects
        self.params = params
        self.buttons = buttons

    def setup(self):
        for button in self.buttons:
            for key in uiparams["buttons"].keys():
                if key not in button.keys():
                    button[key] = uiparams["buttons"][key]
        self.params["buttons"] = self.buttons

    def run(self):
        self.setup()
        console = Console(UI(), self.params)
        console.setObjects(self.objects)
        console.run()
