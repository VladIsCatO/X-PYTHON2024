"""Washing machine Game"""
#Imports section
import turtle
import random
import sys
from time import sleep
#---------------------------------------------
#INIT
WN = turtle.Screen() #Starting screen
WN.setup(1080, 560)
drawer = turtle.Turtle() #declaring our drawer of the level
writer = turtle.Turtle() #writer will write text
positions = {} #a dict for positions of objects
#---------------------------------------------
#Functions helpers
def replace(string, to, index):
    """replacing symbol at string variable to something else"""
    return string[:index] + to + string[index + 1:] #I took this part from stack overflow
def is_collided_with(player_coords:tuple, objects_coords:dict) -> str | None:
    """checking for collision""" #Taken from stack overflow, changed
    for i in range(len(objects_coords)):
        if abs(player_coords[0] - list(objects_coords.keys())[i][0]) < 15:
            if abs(player_coords[1] - list(objects_coords.keys())[i][1]) < 15:
                return list(objects_coords.values())[i]
    return None
def erase_text(player_:turtle.Turtle, font_size=5):
    """erasing text"""
    WN.tracer(0)
    squares = '⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛'
    player_.color(WN.bgcolor())
    player_.write(squares, align='center', font=("Arial", font_size, "normal"))
    player_.forward(5)
    player_.write(squares, align='center', font=("Arial", font_size, "normal"))
    player_.back(5)
    player_.left(90)
    player_.forward(12)
    player_.right(90)
    player_.write(squares, align='center', font=("Arial", font_size, "normal"))
    player_.forward(5)
    player_.write(squares, align='center', font=("Arial", font_size, "normal"))
    player_.back(5)
    player_.left(90)
    player_.back(12)
    player_.right(90)
    player_.pencolor('black')
    WN.tracer(1)
#---------------------------------------------
# Explaining game
writer.write('Hi there!', align='center', font=('Arial', 20, 'normal'))
sleep(2)
erase_text(writer, 10)
PHRASE = 'At this game, you need to take all the things...'
writer.write(PHRASE, align='center', font=('Arial', 20, 'normal'))
sleep(5)
erase_text(writer, 10)
writer.write('...and put them into washing machine.', align='center', font=('Arial', 20, 'normal'))
sleep(4)
erase_text(writer, 10)
writer.write('Good luck! Use  W A S D  to move', align='center', font=('Arial', 20, 'normal'))
sleep(2)
erase_text(writer, 10)
#putting writer in the position

writer.penup()
writer.hideturtle()
writer.goto(WN.screensize()[0]-WN.screensize()[0]/2.5, WN.screensize()[1]-WN.screensize()[1]/0.6)
# This turns off screen updates
WN.tracer(0)
#---------------------------------------------
#Classes
class Player():
    """player class"""
    def __init__(self) -> None:
        #declaring player's variables
        self.turtle_player = turtle.Turtle()
        self.inventory = []
        self.inv_phrase = 'Inventory: '
        self.given_to_machine = []
        #applying all the properties I need to our turtle player
        self.turtle_player.showturtle()
        self.turtle_player.penup()
        self.turtle_player.speed(0)
    def player(self) -> turtle.Turtle:
        """returning player"""
        return self.turtle_player
    def get_inventory(self) -> list:
        """returning inventory of player"""
        return self.inventory
    def check_for_wall(self, action: str) -> None:
        """checking for walls"""
        converted_player_x = int(round(self.turtle_player.xcor()/UNIT))
        converted_player_y = 0 - int(round((self.turtle_player.ycor()-UNIT/2)/UNIT))
        converted_player_y = converted_player_y + int((len(level)-1)/2)
        converted_player_x = converted_player_x + int(len(level[0])/2)
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
        """checking for collision with objects"""
        position_ = self.turtle_player.position()
        obj = is_collided_with(position_,objects_positions)
        if obj != 'W' and obj not in self.inventory:
            names = {'P':'Washing Powder', 'F':"Flavouring agent", 'C':'Dirty Clothes'}
            if obj is not None:
                self.inventory.append(obj)
                self.inv_phrase += names[obj]+'; '
                writer.write(self.inv_phrase)
        elif obj == 'W':
            if len(self.inventory) >= 3:
                for i in self.inventory:
                    if i not in self.given_to_machine:
                        self.given_to_machine.append(i)
                self.inventory.clear()
                if len(self.given_to_machine) >= 3:
                    erase_text(writer)
                    writer.goto(0,0)
                    WN.clear()
                    writer.write('YOU WON!', align='center', font=('Arial', 100, 'normal'))
                    sleep(10)
                    sys.exit()
    def left(self) -> None:
        """turning left"""
        self.turtle_player.left(90)
        self.check_for_wall('left')
        self.check_object_collision(positions)
    def right(self) -> None:
        """turning right"""
        self.turtle_player.right(90)
        self.check_for_wall('right')
        self.check_object_collision(positions)
    def forward(self) -> None:
        """going forward"""
        self.turtle_player.forward(3)
        self.check_for_wall('forward')
        self.check_object_collision(positions)
    def back(self) -> None:
        """going backwards"""
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
for line_ in level:
    for symbol_ in line_:
        if symbol_ == ' ':
            objects.append(' ')
