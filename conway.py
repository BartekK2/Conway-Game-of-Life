from time import sleep
import curses

window = curses.initscr()

rozmiar = 25


x = [[0 for _ in range(rozmiar)] for _ in range(rozmiar)] 
def render(grid):
    d = ""
    for i in grid:
        d += "".join(list(map(lambda n: "🟩" if n==0 else "🟥", i))) + "\n"
    # previously i used os.system("cls") for clearing console but it caused flickering so i used it instead
    window.clear()
    window.addstr(0, 0, d)
    window.refresh()

        

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

x[13][4] = 1
x[13][5] = 1
x[12][5] = 1
x[11][5] = 1
x[11][6] = 1
x[10][7] = 1
x[10][4] = 1
x[10][3] = 1

render(x)
sleep(0.5)


def tick(grid):
    neighbour_count = [[0 for _ in grid] for _ in grid] 
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            for i in range(y-1,y+2):
                for j in range(x-1,x+2):
                    if i!=-1 and i!= len(grid):
                        if j!=-1 and j!=len(row):
                            if i!=y or j!=x:
                                neighbour_count[y][x] += grid[i][j]
    for y,row in enumerate(grid):
        for x,value in enumerate(row):
            if grid[y][x] == 0 and neighbour_count[y][x] == 3:
                grid[y][x] = 1
            if grid[y][x] == 1 and (neighbour_count[y][x] < 2 or neighbour_count[y][x] > 3):
                grid[y][x] = 0
    return grid

for i in range(200):
    render(x)
    x = tick(x)
    sleep(0.02)