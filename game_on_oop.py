player_health = int(input(" Player Health:"))
player_damage = int(input(" Player Damage:"))
player_armor = int(input(" Player Armor:"))

enemy_health = int(input(" Enemy Health:"))
enemy_damage = int(input(" Enemy Damage:"))
enemy_armor = int(input(" Enemy Armor:"))


class Person:
    # Creates a main class that specifies common parameters for the player and the enemy
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor


class Player:
    # Creates a class that inherits from the main class, this class describes the player's health and damage armor
    def __init__(self, health, damage, armor):
        Person.__init__(self, health, damage, armor)

    def attack(self):
        damage = self.damage

        enemy.protection(damage)

    def protection(self, damage):
        health = self.health
        armor = self.armor

        health -= damage - armor

        self.health = health

    def ex_health(self):
        if self.health < 0:
            return True
        else:
            return False


class Enemy:
    # Creates a class that inherits from the main class. In this class, armor, health, and enemy damage are described
    def __init__(self, health, damage, armor):
        Person.__init__(self, health, damage, armor)

    def attack(self):
        damage = self.damage

        player.protection(damage)

    def protection(self, damage):
        health = self.health
        armor = self.armor

        health -= damage - armor

        self.health = health

    def ex_health(self):
        if self.health < 0:
            return True
        else:
            return False


player = Player(player_health, player_damage, player_armor)
enemy = Enemy(enemy_health, enemy_damage, enemy_armor)

x = 1


class Game:
    # Makes the class of the game itself their attack on a friend of a friend, etc
    def ex_game():
        if player.ex_health() == True:
            return 'ENEMY WIN!'
        elif enemy.ex_health() == True:
            return 'PLAYER WIN!'
        else:
            return True

    def game():
        global x

        ex_win = game.ex_game()

        if ex_win == True:

            if x == 1:
                player.attack()
                x -= 1
            else:
                enemy.attack()
                x += 1
            return True
        else:
            return ex_win


game = Game

gamewin = game.game()

while gamewin == True: # Makes it all infinite to get 0 at the end
    gamewin = game.game()


print(gamewin)
