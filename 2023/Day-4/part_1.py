import math

with open('input.txt') as f:
    data = f.read()

total = 0

for line in data.strip().split('\n'):
    points = 0
    power = 0

    nums = line.split(':')[-1]
    winning_nums, your_nums = nums.split('|')

    for winning_num in winning_nums.split():
        for your_num in your_nums.split():
            if your_num == winning_num:
                points = int(math.pow(2, power))
                power += 1
    total += points

print(total)