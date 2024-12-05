with open(r"d:\Advent_of_code-2024\Day_05\day_05.in") as fin:
    content = fin.read().strip()

# Split the content into rules and updates sections
if "\n\n" in content:
    raw_rules, updates = content.split("\n\n")
else:
    raise ValueError("Input file does not contain two sections separated by a blank line.")

# Parse rules
rules = []
for line in raw_rules.split("\n"):
    a, b = line.split("|")
    rules.append((int(a), int(b)))

# Parse updates
updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

def follows_rules(update):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i
    
    for a, b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False, 0
        
    return True, update[len(update) // 2]

ans = 0

for update in updates:
    good, mid = follows_rules(update)
    if good:
        ans += mid

print(ans)
