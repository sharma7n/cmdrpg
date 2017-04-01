def autorepr(cls):
    """ Grants the decorated class a boilerplate __repr__ """
    
    class WithRepr(cls):
        def __repr__(self):
            return '<{clss} {attrs} at {id}>'.format(
                clss=cls.__name__,
                attrs=vars(self),
                id=id(self))
    
    WithRepr.__name__ = cls.__name__
    WithRepr.__doc__ = cls.__doc__
    
    return WithRepr