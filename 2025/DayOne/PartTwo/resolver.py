file_path = "input.txt"
starting_number = 50
number_of_zeros = 0
zeros_trough_rotation = 0
lines_as_words = []
moves_as_int = []

with open(file_path, 'r') as file:
    for line in file:
        word = line.strip()
        lines_as_words.append(word)  ## list with all moves

for move in lines_as_words:
    number = move[1:]
    if move[0] == 'R':
        number = int(number)
    elif move[0] == 'L':
        number = int(number) * -1

    moves_as_int.append(number)

for move in moves_as_int:
    if move > 0:
        clicks_to_zero = (100 - starting_number) % 100
        if clicks_to_zero == 0:
            clicks_to_zero = 100
        if move >= clicks_to_zero:
            zeros_trough_rotation += (move - clicks_to_zero) // 100 + 1
    elif move < 0:
        clicks_to_zero = starting_number
        if clicks_to_zero == 0:
            clicks_to_zero = 100
        if abs(move) >= clicks_to_zero:
            zeros_trough_rotation += (abs(move) - clicks_to_zero) // 100 + 1

    starting_number = (starting_number + move) % 100

    if starting_number == 0:
        number_of_zeros += 1

print(zeros_trough_rotation)
