sonarData = open('data/1.txt', 'r')
depths = list(map(int, sonarData.read().splitlines()))
result = 0

for i in range(len(depths)-1):
    if depths[i] < depths[i+1]:
        result += 1 

print(result)
sonarData.close()