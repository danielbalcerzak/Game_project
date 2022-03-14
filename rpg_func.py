def fight(first, second):
    if not first.is_alive():
        print(f"{first.name} can't fight, becouse he's dead")
        return None
    elif not second.is_alive():
        print(f"{second.name} can't fight, becouse he's dead")
        return None
    while first.is_alive() and second.is_alive():
        first.atack(second)
        print(f"{second.name} has {second.get_health()} points of life")
        if second.is_alive():
            try:
                second.atack(first)
                print(f"{first.name} has {first.get_health()} points of life")
            except:
                pass
    if first.is_alive():
        print(f"\n{first.name} win.\n".upper())
        second.drop_gold(first)
        second.drop_items(first)
    else:
        print(f"\n{second.name} win.\n".upper())
        first.drop_gold(second)
        first.drop_items(second)


def struggle(good_hero, enemy, *moreofenemys):
    counter = 1
    print(20 * "*", f" FIGHT ", 20 * "*", "\n")
    fight(good_hero, enemy)
    for another in moreofenemys:
        if good_hero.is_alive():
            counter += 1
            print(20 * "*", f"{counter} FIGHT", 20 * "*", "\n")
            fight(good_hero, another)
        else:
            break
