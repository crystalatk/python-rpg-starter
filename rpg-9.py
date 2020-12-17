import random
from character_classes import Character, Hero, Enemy, Zombie

enemy_list = ["Goblin", "Medic", "Shadow", "Zombie"]
main_menu = ["Fight", "Do Nothing", "Flee"]


def menu(menu_type):
    print("\n***What do you want to do?***")
    for idx, item in enumerate(menu_type):
        print(f"{idx+1}: {item}")
    choice_made = input()
    return choice_made


def main():
    hero = Hero()
    goblin = Enemy("Goblin")
    medic = Enemy("Medic")
    shadow = Enemy("Shadow")
    zombie = Zombie("Zombie")

    while goblin.alive() and hero.alive():
        hero.print_status
        goblin.print_status
        user_input = menu(main_menu)
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)


main()
