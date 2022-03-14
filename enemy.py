from NPCs import NPCs
import random

items_list = ["bread", "meat", "magic scroll", "book", "new armor"]
mn_gld = 10
mx_gld = 500
mn_itm = 1
mx_itm = 4
mn_hth = 80
mx_hth = 120
mn_perk = 1
mx_perk = 12


class Enemy(NPCs):

    def __init__(self):
        super().__init__(items_list, mn_gld, mx_gld, mn_itm, mx_itm)
        self.set_max_health(random.randint(mn_gld, mx_hth))
        health = self.get_max_health()
        self.set_health(health)
        self.name = "Stranger"
        self.__strength = random.randint(mn_perk, mx_perk)
        self.__condition = random.randint(mn_perk, mx_perk)
        self.__intelligence = random.randint(mn_perk, mx_perk)

    def atack_power(self):
        normal = round(self.luck(1, 12) + (0.4 * self.__strength) + (0.2 * self.__condition))
        return normal

    def defence_power(self):
        defence_power = round(self.luck(1, 4) + (0.4 * self.__condition) + (0.2 * self.__intelligence))
        return defence_power

    def get_info(self):
        super().get_info()
        print('{:>12} {:<10}'.format('Strength:', self.__strength))
        print('{:>12} {:<10}'.format('Condition:', self.__condition))
        print('{:>12} {:<10}'.format('Inteligence:', self.__intelligence))

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
