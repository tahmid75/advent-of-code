inputFile = open('data/1.txt', 'r')
depths = list(map(int, inputFile.read().splitlines()))
result = 0
size = len(depths)
prev_window = sum(depths[:3])

for i in range(3, size):
    curr_sum = prev_window + depths[i] - depths[i-3]
    if prev_window < curr_sum:
        result += 1 
    prev_window = curr_sum
print(result)
inputFile.close()