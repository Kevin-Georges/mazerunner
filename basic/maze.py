def create_maze(width: int = 5, height: int = 5):
    maze = []
    width = (width * 2) + 1
    height = (height * 2) + 1

    for j in range(height):
        row = []
        for i in range(width):
            if j == 0 or j == height - 1 or i == 0 or i == width - 1:
                row.append("#")
            elif j % 2 == 0 and i % 2 == 0:
                row.append("#")
            else:
                row.append(".")
        maze.append(row)
    return maze

# convert (i,j) maze indices to (x,y) coordinates
def convert_i_to_coordinates(i: int) -> int:
    return (i - 1) // 2

def convert_j_to_y_coordinate(j: int) -> int:
    return (j - 1) // 2

# convert (x,y) coordinates to (i,j) maze indices
def convert_x_coordinates_to_i(x_coordinate: int) -> int:
    return (x_coordinate * 2) + 1

def convert_y_coordinates_to_j(y_coordinate: int) -> int:
    return (y_coordinate * 2) + 1

# adding a horizontal wall (works on maze indices)
# horizontal_line = maze row (must be even)
# x_coordinate    = maze column (must be odd)
def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    if horizontal_line % 2 == 0 and x_coordinate % 2 == 1:
        maze[horizontal_line][x_coordinate] = "#"
    return maze

# adding a vertical wall (works on maze indices)
# y_coordinate = maze row (must be odd)
# vertical_line = maze column (must be even)
def add_vertical_wall(maze, y_coordinate, vertical_line):
    if y_coordinate % 2 == 1 and vertical_line % 2 == 0:
        maze[y_coordinate][vertical_line] = "#"
    return maze

# returning the dimensions of the maze
def get_dimensions(maze) -> tuple:
    height = len(maze)
    width = len(maze[0])
    return [width, height]

def display_maze(maze):
    for row in maze:
        print("".join(row))

# returning information about the walls around a specific (x,y) coordinate
def get_walls(maze, x_coordinate, y_coordinate) -> tuple:
    # Convert cell coordinates -> maze indices
    i = convert_x_coordinates_to_i(x_coordinate)
    j = convert_y_coordinates_to_j(y_coordinate)

    walls = {
        "North": maze[j - 1][i],
        "East":  maze[j][i + 1],
        "South": maze[j + 1][i],
        "West":  maze[j][i - 1]
    }
    # Return True if wall ("#"), False if empty (".")
    return (
        walls["North"] == "#",
        walls["East"] == "#",
        walls["South"] == "#",
        walls["West"] == "#"
    )

if __name__ == "__main__":
    maze = create_maze()
    maze = add_horizontal_wall(maze, 3, 4)  # x=3(odd), j=4(even)
    maze = add_vertical_wall(maze, 3, 4)    # y=3(odd), i=4(even)
    display_maze(maze)
    print("\nWalls around cell (1,1):")
    print(get_walls(maze, 1, 1))
