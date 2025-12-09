file_path = 'input.txt'
fresh_ids = 0
range_list = []
merged = []

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

for rang in ranges:
    min_val, max_val = rang.split('-')
    range_list.append((int(min_val), int(max_val)))

range_list.sort()
for start, end in range_list:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

print(merged)

fresh_ids = sum(end - start + 1 for start, end in merged)

print(f'there are {fresh_ids} fresh ids')