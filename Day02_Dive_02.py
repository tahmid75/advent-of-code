import csv

horizontal_pos = 0
vertical_pos = 0
aim = 0

with open('data/02.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        if row[0] == 'forward':
            horizontal_pos += int(row[1])
            vertical_pos += aim * int(row[1])
        elif row[0] == 'up':
            aim -= int(row[1])
        elif row[0] == 'down':
            aim += int(row[1])
print(horizontal_pos * vertical_pos)