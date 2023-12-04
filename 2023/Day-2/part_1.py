with open('input.txt') as f:
    data = f.read()

allowed = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum = 0

for line in data.strip().split('\n'):
    check = True
    game_id, line = line.split(':')
    for game in line.split(';'):
        for balls in game.split(','):
            num, color = balls.split()
            if int(num) > allowed.get(color):
                check = False
    if check:
        sum += int(game_id.split()[-1])

print(sum)