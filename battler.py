import attr


@attr.s
class Depletable:
    """ Represents a quantity that can be decreased to 0 and increased to a max. """
    
    _value = attr.ib(default=10)
    
    def __attrs_post_init__(self):
        self._max = self._value
        self._current = self._value
    
    def get(self):
        return self._current
    
    def set(self, value):
        if value > self._max:
            self._current = self._max
        elif value < 0:
            self._current = 0
        else:
            self._current = value

@attr.s
class Battler:
    name = attr.ib()
    level = attr.ib(default=1)
    _hp = attr.ib(default=10)
    
    def __attrs_post_init__(self):
        self._dhp = Depletable(value=self._hp)
    
    @property
    def hp(self):
        return self._dhp.get()
    
    @hp.setter
    def hp(self, value):
        self._dhp.set(value)