
class Thing:

    def __init__ ( self, key, value ):
        self.key = key
        self.value = value

    @property
    def yd_list ( self ):
        return [str(self.key), str(self.value)]


    def __str__ ( self ):
        return self.key + " " + self.value

class Thing2(Thing):

    def __init__ ( self, key, value, deeper_value ):
        super().__init__(key, value)
        self.deep_value = deeper_value

    def __str__ ( self ):
        return super().__str__() + self.deep_value

    @property
    def yd_list ( self ):
        return super().yd_list + [self.deep_value]
