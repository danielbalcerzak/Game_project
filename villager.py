from NPCs import NPCs

items_list = ["bread", "meat", "cheese", "ale", "iguana on the stick"]
mn_gld = 10
mx_gld = 100
mn_itm = 1
mx_itm = 10
itm_cst = 10
repair_cst = 10
mx_health = 20


class Villager(NPCs):

    def __init__(self):
        super().__init__(items_list, mn_gld, mx_gld, mn_itm, mx_itm)
        self.set_max_health(mx_health)
        self.set_health(mx_health)
        self.name = "Villager"

    def show_items(self):
        return self.items

    def sell_item(self, item, someone):
        print(18 * "*", f" SELL ITEM ", 18 * "*", "\n")
        if item in self.items:
            if someone.gold >= itm_cst:
                someone.items.append(item)
                self.items.remove(item)
                someone.gold = someone.gold - itm_cst
                self.gold = self.gold + itm_cst
                print("{} buy {} for {} gold".
                      format(f"Stranger {someone.__class__.__name__}" if someone.name is None
                             else someone.name, item, itm_cst))
            else:
                print(f"You dont have enough money to buy {item}")
        else:
            print(f"{__class__.__name__} has no item in his inventory")

    def repair_armor(self, someone):
        print(18 * "*", f" REP ARMOR ", 18 * "*", "\n")
        if someone.gold >= repair_cst:
            someone.set_armor(int(someone.get_armor() / 4))
            someone.gold -= repair_cst
            self.gold += repair_cst
            print("{} armor has been repaired to {} points for {} gold".
                  format(f"Stranger {someone.__class__.__name__}" if someone.name is None
                         else someone.name, someone.get_armor(), repair_cst))
        else:
            print(f"You dont have {repair_cst} gold. Your cash is {someone.gold} gold")
