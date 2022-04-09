from math import *
import random

level = input("Enter the level of your pokemon: ")
attack = input("Enter the Attack/Special Attack stat of your pokemon: ")
defense = input("Enter the Defense/Special Defense stat of the enemies pokemon: ")
power = input("Enter the number of power move of your pokemon: ")
targets = 1
weather = 1
badge = 1
critical = 1
random1 = random.uniform(0.85, 1)
STAB = 1
Type = 0.5
burn = 1
other = 1

modifier = float(targets) * float(weather) * float(badge) * float(critical) * float(random1) * float(STAB) * float(Type) * float(burn) * float(other)
damage = ((((2 * float(level) / 5) + 2) * float(power) * float(attack) / float(defense) / 50) + 2) * modifier
print(round(damage) , " attack damage deal!")