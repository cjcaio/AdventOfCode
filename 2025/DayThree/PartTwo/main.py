file_path = "input.txt"
banks = []
max_joltage = 0

with open(file_path, 'r') as file:
    for line in file:
        batteries = line.strip()
        banks.append(batteries)

# banks = ['811111111111119']

for bank in banks:
    n = len(bank)
    to_remove = n - 12

    stack = []

    for i, digit in enumerate(bank):
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1

        stack.append(digit)

    while to_remove > 0:
        stack.pop()
        to_remove -= 1

    largest_joltage = int(''.join(stack))
    max_joltage += largest_joltage


print(max_joltage)