from cmdrpg import Depletable, Battler


def test_direct_set():
    bat = Battler()
    
    bat.hp = 5
    assert bat.hp == 5
    
    bat.hp = -1
    assert bat.hp == 0
    
    bat.hp = 11
    assert bat.hp == 10

def test_taking_damage():
    bat = Battler()
    
    bat.hp -= 1
    assert bat.hp == 9
    
    bat.hp -= 4
    assert bat.hp == 5
    
    bat.hp -= 9
    assert bat.hp == 0

def test_healing():
    bat = Battler(hp=Depletable(max=10, current=0))
    
    bat.hp += 1
    assert bat.hp == 1
    
    bat.hp += 4
    assert bat.hp == 5
    
    bat.hp += 9
    assert bat.hp == 10

def test_attack():
    attacker = Battler(hp=Depletable(max=10, current=10))
    defender = Battler(hp=Depletable(max=10, current=10))
    
    attacker.attack(defender)
    assert defender.hp == 9
    
    defender.hp = 0
    attacker.attack(defender)
    assert defender.hp == 0