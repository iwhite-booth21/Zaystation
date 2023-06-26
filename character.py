#Lets Try a Number System for Character Conditions
from character import Character, player_status




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
    def __init__(self, health, armor, status, level):
        self.health = health 
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


class Character:
    def __init__(self, name,  race, current_level, health, ability, armor, status):
        self.name = name
        self.race = race
        self.current_level = current_level
        self.health = health
        self.ability = ability
        self.armor = armor 
        self.status = status
        


# main code area

Default_Characters = [
    Character("Eric the Barbarian", "Eldian", 25, 100, "Super Perception", "Ebony Armor", player_status),
    Character("Gladys the Healer", "Noble", 15, 95, "Party Heal", "Angel Fabric", player_status),
    Character("Edward Elric", "Alchemist Elite",75,100, "Transmute", player_status),
    Character("Jade the Battler", "Orc", 10, 85, "Bereserk", "Battle Grieves", player_status) 
    ]

Default_Enemies = [
    
]

Eric = Default_Characters[0]
Gladys = Default_Characters[1]
Edward = Default_Characters[2]
Jade = Default_Characters[3]


Enemy_Status = Status(3)
Gogoblin = Enemy(100,"Armor of thorns", Enemy_Status, 8)
print(Gogoblin.damage_taken(20))

player_status = Status(5)      
BillyBob = Character("Jerry", "Brenton", 5, 100, "Fire Fist", "None", player_status)
print(BillyBob.status.get_cond_value())


player_status.decrease_Cond(1)
BillyBob = Character("Brenton", 5, 100, "Fire Fist", "None", player_status)
print(BillyBob.status.get_cond_value())
