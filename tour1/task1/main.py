#Imports section
import turtle
from turtle import Turtle, screensize
import random
from time import sleep

#---------------------------------------------
#INIT
wn = turtle.Screen() #Starting screen
wn.setup(1080, 560)

# This turns off screen updates 
wn.tracer(0) 

drawer = Turtle() #declaring our drawer of the level
writer = Turtle() #writer will write text
writer.penup()
writer.hideturtle()
writer.goto(screensize()[0]-screensize()[0]/4, screensize()[1]-screensize()[1]/0.6)
#---------------------------------------------
#Functions helpers

def replace(string, to, index):
    return string[:index] + to + string[index + 1:] #I took this part from stack overflow

def is_collided_with(player_coords:tuple, objects_coords:dict): #Taken from stack overflow and changed
    for i in range(len(objects_coords)):
        print(i)
        if abs(player_coords[0] - list(objects_coords.keys())[i][0]) < 10 and abs(player_coords[1] - list(objects_coords.keys())[i][1]) < 10:
            print(f'collision with {list(objects_coords.values())[i]}')
        else:
            print('no')

#---------------------------------------------
#Classes

class Player():
    def __init__(self) -> None:
        #declaring player's variables
        self.turtle_player = Turtle()
        self.inventory = []

        #applying all the properties I need to our turtle player
        self.turtle_player.showturtle()
        self.turtle_player.penup()
        self.turtle_player.speed(0)
    
    def TurtlePlayer(self) -> Turtle:
        return self.turtle_player
        
    def AddItemToInventory(self, item) -> None:
        self.inventory.append(item)
    
    def GetInventory(self) -> list:
        return self.inventory
    
    def CheckForWall(self, action: str) -> None:
        pass

    def CheckObjectCollision(self, objects_positions:dict) -> None:
        position_ = self.turtle_player.position()
        is_collided_with(position_,objects_positions)
    
    def left(self) -> None:
        # print('left')
        self.turtle_player.left(5)
        self.CheckForWall('left')
        self.CheckObjectCollision(positions)
    
    def right(self) -> None:
        # print('right')
        self.turtle_player.right(5)
        self.CheckForWall('right')
        self.CheckObjectCollision(positions)
    
    def forward(self) -> None:
        # print('forward')
        self.turtle_player.forward(3)
        self.CheckForWall('forward')
        self.CheckObjectCollision(positions)

    def back(self) -> None:
        # print('back')
        self.turtle_player.back(3)
        self.CheckForWall('back')
        self.CheckObjectCollision(positions)
    
    

    


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
                
                
                


positions = {}
#drawing level
def drawLevel():
    global positions
    #placing objects
    placeObjects()
    #preparations to draw level
    drawer.penup()
    drawer.left(90)
    drawer.forward(len(level)/2*UNIT)
    drawer.left(90)
    drawer.forward(len(level[0])/2*UNIT)
    drawer.right(180)

    positions = {} #a dict for positions of objects

    for line in enumerate(level):
        for symbol in enumerate(line[1]):
            if level[line[0]-1][symbol[0]] == 'X' and symbol[1] == 'X' and line[0] != 0:
                drawer.pendown()
                drawer.left(90)
                drawer.forward(UNIT)
                drawer.right(180)
                drawer.forward(UNIT)
                drawer.left(90)
                drawer.penup()
                try:
                    if level[line[0]][symbol[0]+1] == 'X':
                        drawer.pendown()
                        drawer.forward(UNIT)
                        drawer.penup()
                    else:
                        drawer.forward(UNIT)
                except:
                    drawer.forward(UNIT)
            elif symbol[1] == 'X':
                drawer.pendown()
                drawer.forward(UNIT)
                drawer.penup()
            elif symbol[1] == ' ':
                drawer.forward(UNIT)
            else:
                drawer.write(symbol[1])
                drawer.forward(UNIT/2)
                positions[drawer.pos()] = symbol[1]
                drawer.forward(UNIT/2)
        if level[line[0]][0] == 'X':
            try:
                drawer.right(90)
                # pendown()
                drawer.forward(UNIT)
                drawer.right(90)
                drawer.penup()
                drawer.forward(len(line[1])*UNIT)
                drawer.left(180)
            except:
                pass

    print(positions)


drawLevel()
drawer.hideturtle()

# Update the screen to see the changes   
wn.update() 

#declaring player
wn.tracer(1)

player = Player()


#listening to player controls
wn.onkeypress(player.forward, 'w')
wn.onkeypress(player.back, 's')
wn.onkeypress(player.left, 'a')
wn.onkeypress(player.right, 'd')
wn.listen()

# Keep the window open
wn.mainloop() 
