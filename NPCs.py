import random

items_list = []
min_gold = 10
max_gold = 15
min_item = 1
max_item = 2
min_luck = 1
max_luck = 6


class NPCs:

    def __init__(self, lst=None, min_gol=min_gold, mx_gol=max_gold, min_it=min_item, mx_it=max_item):
        if lst is None:
            lst = items_list
        self.name = None
        self.__max_health = 10
        self.__health = self.__max_health
        self.gold = random.randint(min_gol, mx_gol)
        self.items = random.choices(lst, k=random.randint(min_it, mx_it))

    def get_info(self):
        print(18 * '-', "INFOS", 18 * '-')
        print(f"{self.name} is an {__class__.__name__}")
        print(18*'-', "STATS", 18*'-')
        print('{:>12} {:<10}'.format("Gold:", self.gold))
        print('{:>12} {}'.format("Items:", self.items))
        print('{:>12} {:<10} / {}'.format('Health:', self.__health, self.__max_health))

    def is_alive(self):
        if self.__health > 0:
            return True

    @staticmethod
    def luck(mini=min_luck, maxi=max_item):
        return random.randint(mini, maxi)

    def set_max_health(self, value):
        self.__max_health = value

    def get_max_health(self):
        return self.__max_health

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health += value
        if self.__health > self.__max_health:
            self.__health = self.__max_health

    def drop_gold(self, someone):
        print(f"Villager drop {self.gold} golds coin")
        someone.gold += int(self.gold / 10)
        self.gold = 0

    def drop_items(self, someone):
        print(f"Villager drop {self.items}")
        item = random.sample(self.items, 1)
        someone.items.append(item)
        self.items = []
