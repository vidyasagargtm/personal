
def SOD(N):
	if N == 0:
		return 0
	return SOD(N // 10) + N%10

print("SOD --> ", SOD(1234))


# Print 1 to N without loop
def print_number1(n):
	
	if n < 1:
		return
	print_number1(n-1)
	print(n, end=' ')


# Print N to 1 without loop
def print_number(n):
	if n < 1:
		return
	print(n, end=' ')
	print_number(n-1)



# Mean of array using recursion 
# Mean = Sum of all elements devided by total number
def meanOfArray(A, index=0, mean=0.0):
	if index == len(A):
		return round(mean, 2)
	mean = round(float(mean * index + A[index]) / (index + 1), 2)
	return meanOfArray(A, index + 1, mean)

A = [12, 312, 412]
print(meanOfArray(A))


# Sum of natural number using recurssion 
def natural_num_sum(N):
	if N <= 1:
		return N
	return N+natural_num_sum(N-1)

print(natural_num_sum(5))


# Decimal to binary using recursion :

# 10 = 1010
# 11 = 1011
# 12 = 1100
# 13 = 1101
# 14 = 1110
# 15 = 1111

# def dec_to_binary(N, b=''):
# 	if N == 0:
# 		return b if b != '' else '0'
# 	b =  str(N % 2) + b
# 	return dec_to_binary(N // 2, b)
# print(dec_to_binary(16))

def binary(D):
	if D == 0:
		return 0
	return D % 2 + 10 * binary(D // 2)
print(binary(100))


# Check if given string is pelindrome or not whithout loop

def isPelindrom(S, start, end):
	if start >= end:
		return True
	if S[start] == S[end]:
		return isPelindrom(S, start+1, end-1)
	else:
		return False


S = "ab"
print(isPelindrom(S, 0, 1))

