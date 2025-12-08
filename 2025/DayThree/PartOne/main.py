file_path = "input.txt"
banks = []
max_joltage = 0

with open(file_path, 'r') as file:
    for line in file:
        batteries = line.strip()
        banks.append(batteries)

for bank in banks:
    largest_joltage = 0

    for i in range(len(bank)):
        for j in range(len(bank)):
            if i == j or i > j:
                continue

            elif int(bank[i]+bank[j]) > largest_joltage:
                largest_joltage = int(bank[i]+bank[j])

    max_joltage += largest_joltage

print(max_joltage)