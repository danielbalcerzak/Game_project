import enemy
import hero
import mercenary
import villager
from rpg_func import struggle as fight


def show_infos(*persons):
    for person in persons:
        person.get_info()
        print(43*"#", '\n')


her = hero.Hero("Waldemar", "Knight")
enm = enemy.Enemy()
vil = villager.Villager()
merc = mercenary.Mercenary()

show_infos(her, enm, vil, merc)

fight(her, enm)
vil.sell_item("iguana on the stick", her)
vil.repair_armor(her)
fight(her, vil)
fight(her, merc)
