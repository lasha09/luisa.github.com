#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
name = ["amber","jelly","elanor","paola", "imani", "estella","ms.c","ms.elizabeth", "sam"]
namelist= ""

for x in range (2):
    #Generates a random number
    x=randint(0, len(name)-1)
    namelist +=name[x] + "  "
print(namelist)
