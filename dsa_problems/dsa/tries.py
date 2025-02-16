


# class Node(object):

# 	def __init__(self):
# 		self.isEnd = False
# 		self.HM = {}
# 		self.child = [None, None]


# class Tries(object):

# 	def insert(self, root, word):
# 		temp = root
# 		for char in word:
# 			char = char.lower()
# 			if temp.HM.get(char, None) == None:
# 				newNode = Node()
# 				temp.HM[char] = newNode
# 			temp = temp.HM[char]
# 		temp.isEnd = True


# 	def search(self, root, word):
# 		temp = root
# 		for char in word:
# 			char = char.lower()
# 			if temp.HM.get(char, None) == None:
# 				return False
# 			temp = temp.HM[char]
# 		return temp.isEnd



# def countUniqueRow(A):
# 	count = 0
# 	N = len(A)
# 	root = Node()
# 	for i in range(N):
# 		if insert(root, A[i]):
# 			count += 1
# 	return count


# def insert(root, ar):
# 	flag = False
# 	temp = root
# 	for idx in range(len(ar)):
# 		val = ar[idx]
# 		if temp.child[val] is not None:
# 			temp = temp.child[val]
# 		else:
# 			flag = True
# 			nn = Node()
# 			temp.child[val] = nn
# 			temp = nn
# 	return flag




A = [
	[2, 1, 0],
	[1, 1, 1],
	[0, 1, 1]
]


def rotten(A):
	no_of_rows = len(A)
	no_of_col = len(A[0])

	queue = []

	for row in range(no_of_rows):
		for col in range(no_of_col):
			if A[row][col] == 2:
				queue.append((row, col))

	minutes = 0
	while(len(queue) > 0):
		size = len(queue)
		while size > 0:
			row, col = queue.pop(0)
			# Top ele
			if row > 0:
				if A[row - 1][col] == 1:
					A[row - 1][col] = 2
					queue.append((row - 1, col))

			# Bottom
			if row < no_of_rows - 1:
				if A[row + 1][col] == 1:
					A[row + 1][col] = 2
					queue.append((row + 1, col))


			# left ele
			if col > 0:
				if A[row][col-1] == 1:
					A[row][col-1] = 2
					queue.append((row, col-1))

			# Bottom
			if col < no_of_col - 1:
				if A[row][col + 1] == 1:
					A[row][col + 1] = 2
					queue.append((row, col + 1))
			size -= 1
		minutes += 1

	flag = False
	for row in range(no_of_rows):
		for col in range(no_of_col):
			if A[row][col] == 1:
				return 0
			if A[row][col] == 2:
				flag = True
	return minutes - 1 if flag else 0




print(2 & 1)





