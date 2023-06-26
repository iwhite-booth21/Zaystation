
import random


class Status:
    def __init__(self, condition):
        self._condition = condition 
    
    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, new_condition):
        if new_condition != self._condition:
            self._condition = new_condition
        
    def increase_Cond(self, increment):
        self._condition += increment
        
    def decrease_Cond(self, decrement):
        self._condition -= decrement
        
    def get_cond_value(self):
        return str(self._condition)



class Enemy:
    def __init__(self, health, name, armor, status, level):
        self.health = health 
        self.name = name
        self.armor = armor
        self.status = status
        self.level = level
        
    @property
    def damage(self):
        return self.health
    
    @damage.setter
    def damage(self, new_health):
        if new_health != self.health:
            self.health = new_health
    def damage_taken(self, damage):
        self.health -= damage
        return self.health
    def get_health(self):
        return int(self.health)
    def attack(self, character):
        damage = random.randint(5, 45)  # Generate a random damage value
        character.damage_taken(damage)
        print(f"{self.name} attacks {character.name} for {damage} damage.")
        
        if character.health <= 0:
            print(f"{character.name} has been defeated!")
        
        return damage


class Character:
    def __init__(self, name,  race, current_level, health, ability, armor, status):
        self.name = name
        self.race = race
        self.current_level = current_level
        self.health = health
        self.ability = ability
        self.armor = armor 
        self.status = status
    
    @property
    def damage(self):
        return self.health
    
    @damage.setter
    def damage(self, new_health):
        if new_health != self.health:
            self.health = new_health
    def damage_taken(self, damage):
        self.health -= damage
        return self.health
    def get_health(self):
        return int(self.health)
    def attack(self, enemy):
        damage = random.randint(10, 50)  # Generate a random damage value
        enemy.damage_taken(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
        
        return damage
        

def combatMatrix(player, enemy):
    while player.health > 0 and enemy.health > 0:
        player_damage = player.attack(enemy)
        if enemy.health <= 0:
            break  # Enemy has been defeated, end combat
        
        enemy_damage = enemy.attack(player)
        if player.health <= 0:
            break  # Player has been defeated, end combat

        # Print the current health of player and enemy
        print(f"{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")
        print()
    
    if player.health > 0:
        print(f"{player.name} is victorious!")
    else:
        print(f"{enemy.name} is victorious!")



# main code area

Default_Characters = [
    Character("Eric the Barbarian", "Eldian", 25, 250, "Super Perception", "Ebony Armor", Status(2)),
    Character("Gladys the Healer", "Noble", 15, 150, "Party Heal", "Angel Fabric", Status(2)),
    Character("Edward Elric", "Alchemist Elite",75,350, "Transmute", "Tunic", Status(2)),
    Character("Jade the Battler", "Orc", 10, 75, "Bereserk", "Battle Grieves", Status(2)) 
    ]

Default_Enemies = [
    Enemy(200, "Goblin", "Wooden Armor", Status(1), 8),
    Enemy(200, "Hobgoblin", "Stone Armor", Status(1), 10),
    Enemy(200, "Homonculus", "Skin of dead", Status(1), 20),
    Enemy(200, "Bowser", "Spiky Shell", Status(1), 18)
]

## Characters

Eric = Default_Characters[0]
Gladys = Default_Characters[1]
Edward = Default_Characters[2]
Jade = Default_Characters[3]

## Enemies
Goblin = Default_Enemies[0]
Hobgoblin = Default_Enemies[1]
Homonculus = Default_Enemies[2]
Bowser = Default_Enemies[3]

print("Some Default Hero Statuses")
## View Character and Enemy Status
print("Eric's Status - " + Eric.status.get_cond_value())
print("Gladys Status - " + Gladys.status.get_cond_value())

print("Goblin's Status - " + Goblin.status.get_cond_value())
print("Bowser's Status - " + Bowser.status.get_cond_value())

## Test Increment and Decrement Health
print(Eric.damage_taken(15))
print(Homonculus.damage_taken(20))

combatRes = combatMatrix(Eric, Goblin)



