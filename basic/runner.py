from maze import (
    convert_x_coordinates_to_i,
    convert_y_coordinates_to_j,
    get_dimensions,
)


def create_runner(x=0, y=0, orientation="N"):
    return {"x": x, "y": y, "orientation": orientation}


def get_x(runner):
    return runner["x"]


def get_y(runner):
    return runner["y"]


def get_orientation(runner):
    return runner["orientation"]


def turn(runner, direction):
    # simple orientation rotation maps
    left_turn  = {"N": "W", "W": "S", "S": "E", "E": "N"}
    right_turn = {"N": "E", "E": "S", "S": "W", "W": "N"}

    if direction == "Left":
        runner["orientation"] = left_turn[runner["orientation"]]
    elif direction == "Right":
        runner["orientation"] = right_turn[runner["orientation"]]

    return runner


def forward(runner):
    o = runner["orientation"]

    if o == "N":
        runner["y"] += 1
    elif o == "E":
        runner["x"] += 1
    elif o == "S":
        runner["y"] -= 1
    elif o == "W":
        runner["x"] -= 1

    return runner


def sense_walls(runner, maze):
    # convert runner coords → maze indices
    x, y = get_x(runner), get_y(runner)
    i = convert_x_coordinates_to_i(x)
    j = convert_y_coordinates_to_j(y)
    o = get_orientation(runner)

    if o == "N":
        left  = maze[j][i - 1] == "#"
        front = maze[j - 1][i] == "#"
        right = maze[j][i + 1] == "#"

    elif o == "E":
        left  = maze[j - 1][i] == "#"
        front = maze[j][i + 1] == "#"
        right = maze[j + 1][i] == "#"

    elif o == "S":
        left  = maze[j][i + 1] == "#"
        front = maze[j + 1][i] == "#"
        right = maze[j][i - 1] == "#"

    else:  # W
        left  = maze[j + 1][i] == "#"
        front = maze[j][i - 1] == "#"
        right = maze[j - 1][i] == "#"

    return (left, front, right)


def go_straight(runner, maze):
    # blocked forward movement raises an error
    _, front, _ = sense_walls(runner, maze)
    if front:
        raise ValueError("wall in front")
    return forward(runner)


def move(runner, maze):
    # left-hug priority: left → front → right → back
    left, front, right = sense_walls(runner, maze)

    if not left:
        turn(runner, "Left")
        try:
            go_straight(runner, maze)
            return runner, "LF"
        except ValueError:
            turn(runner, "Right")

    if not front:
        try:
            go_straight(runner, maze)
            return runner, "F"
        except ValueError:
            pass

    if not right:
        turn(runner, "Right")
        try:
            go_straight(runner, maze)
            return runner, "RF"
        except ValueError:
            turn(runner, "Left")

    # dead end → turn around
    turn(runner, "Right")
    turn(runner, "Right")
    go_straight(runner, maze)
    return runner, "B"


def explore(runner, maze, goal=None):
    width, height = get_dimensions(maze)
    max_x = (width - 1) // 2
    max_y = (height - 1) // 2

    # coursework-correct default goal
    if goal is None:
        goal = (max_x, max_y)

    moves = []

    def next_pos(orientation):
        x, y = get_x(runner), get_y(runner)
        if orientation == "N": return (x, y + 1)
        if orientation == "E": return (x + 1, y)
        if orientation == "S": return (x, y - 1)
        if orientation == "W": return (x - 1, y)

    left_map  = {"N": "W", "W": "S", "S": "E", "E": "N"}
    right_map = {"N": "E", "E": "S", "S": "W", "W": "N"}
    back_map  = {"N": "S", "S": "N", "E": "W", "W": "E"}

    while True:
        x, y = get_x(runner), get_y(runner)
        o = get_orientation(runner)
        left, front, right = sense_walls(runner, maze)

        # if already at the goal (should not happen often)
        if (x, y) == goal:
            break

        # try moves that enter the goal
        if not left and next_pos(left_map[o]) == goal:
            moves.append((x, y, "LF"))
            turn(runner, "Left")
            forward(runner)
            break

        if not front and next_pos(o) == goal:
            moves.append((x, y, "F"))
            forward(runner)
            break

        if not right and next_pos(right_map[o]) == goal:
            moves.append((x, y, "RF"))
            turn(runner, "Right")
            forward(runner)
            break

        if next_pos(back_map[o]) == goal:
            moves.append((x, y, "B"))
            turn(runner, "Right")
            turn(runner, "Right")
            forward(runner)
            break

        # otherwise follow left-hug
        runner, action = move(runner, maze)
        moves.append((x, y, action))

    return moves

