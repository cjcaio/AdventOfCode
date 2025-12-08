file_path = "input.txt"
reachable_rolls = 0
LEN_LINE_DEFAULT = 138

with open(file_path, 'r') as file:
    input = file.read()

# input = '''..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.'''

lines = input.strip().split('\n')
print(lines)

def check_adjacents(line: list, pos: int) -> bool:
    many = 0
    if pos + 1 < LEN_LINE_DEFAULT:
        if line[pos+1] == '@':
            print(100)
            many += 1
    if pos-1 >= 0:
        if line[pos-1] == '@':
            print(200)
            many += 1
    return many

def check_adjacents_line_below(lines: list):
    many = 0
    if lines[i+1][j] == '@':
        many += 1
    if lines[i+1][j+1] == '@':
        many += 1
    if lines[i+1][j-1] == '@':
        many += 1

    return many

def check_adjacents_line_above(lines: list):
    many = 0
    if lines[i-1][j] == '@':
        many += 1
    if lines[i-1][j+1] == '@':
        many += 1
    if j-1 >= 0:
        if lines[i-1][j-1] == '@':
            many += 1

    return many

def check_adjacents_line_above_and_below():
    many = 0
    if lines[i+1][j] == '@':
        many += 1
    if j+1 < LEN_LINE_DEFAULT:
        if lines[i+1][j+1] == '@':
            many += 1
    if j-1 >= 0:
        if lines[i+1][j-1] == '@':
            many += 1
    if lines[i-1][j] == '@':
        many += 1
    if j+1 < LEN_LINE_DEFAULT:
        if lines[i-1][j+1] == '@':
            many += 1
    if j-1 >= 0:
        if lines[i-1][j-1] == '@':
            many += 1

    return many

for i, line in enumerate(lines):
    for j in range(len(line)):
        adj_rolls = 0
        if line[j] == '@':

            adj_rolls += check_adjacents(line,j)

            if i == 0:
                adj_rolls += check_adjacents_line_below(lines)

            if i == len(lines)-1:
                adj_rolls += check_adjacents_line_above(lines)

            if i != 0 and i != len(lines)-1:
                adj_rolls += check_adjacents_line_above_and_below()

            if adj_rolls < 4:
                print(f"line: {i}, pos: {j}, adj: {adj_rolls}")
                reachable_rolls += 1
                print(f"reachables: {reachable_rolls}")

## too high = 6665

print(f'Answer: {reachable_rolls}')
