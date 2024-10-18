"""CS120 Turn Based Combat Blackbelt
Character & Fight Module"""
import random

def main():
    villain = Character("Villain", 10, 10, 5, 0)
    hero = Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    hero.printStats()
    villain.printStats()
    fight(hero, villain)
    
class Character(object):
    def __init__(self, name = "Dan the Magical Cheese Wizard", hitPoints = 10, hitChance = 50, maxDamage = 5, armor = 0):
        super().__init__()
        self.name = name
        self.maxDamage = maxDamage
        self.hitChance = hitChance
        self.hitPoints = hitPoints
        self.armor = armor
    def testIsNumeric(value):
        if value.isnumeric():
            value = int(value)
        else:
            print("You dunce. Your value must be a number.")
            value = 2
        return value

    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default """
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
        return out
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        return self.__name
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = self.testInt(value, 0, 10000, 1)
        return self.__maxDamage
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value)==int:
            self.__hitPoints = value
        else:
            print("HP must be an integer.")
            self.__hitPoints = 10
        return self.__hitPoints
            
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = self.testInt(value, 0, 100, 0)
        return self.__hitChance
            
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = self.testInt(value, 0, 1000, 0)
        return self.__armor
        
    def printStats(self):
        print(f"""{self.name}

HP: {self.hitPoints}
Hit Chance: {self.hitChance}
Max Damage: {self.maxDamage}
Armor: {self.armor}""")
          
    def hit(self, enemy):
        if random.randrange(1,100) <= self.hitChance:
            hitDamage = random.randrange(1, self.maxDamage)
            print(f"{self.name} hits {enemy.name} for {hitDamage} damage")
            print(f"{enemy.name}'s armor absorbs {enemy.armor} points")
            hitDamage -= enemy.armor
            if hitDamage < 0:
                hitDamage = 0
            enemy.hitPoints -= hitDamage
            print(f"{enemy.name}: {enemy.hitPoints}")
        else:
            hitDamage = 0
            print(f"{self.name} misses. No damage.")
        
        return enemy.hitPoints
    
    def makeCharacter(self):
        name = input("Please give your character a name.")
        hitPoints = input("Please give your character some health stats. Enter a number.")
        hitPoints = self.testIsNumeric(hitPoints)
        hitPoints = self.testInt(hitPoints)
        hitChance = input("How likely is your character to hit their opponent? Please enter a number from 1-100. ")
        hitChance = self.testIsNumeric(hitChance)
        hitChance = self.testInt(hitChance)
        maxDamage = input("What is the max amount of damage your character can do? Please enter a number from 1-100")
        maxDamage = self.testIsNumeric(maxDamage)
        maxDamage = self.testInt(maxDamage)
        armor = input("Does your character have any armor? How sturdy is it? Please enter a number from 1-10.")
        armor = self.testIsNumeric(hitChance)
        armor = self.testInt(armor)
        
        return name, hitPoints, hitChance, armor, maxDamage
    

    
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