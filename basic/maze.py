def create_maze(width: int = 5, height: int = 5):
    # internal maze uses a doubled grid with walls on even indices
    maze = []
    width = (width * 2) + 1
    height = (height * 2) + 1

    for j in range(height):
        row = []
        for i in range(width):
            if j == 0 or j == height - 1 or i == 0 or i == width - 1:
                row.append("#")  # outer wall
            elif j % 2 == 0 and i % 2 == 0:
                row.append("#")  # internal wall posts
            else:
                row.append(".")
        maze.append(row)
    return maze


def convert_i_to_coordinates(i: int) -> int:
    return (i - 1) // 2


def convert_j_to_y_coordinate(j: int) -> int:
    return (j - 1) // 2


def convert_x_coordinates_to_i(x_coordinate: int) -> int:
    return (x_coordinate * 2) + 1


def convert_y_coordinates_to_j(y_coordinate: int) -> int:
    return (y_coordinate * 2) + 1


def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    # valid only on even rows and odd columns
    if horizontal_line % 2 == 0 and x_coordinate % 2 == 1:
        maze[horizontal_line][x_coordinate] = "#"
    return maze


def add_vertical_wall(maze, y_coordinate, vertical_line):
    # valid only on odd rows and even columns
    if y_coordinate % 2 == 1 and vertical_line % 2 == 0:
        maze[y_coordinate][vertical_line] = "#"
    return maze


def get_dimensions(maze) -> tuple:
    return (len(maze[0]), len(maze))


def display_maze(maze):
    for row in maze:
        print("".join(row))


def get_walls(maze, x_coordinate, y_coordinate) -> tuple:
    # convert logical cell coords → maze indices
    i = convert_x_coordinates_to_i(x_coordinate)
    j = convert_y_coordinates_to_j(y_coordinate)

    return (
        maze[j - 1][i] == "#",  # north
        maze[j][i + 1] == "#",  # east
        maze[j + 1][i] == "#",  # south
        maze[j][i - 1] == "#"   # west
    )

if __name__ == "__main__":
    maze = create_maze()
    maze = add_horizontal_wall(maze, 3, 4)  # x=3(odd), j=4(even)
    maze = add_vertical_wall(maze, 3, 4)    # y=3(odd), i=4(even)
    display_maze(maze)
    print("\nWalls around cell (1,1):")
    print(get_walls(maze, 1, 1))
