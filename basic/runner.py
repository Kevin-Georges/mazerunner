#create runner
import maze
def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> dict:
    runner = {
        "x": x,
        "y": y,
        "orientation": orientation
    }
    return runner

# return values held in dictionary
def get_x(runner):
    return runner.get("x")

def get_y(runner):
    return runner.get("y")

def get_orientation(runner):
    return runner.get("orientation")

#turn the runner
def turn(runner, direction: str):
    #dictionary of each orientation change
    left_turn = {
        "N": "W",
        "W": "S", 
        "S": "E",
        "E": "N"
    }
    right_turn = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }
    if direction == "Left":
        runner["orientation"] = left_turn[runner["orientation"]]
    elif direction == "Right":
        runner["orientation"] = right_turn[runner["orientation"]]
    return runner

#move runner forward
def forward(runner):
    if get_orientation(runner) == "N":
        runner["y"] = runner["y"] + 1
    elif get_orientation(runner) == "E":
        runner["x"] = runner["x"] + 1
    elif get_orientation(runner) == "S":
        runner["y"] = runner["y"] - 1
    elif get_orientation(runner) == "W":
        runner["x"] = runner["x"] - 1
    return runner

def sense_walls(runner, maze) -> tuple:
    x = get_x(runner)
    y = get_y(runner)

    # Convert cell coordinates to maze indices
    i = maze.convert_x_coordinates_to_i(x)
    j = maze.convert_y_coordinates_to_j(y)

    # Check left, forward and right based on orientation
    if get_orientation(runner) == "N":
        left = maze[j][i - 1] == "#"
        forward_wall = maze[j - 1][i] == "#"
        right = maze[j][i + 1] == "#"
    elif get_orientation(runner) == "E":
        left = maze[j - 1][i] == "#"
        forward_wall = maze[j][i + 1] == "#"
        right = maze[j + 1][i] == "#"
    elif get_orientation(runner) == "S":
        left = maze[j][i + 1] == "#"
        forward_wall = maze[j + 1][i] == "#"
        right = maze[j][i - 1] == "#"
    elif get_orientation(runner) == "W":
        left = maze[j + 1][i] == "#"
        forward_wall = maze[j][i - 1] == "#"
        right = maze[j - 1][i] == "#"

    return (bool(left), bool(forward_wall), bool(right))

# ========== MAIN EXECUTION ==========
my_maze = maze.create_maze(4, 4)
print("Maze layout:")
maze.display_maze(my_maze)

# Create a runner at cell coordinates (1,1), facing North
my_runner = create_runner(1, 1, "N")
print(f"\nRunner starting at x={my_runner['x']}, y={my_runner['y']}, facing {my_runner['orientation']}")

# Sense walls around the runner
walls = sense_walls(my_runner, my_maze)
print("Walls (left, forward, right):", walls)

# Example: turn right and move forward
turn(my_runner, "Right")
forward(my_runner)
print(f"\nRunner moved to x={my_runner['x']}, y={my_runner['y']}, facing {my_runner['orientation']}")
walls = sense_walls(my_runner, my_maze)
print("Walls now (left, forward, right):", walls)
