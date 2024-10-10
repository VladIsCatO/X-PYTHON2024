def gen_maze():
    pass


def solve_maze(maze, x, y, solution): # goal is to get to the last square (border) of the maze
    if maze[y][x]:
        return False
    solution.append([x,y]) #solution with coordinates, where to go to resolve
    pos = [x,y]
    last_pos = []
    for i in range((len(maze)-1)*(len(maze)-1)):
        try:
            if pos != False:
                pos = check_around(maze, pos[0], pos[1], solution, pos, last_pos)
            else:
                pos = check_around(maze, solution[-1][0], solution[-1][1], solution, pos, last_pos)

            last_pos.append(solution[-1])
            if pos != False:
                x,y = pos[0],pos[1]
            print(solution)
            
            # print('--------------')
            # print(last_pos)
            if len(maze)-1 == solution[-1][1] or len(maze[0])-1 == solution[-1][0] or solution[-1][1] == 0 or solution[-1][0] == 0:
                return True
            
        except Exception as e:
            print(e)
            return False
    return False
    

def check_around(maze, x, y, solution:list, pos, last_pos:list):
    print(last_pos)
    if maze[y][x+1] == 0 and [x+1,y] not in last_pos:
        solution.append([x+1,y])
        pos = [x+1,y]
        return pos
    if maze[y+1][x] == 0 and [x,y+1] not in last_pos:
        solution.append([x,y+1])
        pos = [x,y+1]
        return pos
    if maze[y][x-1] == 0 and [x-1,y] not in last_pos:
        solution.append([x-1,y])
        pos = [x-1,y]
        return pos
    if maze[y-1][x] == 0 and [x,y-1] not in last_pos:
        solution.append([x,y-1])
        pos = [x,y-1]
        return pos
    else:
        solution.pop(-1)
        return False
    

solution = []


# maze = [[1,1,1,1],
#         [1,0,0,1],
#         [1,0,0,1],
#         [1,0,1,1]]

maze = [[1,1,1,0,1,1,1,1],
        [1,0,1,0,0,0,1,1],
        [1,0,0,0,0,1,1,1],
        [1,1,1,1,1,1,1,1],
        ]


print(solve_maze(maze, 1, 1, solution))
#MAZE MUST BE SQUARE
