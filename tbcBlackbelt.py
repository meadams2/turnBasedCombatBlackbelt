"""Marianne Adams
CS120
Turn Based Combat Blackbelt
Character Module"""
import random
def main():
    hero = Character()
    hero.name = "Dan the Magical Cheese Wizard"
    hero.hitPoints = 10
    hero.hitChance = 42
    hero.maxDamage = 5
    hero.armor = 2
    villain = Character("Michael", 10, 22, 5, 2)
    hero.printStats()
    villain.printStats()
    fight(hero, villain)

class Character(object):
    def __init__(self, name = "Bobby John Jones", hitPoints = 12, hitChance = 13, maxDamage = 3, armor=2):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    def testInt(self, value, min = 0, max = 100, default =0):
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value
                else:
                    print("Too large.")
            else:
                print("Too small.")
        else:
            print("Must be an integer.")
        return out
    
    def printStats(self):
        print(f"""{self.name}
HP: {self.hitPoints}
Hit Chance: {self.hitChance}
Max Damage: {self.maxDamage}
Armor: {self.armor}""")
   
   @property
   def name(self):
       return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        return self.__name
    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, hitChance):
        self.__hitChance = self.testInt(value, 0, 100, 20)
        return self.__hitChance
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            self.__hitPoints = value
        else:
            print("HP must be a number.")
            self.__hitPoints = 10
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = self.testInt(value, 0, 1000, 2)
        return self.__maxDamage
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = self.testInt(value, 0, 1000, 0)
        return self.__armor
    
    def hit(self, enemy):
        if random.randrange(1, 100) <= self.hitChance:
            hitDamage = random.randrange(0, self.maxDamage)
            print(f"""{self.name} hits {enemy.name} for {hitDamage} damage.
{enemy.name}'s armor blocks damage for {enemy.armor} points.""")
            hitDamage -= enemy.armor
            if hitDamage < 0:
                hitDamage = 0
            enemy.hitPoints -= hitDamage
            print(f"{enemy.name}: {enemy.hitPoints} HP")
        else:
            hitDamage = 0
            print(f"{self.name} misses. No damage.")
        return enemy.hitPoints

def fight(character1, character2):
    character1.hit(character2)
    character2.hit(character1)
    keepGoing = True
    while keepGoing:
        if character2.hitPoints <= 0:
            print(f"""{character2.name}:{character2.hitPoints} HP
{character2.name} dies""")
            keepGoing = False
        elif character1.hitPoints <=0:
            print(f"""{character1.name}:{character1.hitPoints} HP
{character1.name} dies.""")
            keepGoing = False
        else:
            character2.hit(character1)
            character1.hit(character2)
main()
    
            
            

        