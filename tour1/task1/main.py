#Imports section
from turtle import *
import random
from time import sleep

#---------------------------------------------
#Functions helpers

def replace(string, to, index):
    return string[:index] + to + string[index + 1:] #I took this part from stack overflow

#---------------------------------------------
#Classes

class Player():
    def __init__(self) -> None:
        self.inventory = []
        
    def AddItemToInventory(self, item):
        self.inventory.append(item)
    
    def GetInventory(self):
        return self.inventory


#---------------------------------------------
#Level Creation:
#W - means washing machine
#X - means wall
#C - means dirty clothes
#P - means washing powder
#F - means flavoring agent

objects = ['W', 'C', 'P', 'F']

#All the objects will be placed in random positions
level = ["XXXXXXXXXXXXXXXX",
        "X        X     X",
        "X        X     X",
        "XXXXX  XXXXX  XX",
        "X              X",
        "XXXXXXXXXXXX  XX",
        "X      X       X",
        "X      X       X",
        "X              X",
        "X              X",
        "XXXXXXXXXXXXXXXX"]


#Making variable objects work with all kind of levels
for line in level:
    for symbol in line:
        if symbol == ' ':
            objects.append(' ')
for i in range(4):
    objects.pop()


#declaring UNIT constant that we'll use to draw level
UNIT = 10 #number of steps

#placing objects in random positions
def placeObjects():
    for line in enumerate(level):
        for symbol in enumerate(line[1]):
            if symbol[1] == ' ':
                try:
                    objectToAdd = random.randint(0,len(objects)-1)
                except:
                    break
                level.insert(line[0], replace(level[line[0]], objects[objectToAdd], symbol[0]))
                level.pop(line[0]+1)
                
                objects.pop(objectToAdd)
                
                
                



#drawing level
def drawLevel():
    placeObjects()
    penup()
    for line in level:
        for symbol in line:
            pass


placeObjects()
for i in level:
    print(i)

