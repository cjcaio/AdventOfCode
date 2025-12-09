file_path = "input.txt"
hash_line_1 = {}
hash_line_2 = {}
hash_line_3 = {}
hash_line_4 = {}
hash_operators = {}
answer = 0

with open(file_path, 'r') as file:
    content = file.read()
    lines = content.split('\n')
    print(lines)

for i, line in enumerate(lines):
    print(i, line)
    columns = line.split(' ')
    columns = [val for val in columns if val != '']

    for j in range(len(columns)):
        if i == 0:
            hash_line_1[j] = columns[j]
        if i == 1:
            hash_line_2[j] = columns[j]
        if i == 2:
            hash_line_3[j] = columns[j]
        if i == 3:
            hash_line_4[j] = columns[j]
        if i == 4:
            hash_operators[j] = columns[j]

for i in range(len(hash_line_1)):
    if hash_operators[i] == '*':
        res = int(hash_line_1[i]) * int(hash_line_2[i]) * int(hash_line_3[i]) * int(hash_line_4[i])
    else:
        res = int(hash_line_1[i]) + int(hash_line_2[i]) + int(hash_line_3[i]) + int(hash_line_4[i])

    print(hash_line_1[i], hash_line_2[i], hash_line_3[i], hash_operators[i], res)

    answer += res

## too low: 15416420295

print(answer)