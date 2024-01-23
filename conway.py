from time import sleep
import curses

window = curses.initscr()
size = 15

x = [[0 for _ in range(size)] for _ in range(size)] # Empty square grid size x size

def render(grid):
    result = ""
    for i in grid:
        result += "".join(list(map(lambda n: "🟩" if n==0 else "🟥", i))) + "\n"
    # previously i used os.system("cls") for clearing console but it caused flickering so i used it instead
    window.clear()
    window.addstr(0, 0, result)
    window.refresh()

        
# Another way of setting for size = 15 
# x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#      [0, 0, 1, 1, 0, 0, 1, 0, 0, 0], 
#      [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
#      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
#      [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# Example setting
x[13][4] = 1
x[13][5] = 1
x[12][5] = 1
x[11][5] = 1
x[11][6] = 1
x[10][7] = 1
x[10][4] = 1
x[10][3] = 1


def tick(grid):
    neighbour_count = [[0 for _ in grid] for _ in grid] 
    for y in range(size):
        for x in range(size):
            # To exclude values like y = -1 or y > window size and same with x
            for i in range(max(0,y-1), min(len(grid),y+2)):
                for j in range(max(0, x - 1), min(len(grid), x + 2)):
                        neighbour_count[y][x] += grid[i][j]
            neighbour_count[y][x] -= grid[y][x] # Removing value of itself to not count is as neighbour

    for y in range(size):
        # Rules of conway's game of life
        for x in range(size):
            if grid[y][x] == 0 and neighbour_count[y][x] == 3:
                grid[y][x] = 1
            if grid[y][x] == 1 and (neighbour_count[y][x] < 2 or neighbour_count[y][x] > 3):
                grid[y][x] = 0
    return grid

for i in range(200):
    render(x)
    x = tick(x)
    sleep(0.02)