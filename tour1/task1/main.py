#Imports section
import turtle
from turtle import *
import random

#---------------------------------------------
#INIT
wn = turtle.Screen() #Starting screen

# This turns off screen updates 
wn.tracer(0) 



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
UNIT = 28 #number of steps

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
    #placing objects
    placeObjects()
    #preparations to draw level
    penup()
    left(90)
    forward(len(level)/2*UNIT)
    left(90)
    forward(len(level[0])/2*UNIT)
    right(180)

    for line in enumerate(level):
        for symbol in enumerate(line[1]):
            if level[line[0]-1][symbol[0]] == 'X' and symbol[1] == 'X' and line[0] != 0:
                pendown()
                left(90)
                forward(UNIT)
                right(180)
                forward(UNIT)
                left(90)
                penup()
                try:
                    if level[line[0]][symbol[0]+1] == 'X':
                        pendown()
                        forward(UNIT)
                        penup()
                    else:
                        forward(UNIT)
                except:
                    forward(UNIT)
            elif symbol[1] == 'X':
                pendown()
                forward(UNIT)
                penup()
            elif symbol[1] == ' ':
                forward(UNIT)
            else:
                forward(UNIT)
        if level[line[0]][0] == 'X':
            try:
                right(90)
                # pendown()
                forward(UNIT)
                right(90)
                penup()
                forward(len(line[1])*UNIT)
                left(180)
            except:
                pass


drawLevel()

# Update the screen to see the changes   
wn.update() 




wn.tracer(1) 




# Keep the window open
wn.mainloop() 