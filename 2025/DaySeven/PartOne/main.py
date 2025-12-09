file_path = 'input.txt'
splitters = set()
many_splits = 0

with open(file_path, 'r') as file:
    content = file.read()
    lines = content.split('\n')
    lines = lines[:-1]
    lines = [list(line) for line in lines]

for idx in range(len(lines)):
    for col in range(len(lines[0])):
        if idx == 0:
            if lines[idx][col] == 'S':
                init_pos = (idx,col)
        print(idx,col)
        if lines[idx][col] == '^':
            splitters.add((idx, col))

for idx in range(len(lines)):
    for col in range(len(lines[0])):
        print(idx,col)
        if idx == init_pos[0]+1 and col == init_pos[1] and (idx,col) not in splitters:
            lines[idx][col] = '|'

        elif (idx,col) in splitters:
            lines[idx][col-1] = '|'
            lines[idx][col+1] = '|'

for idx in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[idx][col] == '|' and (idx+1,col) not in splitters and idx+1 < len(lines):
            lines[idx+1][col] = '|'

for splitter in splitters:
    split_idx = splitter[0]
    split_col = splitter[1]

    if lines[split_idx-1][split_col] == '|':
        print(split_idx, split_col)
        many_splits += 1

for row in lines:
    for element in row:
        print(element, end=" ")
    print()

print(many_splits)