
with open(r"d:\Advent_of_code-2024\Day_04\day_04.in") as fin:
    lines = fin.read().strip().split('\n')

n = len(lines)
m = len(lines[0])

# Generate all directions
dd = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))

def has_xmas(i, j, d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if lines[ii][jj] != x:
            return False
    return True

ans = 0
for i in range(n):
    for j in range(m):
        for d in dd:
            ans += has_xmas(i, j, d)

print(ans)