with open('input.txt') as f:
    data = f.read().strip().split('\n')

part_nums = []

for i, line in enumerate(data):
    skip_iterations = 0

    for j, char in enumerate(line):
        if skip_iterations > 0:
            skip_iterations -= 1
            continue

        if char.isdigit():
            if i == 0 and j == 0:
                check = data[i][j + 1] in '@#$%&*-+=/' or data[i + 1][j] in '@#$%&*-+=/' or data[i + 1][j + 1] in '@#$%&*-+=/'
            elif i == 0 and 0 < j < len(line) - 1:
                check = data[i][j - 1] in '@#$%&*-+=/' or data[i][j + 1] in '@#$%&*-+=/' or data[i + 1][j - 1] in '@#$%&*-+=/' or data[i + 1][j] in '@#$%&*-+=/' or data[i + 1][j + 1] in '@#$%&*-+=/'
            elif i == 0 and j == len(line) - 1:
                check = data[i][j - 1] in '@#$%&*-+=/' or data[i + 1][j - 1] in '@#$%&*-+=/' or data[i + 1][j] in '@#$%&*-+=/'
            elif 0 < i < len(data) - 1 and j == 0:
                check = data[i - 1][j] in '@#$%&*-+=/' or data[i - 1][j + 1] in '@#$%&*-+=/' or data[i][j + 1] in '@#$%&*-+=/' or data[i + 1][j] in '@#$%&*-+=/' or data[i + 1][j + 1] in '@#$%&*-+=/'
            elif 0 < i < len(data) - 1 and j == len(line) - 1:
                check = data[i - 1][j - 1] in '@#$%&*-+=/' or data[i - 1][j] in '@#$%&*-+=/' or data[i][j - 1] in '@#$%&*-+=/' or data[i + 1][j - 1] in '@#$%&*-+=/' or data[i + 1][j] in '@#$%&*-+=/'
            elif i == len(data) - 1 and j == 0:
                check = data[i - 1][j] in '@#$%&*-+=/' or data[i - 1][j + 1] or data[i][j + 1] in '@#$%&*-+=/'
            elif i == len(data) - 1 and 0 < j < len(line) - 1:
                check = data[i - 1][j - 1] in '@#$%&*-+=/' or data[i - 1][j] in '@#$%&*-+=/' or data[i - 1][j + 1] in '@#$%&*-+=/' or data[i][j - 1] in '@#$%&*-+=/' or data[i][j + 1] in '@#$%&*-+=/'
            elif i == len(data) - 1 and j == len(line) - 1:
                check = data[i - 1][j - 1] in '@#$%&*-+=/' or data[i - 1][j] in '@#$%&*-+=/' or data[i][j - 1] in '@#$%&*-+=/'
            else:
                check = data[i - 1][j - 1] in '@#$%&*-+=/' or data[i - 1][j] in '@#$%&*-+=/' or data[i - 1][j + 1] in '@#$%&*-+=/' or data[i][j - 1] in '@#$%&*-+=/' or data[i][j + 1] in '@#$%&*-+=/' or data[i + 1][j - 1] in '@#$%&*-+=/' or data[i + 1][j] in '@#$%&*-+=/' or data[i + 1][j + 1] in '@#$%&*-+=/'

            if check:
                if line[j + 1].isdigit() and line[j + 2].isdigit():
                    part_nums.append(int(char + line[j + 1] + line[j + 2]))
                    skip_iterations += 2
                elif line[j - 1].isdigit() and line[j + 1].isdigit():
                    part_nums.append(int(line[j - 1] + char + line[j + 1]))
                    skip_iterations += 1
                elif line[j - 1].isdigit() and line[j - 2].isdigit():
                    part_nums.append(int(line[j - 2] + line[j - 1] + char))
                elif line[j + 1].isdigit():
                    part_nums.append(int(char + line[j + 1]))
                    skip_iterations += 1
                elif line[j - 1].isdigit():
                    part_nums.append(int(line[j - 1] + char))
                else:
                    part_nums.append(int(char))

print(sum(part_nums))