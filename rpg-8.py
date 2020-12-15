class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))


class Hero(Character):
    def __init__(self):
        super().__init__(10, 5)

    def attack(self, enemy):
        super().attack(enemy)
        print("You do %d damage to the zombie." % self.power)
        if enemy.health <= 0:
            print("The zombie is dead...but zombies are always dead! Mwahahahah!")


class Goblin(Character):
    def __init__(self, health=6, power=2):
        super().__init__(6, 2)

    def attack(self, enemy):
        super().attack(enemy)
        print("The goblin does %d damage to you." % self.power)
        if enemy.health <= 0:
            print("You are dead.")


class Zombie(Character):
    def __init__(self, health=6, power=2):
        super().__init__(6, 2)

    def attack(self, enemy):
        super().attack(enemy)
        print("The zombie does %d damage to you." % self.power)
        if enemy.health <= 0:
            print("You are dead.")

    def alive(self):
        if self.health > 0:
            return True
        else:
            print("Bahaha! Zombies never die!")
            return True


def main():
    hero = Hero()
    goblin = Goblin()
    zombie = Zombie()

    while zombie.alive() and hero.alive():
        hero.print_status
        zombie.print_status
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(zombie)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
        # Goblin attacks hero
        zombie.attack(hero)


main()
