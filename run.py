from attr import asdict
from database import db, Player

from battler import Battler


res = db.search(Player.exists())
if res:
    print(res[0]['player'])
else:
    name = input("Enter your name: ")
    battler = Battler(name=name)
    db.insert({'player': asdict(battler)})