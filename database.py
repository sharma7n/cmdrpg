from tinydb import TinyDB, Query


db = TinyDB("rpg.json")

def tinymodel(cls):
    """ 
        Decorates a class to be compatible with the `save` and `load` functions.
        Returned class has __repr__ and de/serialization methods.
        Returned class also has the name of the original class.
    """
    
    class TinyModel(cls):
        def __repr__(self):
            return "<{cls} {attrs} at {id}>".format(
                cls=self.__class__.__name__,
                attrs=self.asdict(),
                id=id(self))
        
        def asdict(self):
            return self.__dict__
        
        @classmethod
        def fromdict(cls, json):
            return cls(**json)
            
    TinyModel.__name__ = cls.__name__
    return TinyModel

def save(instance):
    """ Inserts or updates instance into its database table. """
    
    table = db.table(instance.__class__.__name__)
    table.insert(instance.asdict())
        
def load(cls, *, where=None, create_if_none_callback=None):
    """ Returns records for a specific class. """
    
    table = db.table(cls.__name__)
    
    if where:
        result = table.search(where(Query()))
    else:
        result = table.all()
    
    if len(result) > 0:
        return (cls.fromdict(item) for item in result)
    else:
        if not create_if_none_callback:
            return None
        else:
            return create_if_none_callback()