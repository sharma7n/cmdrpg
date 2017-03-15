from dungeon import Dungeon

with Dungeon("Beginner's Forest", level=1, depth=3, monsters=[]) as d:
    d.explore()
