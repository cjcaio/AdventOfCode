file_path = "input.txt"
LEN_LINE_DEFAULT = 138
again = True

with open(file_path, 'r') as file:
    input = file.read()
#
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
# print(lines)

marked_lines = [list(line) for line in lines]

def check_adjacents(line: list, pos: int) -> int:
    many = 0
    if pos + 1 < LEN_LINE_DEFAULT:
        if line[pos+1] == '@':
            many += 1
    if pos-1 >= 0:
        if line[pos-1] == '@':
            many += 1
    return many

def check_adjacents_line_below(lines: list, i: int, j: int) -> int:
    many = 0
    if lines[i+1][j] == '@':
        many += 1
    if j + 1 < len(lines[i+1]) and lines[i+1][j+1] == '@':
        many += 1
    if j - 1 >= 0 and lines[i+1][j-1] == '@':
        many += 1
    return many

def check_adjacents_line_above(lines: list, i: int, j: int) -> int:
    many = 0
    if lines[i-1][j] == '@':
        many += 1
    if j + 1 < len(lines[i-1]) and lines[i-1][j+1] == '@':
        many += 1
    if j - 1 >= 0 and lines[i-1][j-1] == '@':
        many += 1
    return many

def check_adjacents_line_above_and_below(lines: list, i: int, j: int) -> int:
    many = 0
    # abaixo
    if lines[i+1][j] == '@':
        many += 1
    if j + 1 < len(lines[i+1]) and lines[i+1][j+1] == '@':
        many += 1
    if j - 1 >= 0 and lines[i+1][j-1] == '@':
        many += 1
    # acima
    if lines[i-1][j] == '@':
        many += 1
    if j + 1 < len(lines[i-1]) and lines[i-1][j+1] == '@':
        many += 1
    if j - 1 >= 0 and lines[i-1][j-1] == '@':
        many += 1
    return many

def run(input: str) -> tuple:
    lines_local = input.strip().split('\n')
    marked_lines_local = [list(line) for line in lines_local]

    reachable_rolls = 0
    four_adj_rolls = 0

    for i, line in enumerate(lines_local):
        for j in range(len(line)):
            adj_rolls = 0
            if line[j] == '@':

                adj_rolls += check_adjacents(line, j)

                if i == 0:
                    adj_rolls += check_adjacents_line_below(lines_local, i, j)

                if i == len(lines_local)-1:
                    adj_rolls += check_adjacents_line_above(lines_local, i, j)

                if i != 0 and i != len(lines_local)-1:
                    adj_rolls += check_adjacents_line_above_and_below(lines_local, i, j)

                if adj_rolls < 4:
                    print(f"line: {i}, pos: {j}, adj: {adj_rolls}")
                    reachable_rolls += 1
                    print(f"reachables: {reachable_rolls}")

                    marked_lines_local[i][j] = '.'


    again = reachable_rolls > 0

    new_input = "\n".join("".join(row) for row in marked_lines_local)

    return new_input, reachable_rolls, again

total_reachable_rolls = 0

new_input, reachable_rolls, again = run(input)

total_reachable_rolls += reachable_rolls

while again:
    new_input, reachable_rolls, again = run(new_input)
    total_reachable_rolls += reachable_rolls
    print(new_input)

##too high - 12256

print(f"Answer: {total_reachable_rolls}")