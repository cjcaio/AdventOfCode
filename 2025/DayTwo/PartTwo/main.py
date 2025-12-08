file_path = 'input.txt'
ranges = []
sum_of_sequences = 0

def is_odd(n) -> bool:
    return n % 2 == 1

def is_divisible_by(n, divisor) -> bool:
    return n % divisor == 0

def split_in_parts(str, parts) -> list:
    string_length = len(str)
    part_size = string_length // parts
    result = []
    for i in range(parts):
        result.append(str[i * part_size:(i + 1) * part_size])
    return result

def all_equal(parts) -> bool:
    return all(part == parts[0] for part in parts)

with open(file_path, 'r') as file:
    ranges = [x.strip() for x in file.read().split(',')]

print(ranges)

for rng in ranges:
    min = rng.split('-')[0]
    min_len = len(min)
    max = rng.split('-')[1]
    max_len = len(max)

    numbers = list(range(int(min), int(max) + 1))
    print(numbers)

    for num in numbers:
        num = str(num)
        num_length = len(num)
        added = False

        # Verifica todos os divisores possíveis do comprimento
        for divisor in range(2, num_length + 1):
            if is_divisible_by(num_length, divisor) and not added:
                parts = split_in_parts(num, divisor)

                if all_equal(parts):
                    sum_of_sequences += int(num)
                    added = True
                    break

print(sum_of_sequences)