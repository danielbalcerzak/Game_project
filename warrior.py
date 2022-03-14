import random


class Warrior:

    def __init__(self, name=None, fraction=None):
        self.__fraction = fraction
        self.name = name
        self.items = []
        self.gold = 0
        if fraction == 'Knight':
            self.__max_health = 120
            self.__health = self.__max_health
            self.__max_armor = 30
            self.__armor = self.__max_armor
            self.__strength = 12
            self.__condition = 7
            self.__intelligence = 7
        elif fraction == 'Druid':
            self.__max_health = 90
            self.__health = self.__max_health
            self.__max_armor = 10
            self.__armor = self.__max_armor
            self.__strength = 8
            self.__condition = 14
            self.__intelligence = 13
        elif fraction == 'Priest':
            self.__max_health = 90
            self.__health = self.__max_health
            self.__max_armor = 10
            self.__armor = self.__max_armor
            self.__strength = 8
            self.__condition = 14
            self.__intelligence = 13
        else:
            self.__max_health = 100
            self.__health = self.__max_health
            self.__max_armor = 30
            self.__armor = self.__max_armor
            self.__strength = 9
            self.__condition = 10
            self.__intelligence = 9

    @staticmethod
    def luck(mini=1, maxi=6):
        return random.randint(mini, maxi)

    def atack_power(self):
        normal = round(self.luck(1, 12) + (0.4 * self.__strength) + (0.2 * self.__condition))
        return normal

    def defence_power(self):
        defence_power = round(self.luck(1, 4) + (0.4 * self.__condition) + (0.2 * self.__intelligence))
        return defence_power

    def get_info(self):
        print(18 * '-', "INFOS", 18 * '-')
        if self.__fraction is None:
            print("{} is a {} and has no fraction".format
                  ("Stranger" if self.name is None else self.name, __class__.__name__, ))
        else:
            print("{} is a {} and is in {} fraction".format
                  ("Stranger" if self.name is None else self.name, __class__.__name__, self.__fraction))
        print(18 * '-', "STATS", 18 * '-')
        print('{:>12} {:<10}'.format("Gold:", self.gold))
        print('{:>12} {}'.format("Items:", self.items))
        print('{:>12} {:<10} / {}'.format('Health:', self.__health, self.__max_health))
        print('{:>12} {:<10} / {}'.format('Armor:', self.__armor, self.__max_armor))
        print('{:>12} {:<10}'.format('Strength:', self.__strength))
        print('{:>12} {:<10}'.format('Condition:', self.__condition))
        print('{:>12} {:<10}'.format('Inteligence:', self.__intelligence))

    def is_alive(self):
        if self.__health > 0:
            return True

    def get_armor(self):
        return self.__armor

    def set_armor(self, value):
        self.__armor += value
        if self.__armor > self.__max_armor:
            self.__armor = self.__max_armor

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health += value
        if self.__health > self.__max_health:
            self.__health = self.__max_health

    def drop_gold(self, x):
        pass

    def drop_items(self, x):
        pass

    def atack(self, someone):

        power = self.atack_power()
        hit_points = 0
        val = 0
        while someone.get_health() > 0 and val != power:
            try:
                if (self.luck() % 2) or someone.get_armor() <= 0:
                    someone.set_health(-1)
                    hit_points += 1
                else:
                    someone.set_armor(-1)
            except:
                someone.set_health(-1)
                hit_points += 1
            finally:
                val += 1

        print(f"{self.name} atacked {someone.name} with {power} points of power and took {hit_points}")

    def eat_and_drink(self, item):
        if item not in self.items:
            print(f"{self.name} don't have an item {item} in inventory")
        else:
            self.items.remove(item)
            self.set_health(self.get_health() / 4)
