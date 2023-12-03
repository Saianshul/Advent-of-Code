with open('input.txt') as f:
    data = f.read()

word_versions = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

calibration_vals_sum = 0
for ammended_calibration_val in data.strip().split('\n'):
    digits = []
    for i, char in enumerate(ammended_calibration_val):
        if char.isdigit():
            digits.append(char)
        for j, word_version in enumerate(word_versions):
            if ammended_calibration_val[i:].startswith(word_version):
                digits.append(str(j + 1))
    if digits:
        calibration_vals_sum += int(digits[0] + digits[-1])

print(calibration_vals_sum)