class Battler:
    def __init__(self, name, level=1, experience=0, hp=10, mp=10, attack=1, defense=1, magic=1, speed=1):
        self.name = name
        self._level = level
        self.experience = experience
        self._maxhp = self._curhp = hp
        self._maxmp = self._curmp = mp
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
    
    @property
    def level(self):
        return self._level
    
    def __repr__(self):
        return '<{cls} {name} HP: {hp} / {maxhp}, MP: {mp} / {maxmp} at {id}>'.format(
                cls=self.__class__.__name__, name=self.name,
                hp=self.hp, maxhp=self._maxhp, mp=self.mp, maxmp=self._maxmp,
                id=id(self))
    
    @property
    def hp(self):
        return self._curhp
    
    @hp.setter
    def hp(self, value):
        if value > self._maxhp:
            self._curhp = self._maxhp
        elif value < 0:
            self._curhp = 0
        else:
            self._curhp = value
    
    @property
    def mp(self):
        return self._curmp
    
    @mp.setter
    def mp(self, value):
        if value > self._maxmp:
            self._curmp = self._maxmp
        elif value < 0:
            self._curmp = 0
        else:
            self._curmp = value

    def level_up(self, levelup):
        self._level += 1
        self._maxhp += levelup.hp
        self._maxmp += levelup.mp
        self.attack += levelup.attack
        self.defense += levelup.defense
        self.magic += levelup.magic
        self.speed += levelup.speed

class LevelUp:
    def __init__(self, name, hp=0, mp=0, attack=0, defense=0, magic=0, speed=0):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed

