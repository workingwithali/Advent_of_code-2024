with open(r"d:\Advent_of_code-2024\Day_04\day_04.in") as fin:
    lines = fin.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

dd = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))

def has_xmas(i, j):
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return False
    if lines[i][j] != "A":
        return False

    # Check both diagonals
    diag_1 = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
    diag_2 = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"

    return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]

ans = 0
for i in range(n):
    for j in range(m):
        ans += has_xmas(i, j)

print(ans)