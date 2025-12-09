import runner

def shortest_path(maze, starting=None, goal=None):
    # coursework default starting point
    if starting is None:
        start = (0, 0)
    else:
        start = starting

    width = len(maze[0])
    height = len(maze)
    max_x = (width - 1) // 2
    max_y = (height - 1) // 2

    # coursework default goal = top-right logical cell
    if goal is None:
        end = (max_x, max_y)
    else:
        end = goal

    # explore the maze using left-hug only
    r = runner.create_runner(start[0], start[1], "N")
    moves = runner.explore(r, maze, end)

    # orientation maps
    left_turn  = {"N":"W","W":"S","S":"E","E":"N"}
    right_turn = {"N":"E","E":"S","S":"W","W":"N"}

    def apply_action(x, y, o, action):
        # update orientation first
        for c in action:
            if c == "L": o = left_turn[o]
            elif c == "R": o = right_turn[o]

        # then move forward if action ends with F
        if action.endswith("F"):
            if o == "N": y += 1
            if o == "E": x += 1
            if o == "S": y -= 1
            if o == "W": x -= 1

        return x, y, o

    # build full path of visited positions
    # BEFORE each move (as per explore() format)
    path = []
    cx, cy = start
    orientation = "N"

    for (px, py, action) in moves:
        # record position BEFORE action
        path.append((cx, cy, action))
        cx, cy, orientation = apply_action(cx, cy, orientation, action)

    # Now remove loops
    seen = {}
    final = []

    for (x, y, action) in path:
        pos = (x, y)

        if pos in seen:
            # cut everything from the previous occurrence onward
            idx = seen[pos]
            final = final[:idx]
            seen = {}
            for i, (xx, yy, aa) in enumerate(final):
                seen[(xx, yy)] = i

        seen[pos] = len(final)
        final.append((x, y, action))

    return final
