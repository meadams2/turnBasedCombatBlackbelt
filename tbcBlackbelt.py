"""Marianne Adams
CS120
Turn Based Combat Blackbelt
Character Module"""
import tbcModuleBlackbelt.py
def main():
    character1 = Character.makeCharacter()
    character2 = Character.makeCharacter()

def testInt(value, max, min, default = 0)
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

# def makeCharacter():
#     name = input("Please give your character a name.")
#     hitPoints = input("Please give your character some health stats. Enter a number.")
#     hitPoints = testIsNumeric(hitPoints)
#     hitPoints = testInt(hitPoints)
#     hitChance = input("How likely is your character to hit their opponent? Please enter a number from 1-100. ")
#     hitChance = testIsNumeric(hitChance)
#     hitChance = testInt(hitChance)
#     maxDamage = input("What is the max amount of damage your character can do? Please enter a number from 1-100")
#     maxDamage = testIsNumeric(maxDamage)
#     maxDamage = testInt(maxDamage)
#     armor = input("Does your character have any armor? How sturdy is it? Please enter a number from 1-10.")
#     armor = testIsNumeric(hitChance)
#     armor = testInt(armor)
#     return name, hitPoints, hitChance, armor, maxDamage

    
