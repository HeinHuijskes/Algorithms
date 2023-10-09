class Drawable():
    def __init__(self, value, drawType) -> None:
        self.value = value
        self.drawType = drawType

    def makeDrawable(value, drawType):
        return Drawable(value=value, drawType=drawType)

    def makeDrawables(values, drawType):
        return [Drawable.makeDrawable(value, drawType) for value in values]

    def unMakeDrawables(drawables):
        return [drawable.value for drawable in drawables]
