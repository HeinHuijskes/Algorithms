def makeDrawables(values, drawType):
    return [Drawable(value, drawType) for value in values]

def unMakeDrawables(drawables):
    return [drawable.value for drawable in drawables]

class Drawable():
    def __init__(self, value, drawType) -> None:
        self.value = value
        self.drawType = drawType
