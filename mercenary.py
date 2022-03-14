from warrior import Warrior


class Mercenary(Warrior):

    def __init__(self, name="Stranger", fraction=None):
        super().__init__(name, fraction)
        self.gold = 10

    def set_health(self, value):
        pass

    def eat_and_drink(self, item):
        pass

    def drop_gold(self, someone):
        print("Enemy drops {} golds coin".format(self.gold))
        someone.gold += self.gold
        self.gold = 0

    def drop_items(self, someone):
        print("Enemy drops {}".format(self.items))
        for items in self.items:
            someone.items.append(items)
        self.items = []
