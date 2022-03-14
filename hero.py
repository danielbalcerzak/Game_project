from warrior import Warrior


class Hero(Warrior):

    def __init__(self, name=None, fraction=None):
        super().__init__(name, fraction)
        self.gold = 100
