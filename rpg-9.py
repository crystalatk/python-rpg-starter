import random


class Character:
    def __init__(self, name, health, power, verb="is", verb_2="has", verb_3="does", ):
        self.name = name
        self.verb = verb
        self.verb_2 = verb_2
        self.verb_3 = verb_3
        self.health = health
        self.power = power

    def attack(self, enemy):
        if enemy.name != "Shadow":
            enemy.health -= self.power
        elif enemy.name == "Shadow":
            key_number = 3
            prob_number = random.randint(1, 10)
            if prob_number == key_number:
                enemy.health -= self.power
        if enemy.name == "Medic":
            key_number = 3
            prob_number = random.randint(1, 5)
            if prob_number == key_number:
                enemy.health += 2
        print("%s %s %d damage to %s." %
              (self.name, self.verb_3, self.power, enemy.name))
        if enemy.health <= 0:
            print(f"{enemy.name} {enemy.verb} dead.")

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("%s %s %d health and %d power." %
              (self.name, self.verb_2, self.health, self.power))


class Hero(Character):
    def __init__(self):
        super().__init__("You", 10, 5, "are", "have", "do")

    def attack(self, enemy):
        attack_double_key_number = 3
        key_number = random.randint(1, 5)
        if key_number == attack_double_key_number:
            self.power *= 2
        super().attack(enemy)


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, 6, 2)


class Zombie(Character):
    def __init__(self, name):
        super().__init__(name, 6, 2)

    def attack(self, enemy):
        super().attack(enemy)


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
