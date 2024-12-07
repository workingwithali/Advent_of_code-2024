with open(r"d:\Advent_of_code-2024\Day_06\day_06.in") as fin:
    grid = fin.read().strip().split("\n")
    


n = len(grid)
m = len(grid[0])

found = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == "^":
            found = True
            break
    if found:
        break


dir = 0 
dd = [[-1,0],[0,1],[]]

    
