import copy
from tqdm import tqdm

# Read and parse the input grid
with open(r"d:\Advent_of_code-2024\Day_06\day_06.in") as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]

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

ii, jj = i, j

# Direction vectors for up, right, down, left
dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir = 0
og_seen = set()

# Simulate the original traversal to find all visited cells
while True:
    og_seen.add((i, j))

    next_i = i + dd[dir][0]
    next_j = j + dd[dir][1]

    # Check bounds
    if not (0 <= next_i < n and 0 <= next_j < m):
        break

    # Change direction if a wall is encountered
    if grid[next_i][next_j] == "#":
        dir = (dir + 1) % 4
    else:
        i, j = next_i, next_j


def will_loop(oi, oj):
    """
    Check if placing a wall at (oi, oj) causes a loop in the path.
    """
    if grid[oi][oj] == "#":
        return False  # Already a wall, cannot place another wall

    # Temporarily place a wall at (oi, oj)
    grid[oi][oj] = "#"
    i, j = ii, jj
    dir = 0
    seen = set()

    while True:
        # Check if the current state has been visited before
        if (i, j, dir) in seen:
            grid[oi][oj] = "."  # Reset the grid cell
            return True
        seen.add((i, j, dir))

        next_i = i + dd[dir][0]
        next_j = j + dd[dir][1]

        # Check bounds
        if not (0 <= next_i < n and 0 <= next_j < m):
            grid[oi][oj] = "."  # Reset the grid cell
            return False

        # Change direction or move to the next cell
        if grid[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j


# Iterate through all cells visited in the original traversal
ans = 0
for oi, oj in tqdm(og_seen, desc="Processing cells"):
    if will_loop(oi, oj):
        ans += 1

print(ans)
