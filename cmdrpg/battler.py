from tinymodel import model

from utils import autorepr


@autorepr
@model
class Depletable:
    """ A quantity that ranges from 0 to a maximum value. """
    
    def __init__(self, *, max=10, current=10):
        self._max = max
        self._current = min(current, max)
    
    def get(self):
        return self._current
        
    def set(self, value):
        """ Set the value within the range [0, max]. """
        
        if value > self._max:
            self._current = self._max
        elif value < 0:
            self._current = 0
        else:
            self._current = value

@autorepr
@model
class Battler:
    """ An entity that has HP and can attack and be attacked. """
    
    def __init__(self, *, hp=Depletable(max=10, current=10)):
        self._hp = hp
    
    @property
    def hp(self):
        return self._hp.get()
    
    @hp.setter
    def hp(self, value):
        return self._hp.set(value)
    
    def attack(self, target):
        """ Deals damage to target battler. """
        target.hp -= 1