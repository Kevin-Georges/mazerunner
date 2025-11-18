#defining the maze
def create_maze(width: int = 5, height: int = 5):
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
            if i==0 or i==height-1 or j==0 or j == width-1:
                row.append("#")
            else:
                row.append(".")
        maze.append(row)
    return maze

#adding a horizontal wall
def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    maze[horizontal_line][x_coordinate]= "#"
    return maze

#adding a vertical wall
def add_vertical_wall(maze, y_coordinate, vertical_line):
    maze[y_coordinate][vertical_line]= "#"
    return maze

#returning the dimensions of the maze
def  get_dimensions(maze) -> tuple:
    height = len (maze)
    width = len (maze[0])
    return [width, height]

#returning informaton about the walls around a specific (x,y) co-ordinate
def get_walls(maze, x_coordinate, y_coordinate) -> tuple:
    walls={
        "North": maze[y_coordinate - 1][x_coordinate],
        "East": maze[y_coordinate][x_coordinate + 1],
        "South": maze[y_coordinate + 1][x_coordinate],
        "West": maze[y_coordinate][x_coordinate - 1]
    }
    walls2 = []
    for i in walls:
        if walls[i]=="#":
            walls[i]= True
            walls2.append(True)
        else:
            walls[i]= False
            walls2.append(False)
    return tuple(walls2)
