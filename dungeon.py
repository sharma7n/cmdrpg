import random


class Dungeon:
    def __init__(self, name, *, level=1, depth=1, monsters=None):
        self.name = name
        self.level = level
        self.depth = depth
        self.monsters = monsters if monsters else set()
        random.seed()
        
    def random_encounter(self):
        """ Produces a random monster from the dungeon at a set level. 
            May return None if a monster didn't appear or if there are no monsters. """
        
        ENCOUNTER_RATE = 0.5
        if random.random() < ENCOUNTER_RATE:
            template = random.choice(self.monsters) if self.monsters else None
            if template:
                return template.generate(level=self.level)
            else:
                return None
        else:
            return None
    
    def __enter__(self):
        return DungeonNode(self, prev=None)
    
    def __exit__(self, type_, value, traceback):
        pass

class DungeonNode:
    def __init__(self, dungeon, *, depth=1, prev=None):
        self.dungeon = dungeon
        self.depth = depth
        self.prev = prev
        self.cleared = False
    
    class CannotContinue(Exception):
        """ Exception raised when the player tries to continue from a node that has not yet been cleared. """
        pass
    
    def next(self):
        """ Gets the next dungeon node. """
        
        if not self.cleared:
            raise DungeonNode.CannotContinue("Cannot go to next room until the current room has been cleared!")
        else:
            if self.depth < self.dungeon.depth:
                return self.__class__(self.dungeon, depth=self.depth + 1, prev=self)
            else:
                return None
            
    def explore(self):
        """ Fight the monster, if it exists. """
        
        if not self.cleared:
            monster = self.dungeon.random_encounter()
            if monster:
                print("Encountered {}".format(monster))
            else:
                print("No encounter!")
            self.cleared = True
                
        next_ = self.next()
        if next_:
            next_.explore()
