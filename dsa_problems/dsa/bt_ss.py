
import copy

result = []

def print_all_ss(A, N, i, ss):

	if i == N:
		result.append(copy.deepcopy(ss))
		return

	print_all_ss(A, N, i+1, ss)
	ss.append(A[i])
	
	print_all_ss(A, N, i+1, ss)
	ss.remove(A[i])
	


A = [1,2,3]
result = []
ss =[]

print_all_ss(A, 3, 0, ss)

# result.sort()
print(result)
