with open(r"d:\Advent_of_code-2024\Day_06\day_06.in") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)
m = len(grid[0])

# Find the starting position marked with '^'
found = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == "^":
            found = True
            break
    if found:
        break

# Direction indices for up, right, down, left
dir = 0
dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

seen = set()

# Main traversal loop
while True:
    seen.add((i, j))
    next_i = i + dd[dir][0]
    next_j = j + dd[dir][1]

    # Check bounds and break if out of grid
    if not (0 <= next_i < n and 0 <= next_j < m):
        break

    # If hitting a wall, turn right
    if grid[next_i][next_j] == '#':
        dir = (dir + 1) % 4
    else:
        # Move to the next cell
        i, j = next_i, next_j

print(len(seen))
