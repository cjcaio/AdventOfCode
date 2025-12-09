file_path = 'input.txt'
fresh_ids = 0

with open(file_path, 'r') as file:
    ranges, values = file.read().split('\n\n')

# ranges = '''3-5
# 10-14
# 16-20
# 12-18'''
#
# values = '''1
# 5
# 8
# 11
# 17
# 32'''

ranges = ranges.split('\n')
values = values.split('\n')
values = values[:-1]

for i, value in enumerate(values):
    for j, r in enumerate(ranges):
        r = r.split('-')
        if int(r[0]) <= int(value) <= int(r[1]):
            print(f'value: {value} is in range: {r[0]}-{r[1]}')
            fresh_ids += 1
            break

print(f'there are {fresh_ids} fresh ids')