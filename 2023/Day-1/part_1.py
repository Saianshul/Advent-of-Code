import csv

with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    data = [ammended_calibration_vals for row in reader for ammended_calibration_vals in row]
    
calibration_vals_sum = 0
for ammended_calibration_val in data:
    digits = [character for character in ammended_calibration_val if character.isdigit()]
    if digits:
        calibration_vals_sum += int(digits[0] + digits[-1])

print(calibration_vals_sum)