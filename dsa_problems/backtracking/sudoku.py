

def sudoku(cell):
	if cell == 81:
		printSudoku(mat)
		return

	row = cell // 9
	col = cell % 9
	if mat[row][col] == 0:
		for choice in range(1, 10):
			if validChoice(row, col, choice):
				mat[row][col] = choice
				sudoku(cell + 1)
				mat[row][col] = 0
	else:
		sudoku(cell + 1)


def validChoice(row, col, choice):
	# check current row
	for i in range(9):
		if mat[row][i] == choice:
			return False

	# check current column 
	for i in range(9):
		if mat[i][col] == choice:
			return False

	# check current square
	square_i = row - (row % 3)
	square_j = col - (col % 3)
	for i in range(3):
		for j in range(3):
			if mat[i + square_i][j + square_j] == choice:
				return False
	return True


def printSudoku(mat):
	for row in range(9):
		print(mat[row])


mat = [
	[0, 1, 0, 6, 0, 0, 0, 8, 4],
	[0, 0, 0, 0, 0, 7, 0, 0, 0],
	[0, 8, 7, 0, 0, 4, 0, 0, 0],
	[0, 0, 2, 9, 0, 0, 0, 6, 5],
	[9, 0, 3, 0, 0, 0, 2, 0, 7],
	[1, 5, 0, 0, 0, 6, 3, 0, 0],
	[0, 0, 0, 5, 0, 0, 4, 9, 0],
	[0, 0, 0, 4, 0, 0, 0, 0, 0],
	[5, 2, 0, 0, 0, 1, 0, 3, 0]
]


sudoku(0)





