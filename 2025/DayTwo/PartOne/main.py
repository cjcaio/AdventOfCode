file_path = 'input.txt'
ranges = []
sum_of_sequences = 0

def is_odd(n):
    return n % 2 == 1

with open(file_path, 'r') as file:
    ranges = [x.strip() for x in file.read().split(',')]

print(ranges)

for rng in ranges:
    min = rng.split('-')[0]
    min_len = len(min)
    max = rng.split('-')[1]
    max_len = len(max)

    if is_odd(min_len) and is_odd(max_len):
        continue
        print(min_len, max_len)


    numbers = list(range(int(min), int(max) + 1))
    # print(numbers)

    for num in numbers:
        num = str(num)
        num_length = len(num)
        mid_pos_number = num_length // 2
        if not is_odd(num_length):
            if num[0:mid_pos_number] == num[mid_pos_number:]:
                print(f"Found sequence: {num}")
                sum_of_sequences += int(num)

print(sum_of_sequences)