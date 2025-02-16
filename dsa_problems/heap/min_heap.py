

import heapq


# list1 = [1,45, 60,4,5]

# heapq.heapify(list1)

# print(list1)

# print(heapq.heappop(list1))

# print(list1)



# N no digit given, print all N digit number using 1,2



def print_all(A, index, N):

	if index == N:
		print(A)
		return 

	A[index] = 1
	print_all(A, index+1, N)

	A[index] = 2
	print_all(A, index+1, N)



print_all([1, 1, 1, 1], 0, 4)








