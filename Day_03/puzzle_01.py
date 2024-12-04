import re
with open(r"d:\Advent_of_code-2024\Day_03\day_03.in") as fin:
    line = fin.read().strip()

matches = re.findall(r"mul\((\d+),(\d+)\)", line)

ans = 0
for match in matches:
    ans += int(match[0]) * int(match[1])

print(ans) 