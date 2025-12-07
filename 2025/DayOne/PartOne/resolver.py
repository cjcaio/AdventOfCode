file_path = "input.txt"
starting_number = 50
number_of_zeros = 0
lines_as_words = []
moves_as_int = []

with open(file_path, 'r') as file:
    for line in file:
        word = line.strip()
        lines_as_words.append(word) ## list with all moves

for move in lines_as_words:
    number = move[1:]
    if move[0] == 'R':
        number = int(number)
    elif move[0] == 'L':
        number = int(number) * -1

    moves_as_int.append(number)

for move in moves_as_int:
    starting_number = (starting_number + move) % 100

    if starting_number == 0:
        number_of_zeros += 1

print(number_of_zeros)