from cmdrpg import Depletable


def test_instantiation():
    dep1 = Depletable()
    assert dep1.get() == 10
    
    dep2 = Depletable(max=5)
    assert dep2.get() == 5
    
    dep3 = Depletable(current=15)
    assert dep3.get() == 10
    
    dep4 = Depletable(max=10, current=9)
    assert dep4.get() == 9
    
    dep5 = Depletable(max=9, current=9)
    assert dep5.get() == 9
    
    dep6 = Depletable(max=9, current=10)
    assert dep6.get() == 9

def test_set():
    dep = Depletable()
    
    dep.set(-1)
    assert dep.get() == 0
    
    dep.set(0)
    assert dep.get() == 0
    
    dep.set(5)
    assert dep.get() == 5
    
    dep.set(10)
    assert dep.get() == 10
    
    dep.set(11)
    assert dep.get() == 10