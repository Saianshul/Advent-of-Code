with open('input.txt') as f:
    data = f.read()

sum = 0

for line in data.strip().split('\n'):
    red = []
    green = []
    blue = []

    game_id, line = line.split(':')
    for game in line.split(';'):
        for balls in game.split(','):
            num, color = balls.split()
            if color == 'red':
                red.append(int(num))
            if color == 'green':
                green.append(int(num))
            if color == 'blue':
                blue.append(int(num))

    max_red_count = 0
    max_green_count = 0
    max_blue_count = 0
    
    for count in red:
        if count > max_red_count:
            max_red_count = count
    for count in green:
        if count > max_green_count:
            max_green_count = count
    for count in blue:
        if count > max_blue_count:
            max_blue_count = count
    
    power = max_red_count * max_green_count * max_blue_count
    sum += power
    
print(sum)