from random import *

#Code below is the skeleton for a menu generator.

#Create the 3 lists of words you want to choose from.

#Create a sides_selected list

for x in range(2):

    #Generates a random integer.
    x = randint(0, len(side)-1)
    sides_selected.append(side[x])

print("sides: ", sides_selected)

#Generates a random integer.
x = randint(0, len(main)-1)
print("main: ", main[x])

x = randint(0, len(dessert)-1)
print("dessert: ", dessert[x])
