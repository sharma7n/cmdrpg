from battler import Battler


class Monster:
    def __init__(self, battler, *, on_defeat=None):
        self.name = battler.name
        self.battler = battler
        self.on_defeat = on_defeat
    
    def clone(self):
        return self.__class__(self._battler, on_defeat=self._on_defeat)

class MonsterTemplate:
    def __init__(self, monster, *, allowed_level_ups=None):
        self.monster = monster
        self.allowed_level_ups = allowed_level_ups if allowed_level_ups else set()
    
    def generate(self, *, level=1):
        mon = self.monster.clone()
        if level:
            for _ in range(level):
                level_up = random.choice(self.allowed_level_ups)
                mon.battler.level_up(level_up)
