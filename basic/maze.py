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

#printing the maze
maze= create_maze()
for row in maze:
    x="" .join(row)
    print(x)
  
