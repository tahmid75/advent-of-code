def victory(board, move):
    x = [[board[i][j] in move for j in range(5)] for i in range(5)]
    y = [[x[j][i] for j in range(5)] for i in range(5)]
    for i in range(5):
        if sum(x[i]) == 5 or sum(y[i]) == 5:
            return True
    return False

inputFile = open('data/04.txt', 'r')
data = inputFile.read().splitlines()

moves = map(int, data[0].split(','))
boards = []
for l in data[1:]:
	if not l:
		boards.append([])
		continue
	boards[-1].append(list(map(int, l.split())))

m = set()
res = -1
for move in moves:
	m.add(move)
	numboard = []
	for board in boards:
		if not victory(board, m):
			numboard.append(board)
	if len(numboard) == 0:
		res = 0
		for i in boards[0]:
			for j in i:
				if j not in m:
					res += j
		res *= move
		break
	boards = numboard
print(res)
inputFile.close()