for i_ in range(4):
    objects.pop()
#declaring UNIT constant that we'll use to draw level
UNIT = 28 #number of steps
#placing objects in random positions
def place_objects():
    """Placing objects"""
    for line in enumerate(level):
        for symbol in enumerate(line[1]):
            if symbol[1] == ' ':
                object_to_add = random.randint(0,len(objects)-1)
                level.insert(line[0], replace(level[line[0]], objects[object_to_add], symbol[0]))
                level.pop(line[0]+1)
                objects.pop(object_to_add)
def start_drawing():
    """start to reduce statements in function draw_level"""
    drawer.showturtle()
    place_objects()
    drawer.penup()
    drawer.left(90)
    drawer.forward(len(level)/2*UNIT)
    drawer.left(90)
    drawer.forward(len(level[0])/2*UNIT)
    drawer.right(180)
def draw_objects(symbol):
    """drawing objects, also to reduce amount of statements in draw_level function"""
    base_dir = "C:\\Users\\vlady\\XPYTHON\\tour1\\task1\\images\\"
    if symbol[1] == 'W':
        wm = f'{base_dir}laundry-washing-machine.gif' #washing machine
        WN.register_shape(wm)
        drawer.shape(wm)
        drawer.stamp()
    elif symbol[1] == 'C':
        clothes = f'{base_dir}clothes.gif'
        WN.register_shape(clothes)
        drawer.shape(clothes)
        drawer.stamp()
    elif symbol[1] == 'F':
        clothes = f'{base_dir}flavouring_agent.gif'
        WN.register_shape(clothes)
        drawer.shape(clothes)
        drawer.stamp()
    elif symbol[1] == 'P':
        clothes= f'{base_dir}powder.gif'
        WN.register_shape(clothes)
        drawer.shape(clothes)
        drawer.stamp()
    else:
        drawer.write(symbol[1], align='center')
    positions[drawer.pos()] = symbol[1]
    drawer.forward(UNIT)
#drawing level
def draw_level():
    """Drawing level"""
    start_drawing()
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
                except IndexError:
                    drawer.forward(UNIT)
            elif symbol[1] == 'X':
                drawer.pendown()
                drawer.forward(UNIT)
                drawer.penup()
            elif symbol[1] == ' ':
                drawer.forward(UNIT)
            else:
                draw_objects(symbol)
        if level[line[0]][0] == 'X':
            drawer.right(90)
            drawer.forward(UNIT)
            drawer.right(90)
            drawer.penup()
            drawer.forward(len(line[1])*UNIT)
            drawer.left(180)

draw_level()
drawer.hideturtle()
# Update the screen to see the changes
WN.update()
WN.tracer(1)
#declaring player
player = Player()
player.player().goto(28, -28)
#listening to player controls
WN.onkeypress(player.forward, 'w')
WN.onkeypress(player.back, 's')
WN.onkeypress(player.left, 'a')
WN.onkeypress(player.right, 'd')
WN.listen()
# Keep the window open
WN.mainloop()
