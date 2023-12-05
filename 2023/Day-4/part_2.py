def handle_copies(copies_count):
    for i in range(matching_nums):
        copies.append(int(card_nums) + i + 1)
        copies_count += 1
    
    return copies_count

with open('input.txt') as f:
    data = f.read()

originals = []
copies = []

originals_count = 0
copies_count = 0

for line in data.strip().split('\n'):
    card_ids, nums = line.split(':')
    winning_nums, your_nums = nums.split('|')
    card_nums = card_ids.split()[-1]

    matching_nums = 0
    for winning_num in winning_nums.split():
        for your_num in your_nums.split():
            if your_num == winning_num:
                matching_nums += 1
    
    originals.append(int(card_nums))
    originals_count += 1

    copies_count = handle_copies(copies_count)
    for copy in copies:
        if copy == int(card_nums):
            copies_count = handle_copies(copies_count)
    
print(originals_count + copies_count)