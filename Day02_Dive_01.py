import csv


horizontal_pos = 0
vertical_pos = 0

with open('data/02.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in reader:
		if row[0] == 'forward':
			horizontal_pos += int(row[1])
		elif row[0] == 'up':
			vertical_pos -= int(row[1])
		elif row[0] == 'down':
			vertical_pos += int(row[1])

print(horizontal_pos * vertical_pos)
