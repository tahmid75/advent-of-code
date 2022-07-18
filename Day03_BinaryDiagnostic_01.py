inputFile = open('data/03.txt', 'r')
l = inputFile.read().splitlines()
gamma_rate = [0] * len(l[0])
epsilon_rate = [0] * len(l[0])
for i in range(len(l[0])):
	zero = 0
	one = 0
	for j in range(len(l)):
		zero += l[j][i] == '0'
		one += l[j][i] == '1'
	if zero > one:
		gamma_rate[i] = '0'
		epsilon_rate[i] = '1'
	elif one > zero:
		gamma_rate[i] = '1'
		epsilon_rate[i] = '0'
decimal_gamma = int(''.join(gamma_rate), 2)
decimal_epsilon = int(''.join(epsilon_rate), 2)
print(decimal_gamma * decimal_epsilon)
inputFile.close()