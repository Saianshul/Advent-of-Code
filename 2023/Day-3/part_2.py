with open('input.txt') as f:
    data = f.read().strip().split('\n')

gear_ratios = []

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '*':            
            digit_found_indicies = []
            check = False

            gear_ratio_nums = []

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if not (di == 0 and dj == 0):
                        if data[i + di][j + dj] in '0123456789':
                            digit_found_indicies.append([i + di, j + dj])
                            check = True
                            if data[i + di][j + dj + 2] in '0123456789' and data[i + di][j + dj + 1] not in '0123456789':
                                digit_found_indicies.append([i + di, j + dj + 2])                           
                            break

            if len(digit_found_indicies) != 2:
                continue

            if check:
                for k, coor in enumerate(digit_found_indicies):
                    for l, index in enumerate(coor):
                        if l == 1:
                            continue                        
                        
                        if data[coor[l]][coor[l + 1] + 1] in '0123456789' and data[coor[l]][coor[l + 1] + 2] in '0123456789':
                            gear_ratio_nums.append(int(data[coor[l]][coor[l + 1]] + data[coor[l]][coor[l + 1] + 1] + data[coor[l]][coor[l + 1] + 2]))
                        elif data[coor[l]][coor[l + 1] - 1] in '0123456789' and data[coor[l]][coor[l + 1] + 1] in '0123456789':
                            gear_ratio_nums.append(int(data[coor[l]][coor[l + 1] - 1] + data[coor[l]][coor[l + 1]] + data[coor[l]][coor[l + 1] + 1]))
                        elif data[coor[l]][coor[l + 1] - 1] in '0123456789' and data[coor[l]][coor[l + 1] - 2] in '0123456789':
                            gear_ratio_nums.append(int(data[coor[l]][coor[l + 1] - 2] + data[coor[l]][coor[l + 1] - 1] + data[coor[l]][coor[l + 1]]))
                        elif data[coor[l]][coor[l + 1] + 1] in '0123456789':
                            gear_ratio_nums.append(int(data[coor[l]][coor[l + 1]] + data[coor[l]][coor[l + 1] + 1]))
                        elif data[coor[l]][coor[l + 1] - 1] in '0123456789':
                            gear_ratio_nums.append(int(data[coor[l]][coor[l + 1] - 1] + data[coor[l]][coor[l + 1]]))
                        else:
                            gear_ratio_nums.append(int(data[coor[l]][coor[l + 1]]))

            gear_ratio = 1
            for gear_ratio_num in gear_ratio_nums:
                gear_ratio *= gear_ratio_num
            gear_ratios.append(gear_ratio)

print(sum(gear_ratios))