


class Sorting(object):
	"""docstring for sorting"""
	
	def __init__(self, arr):
		self.arr = arr
		self.size = len(arr)

	# find minimum and swap with correct position
	def selection_sort(self):
		for i in range(self.size):
			c_min = self.arr[i]
			index = i
			for j in range(i, self.size):
				if self.arr[j] < c_min:
					c_min = self.arr[j]
					index = j
			self.arr[index], self.arr[i] = self.arr[i], self.arr[index]
		return self.arr

	# bubble max ele in the end 
	def bubble_sort(self):

		for i in range(self.size-1):
			count = 0
			for j in range(1, self.size):
				if self.arr[j-1] > self.arr[j]:
					self.arr[j-1], self.arr[j] = self.arr[j], self.arr[j-1]
					count += 1
			if count == 0:
				break
		return self.arr

	def merge_sort(self):
		self.ms_utils(0, self.size-1)
		return self.arr

	def ms_utils(self, s, e):
		if s >= e:
			return
		mid = (s + e) // 2
		self.ms_utils(s, mid)
		self.ms_utils(mid+1, e)
		self.merge(s, mid, e)

	def merge(self, s, m, e):
		C = []
		i = s
		j = m + 1
		while (i <= m and j <= e):
			if self.arr[i] < self.arr[j]:
				C.append(self.arr[i])
				i += 1
			else:
				C.append(self.arr[j])
				j += 1

		while (i <= m):
			C.append(self.arr[i])
			i += 1

		while (j <= e):
			C.append(self.arr[j])
			j += 1

		i = s
		j = 0
		while i <= e:
			self.arr[i] = C[j]
			i += 1
			j += 1









A = [1, 4, 1, 5, 2, 6,-1]

ss = Sorting(A)
print(ss.merge_sort())

