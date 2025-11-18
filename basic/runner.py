#create runner
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
