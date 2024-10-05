#Imports section
import turtle
from turtle import Turtle, screensize
import random
from time import sleep

#---------------------------------------------
#INIT
wn = turtle.Screen() #Starting screen
wn.setup(1080, 560)


drawer = Turtle() #declaring our drawer of the level
writer = Turtle() #writer will write text

#---------------------------------------------
#Functions helpers

def replace(string, to, index):
    return string[:index] + to + string[index + 1:] #I took this part from stack overflow

def is_collided_with(player_coords:tuple, objects_coords:dict) -> str | None: #Taken from stack overflow and changed
    for i in range(len(objects_coords)):
        if abs(player_coords[0] - list(objects_coords.keys())[i][0]) < 15 and abs(player_coords[1] - list(objects_coords.keys())[i][1]) < 15:
            return list(objects_coords.values())[i]
    return None

def erase_text(player:Turtle, font_size=5):
    wn.tracer(0)
    player.color(wn.bgcolor())
    player.write('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛', align='center', font=("Arial", font_size, "normal"))
    player.forward(5)
    player.write('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛', align='center', font=("Arial", font_size, "normal"))
    player.back(5)
    player.left(90)
    player.forward(12)
    player.right(90)

    player.write('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛', align='center', font=("Arial", font_size, "normal"))
    player.forward(5)
    player.write('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛', align='center', font=("Arial", font_size, "normal"))
    player.back(5)

    player.left(90)
    player.back(12)
    player.right(90)
    player.pencolor('black')
    wn.tracer(1)


#---------------------------------------------
# Explaining game
writer.write('Hi there!', align='center', font=('Arial', 20, 'normal'))
sleep(2)
erase_text(writer, 10)
writer.write('At this game, you need to take all the things...', align='center', font=('Arial', 20, 'normal'))
sleep(5)
erase_text(writer, 10)
writer.write('...and give them to the washing machine.', align='center', font=('Arial', 20, 'normal'))
sleep(4)
erase_text(writer, 10)
writer.write('Good luck!', align='center', font=('Arial', 20, 'normal'))
sleep(2)
erase_text(writer, 10)


#putting writer in the position
writer.penup()
writer.hideturtle()
writer.goto(screensize()[0]-screensize()[0]/2.5, screensize()[1]-screensize()[1]/0.6)

# This turns off screen updates 
wn.tracer(0) 

#---------------------------------------------
#Classes

class Player():
    def __init__(self) -> None:
        #declaring player's variables
        self.turtle_player = Turtle()
        self.inventory = []
        self.inv_phrase = 'Inventory: '
        self.given_to_machine = []

        #applying all the properties I need to our turtle player
        self.turtle_player.showturtle()
        self.turtle_player.penup()
        self.turtle_player.speed(0)
        
    
    def player(self) -> Turtle:
        return self.turtle_player
        
    
    def get_inventory(self) -> list:
        return self.inventory
    
    def check_for_wall(self, action: str) -> None:
            converted_player_x = int(round(self.turtle_player.xcor()/UNIT))
            converted_player_y = 0 - int(round((self.turtle_player.ycor()-UNIT/2)/UNIT))
            
            converted_player_y = converted_player_y + int((len(level)-1)/2)
            converted_player_x = converted_player_x + int(len(level[0])/2)
            print(converted_player_x)
            print(converted_player_y)
            print(level[converted_player_y][converted_player_x])
            if level[converted_player_y][converted_player_x] == "X":
                if action == 'left':
                    player.player().right(90)
                elif action == 'right':
                    player.player().left(90)
                elif action == 'forward':
                    player.player().back(5)
                elif action == 'back':
                    player.player().forward(5)

    def check_object_collision(self, objects_positions:dict) -> None:
        position_ = self.turtle_player.position()
        obj = is_collided_with(position_,objects_positions)
        if obj != 'W':
            if obj not in self.inventory:
                names = {'P':'Washing Powder', 'F':"Flavouring agent", 'C':'Dirty Clothes'}
                self.inventory.append(obj)
                self.inv_phrase += names[obj]+'; '
                writer.write(self.inv_phrase)
        elif obj == 'W':
            print(self.inventory)
            if len(self.inventory) >= 3:
                for i in self.inventory:
                    if i not in self.given_to_machine:
                        self.given_to_machine.append(i)
                self.inventory.clear()
                if len(self.given_to_machine) >= 3:
                    erase_text(writer)
                    writer.write('YOU WON!')
    
    def left(self) -> None:
        self.turtle_player.left(90)
        self.check_for_wall('left')
        self.check_object_collision(positions)
    
    def right(self) -> None:
        self.turtle_player.right(90)
        self.check_for_wall('right')
        self.check_object_collision(positions)
    
    def forward(self) -> None:
        self.turtle_player.forward(3)
        self.check_for_wall('forward')
        self.check_object_collision(positions)

    def back(self) -> None:
        self.turtle_player.back(3)
        self.check_for_wall('back')
        self.check_object_collision(positions)
    
    

    


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
def place_objects():
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
                
                
                


positions = {} #a dict for positions of objects
#drawing level
def draw_level():
    global positions
    drawer.showturtle()
    #placing objects
    place_objects()
    #preparations to draw level
    drawer.penup()
    drawer.left(90)
    drawer.forward(len(level)/2*UNIT)
    drawer.left(90)
    drawer.forward(len(level[0])/2*UNIT)
    drawer.right(180)

    positions = {}

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
                if symbol[1] == 'W':
                    wm = 'C:\\Users\\vlady\\XPYTHON\\tour1\\task1\\images\\laundry-washing-machine.gif' #washing machine
                    turtle.register_shape(wm)
                    drawer.shape(wm)
                    drawer.stamp()
                elif symbol[1] == 'C':
                    clothes = 'C:\\Users\\vlady\\XPYTHON\\tour1\\task1\\images\\clothes.gif' 
                    turtle.register_shape(clothes)
                    drawer.shape(clothes)
                    drawer.stamp()
                elif symbol[1] == 'F':
                    clothes = 'C:\\Users\\vlady\\XPYTHON\\tour1\\task1\\images\\flavouring_agent.gif' 
                    turtle.register_shape(clothes)
                    drawer.shape(clothes)
                    drawer.stamp()
                elif symbol[1] == 'P':
                    clothes = 'C:\\Users\\vlady\\XPYTHON\\tour1\\task1\\images\\powder.gif' 
                    turtle.register_shape(clothes)
                    drawer.shape(clothes)
                    drawer.stamp()
                else:
                    drawer.write(symbol[1], align='center')
                positions[drawer.pos()] = symbol[1]
                drawer.forward(UNIT)
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


draw_level()
drawer.hideturtle()

# Update the screen to see the changes   
wn.update() 
wn.tracer(1)

#declaring player

player = Player()

player.player().goto(28, -28)

#listening to player controls
wn.onkeypress(player.forward, 'w')
wn.onkeypress(player.back, 's')
wn.onkeypress(player.left, 'a')
wn.onkeypress(player.right, 'd')
wn.listen()

# Keep the window open
wn.mainloop() 
