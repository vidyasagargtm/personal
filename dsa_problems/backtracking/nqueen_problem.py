



def NQueen(Mat, N, row):
	if row == N:
		print(Mat)
		return 1
	for col in range(N):
		if isValidChoice(Mat, row, col, N):
			Mat[row][col] = 1
			NQueen(Mat, N, row + 1)
			Mat[row][col] = 0


def isValidChoice(Mat, row, col, N):

	# Checking current Column
	for j in range(row-1, -1, -1):
		if Mat[j][col] == 1:
			return False

	# Checking left diagonal
	i, j = row - 1, col - 1
	while(i >= 0) and (j >= 0):
		if Mat[i][j] == 1:
			return False
		i -= 1
		j -= 1

	# Checking right diagonal
	i, j = row - 1, col + 1
	while(i >= 0) and (j < N):
		if Mat[i][j] == 1:
			return False
		i -= 1
		j += 1

	return True




from copy  import deepcopy

class Solution:
	# @param A : integer
	# @return a list of list of strings
	def solveNQueens(self, A):
		matrix = [['.' for col in range(A)] for row in range(A)]
		self.result = []
		self.NQueens(matrix, A, 0)
		return self.result
	

	def NQueens(self, matrix, N, row):
		if row == N:
			self.result.append(deepcopy(matrix))
			return 
		
		for col in range(N):
			if self.isValidPosition(matrix, N, row, col):
				matrix[row][col] = "Q"
				self.NQueens(matrix, N, row+1)
				print(matrix)
				matrix[row][col] = "."


	def isValidPosition(self, matrix, N, row, col):

		# check column 
		for c in range(row):
			if matrix[c][col] == "Q":
				return False
		

		# check left diagonal 
		i, j = row - 1, col - 1
		while((i >= 0) and (j >= 0)):
			if matrix[i][j] == "Q":
				return False
			
			i -= 1
			j -= 1
		
		# check right diagonal 
		i, j = row - 1, col + 1
		while((i >= 0) and (j < N)):
			if matrix[i][j] == "Q":
				return False
			i -= 1
			j += 1
		return True



s = Solution()
	



N = 4

Mat = [[0 for c in range(N)] for r in range(N)]

print(s.solveNQueens(N))
