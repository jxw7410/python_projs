class classproperty:
    def __init__(self, function):
        self.function = function

    def __get__(self, instance, cls):
        return self.function(cls)


class Const:
    @classproperty
    def BOARD_SIZE(cls):
        return 8


    @classproperty
    def DIAGONAL(cls):
        return 'DIAGONAL'

    @classproperty
    def ORTHAGONAL(cls):
        return 'ORTHOGONAL'

    
    @classproperty
    def ALL_DIRECTION(cls):
        return 'ALL_DIRECTION'

    @classproperty
    def WHITE(cls):
        return 'WHITE'

    @classproperty
    def BLACK(cls):
        return 'BLACK'