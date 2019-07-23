class classproperty:
    def __init__(self, function):
        self.function = function

    def __get__(self, owner_self, owner_class):
        return self.function(owner_class)


class Constants:
    @classproperty
    def BOARD_SIZE(cls):
        return 8




    

