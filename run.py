from attr import asdict
from tinydb import TinyDB, Query

from battler import Battler


Player = Query()
res = db.search(Player.player.exists())
if res:
    print(res)
else:
    name = input("Enter your name: ")
    battler = Battler(name=name)
    db.insert({'player': battler.asdict()})