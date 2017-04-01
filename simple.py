from database import tinymodel, save, load


@tinymodel
class Holy:
    def __init__(self, *, dark=False, light=True):
        self.dark = dark
        self.light = light

@tinymodel
class Flare:
    def __init__(self, *, fire="FIRE"):
        self.fire = fire