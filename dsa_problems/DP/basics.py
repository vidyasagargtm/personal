

""" 
	Storing calculated ith fibonacci in array, using further to calculate the next fibonacci number

"""


fib_dp = [-1 for i in range(101)]

def fib(n):
	if n <= 1:
		return n
	if fib_dp[n] == -1:
		fib_dp[n] = fib(n-1) + fib(n-2)
	return fib_dp[n]



def fib_iter(n):
	DP = [-1 for i in range(n+1)]
	DP[0], DP[1] = 0, 1
	for i in range(2, n+1):
		DP[i] = DP[i-1] + DP[i-2]

	return DP[n]






def LPSS(S):

	N = len(S)

	DP = [[-1 for j in range(N)] for i in range(N)]

	print(LPSS_utils(S, 0, N-1, DP))


def LPSS_utils(S, i, j, DP):

	if i == j:
		return 1

	if i > j:
		return 0


	if DP[i][j] == -1:

		if S[i] == S[j]:
			DP[i][j] = 2 + LPSS_utils(S, i+1, j-1, DP)
		else:
			DP[i][j] = max(LPSS_utils(S, i+1, j, DP), LPSS_utils(S, i, j-1, DP))
	return DP[i][j]

# LPSS("adadadada")



def lengthOfLongestSubstring(A):
    max_length = 0
    hash_set = set()
    i, j = 0, 0
    start, end = 0, 0
    N = len(A)

    while(i < N):
        if A[i] in hash_set:
            hash_set.remove(A[j])
            j += 1
        else:
            hash_set.add(A[i])
            curr_length = len(hash_set)
            if curr_length > max_length:
            	max_length = curr_length
            	start = j
            	end = i            
            i += 1
    return f"Substring is: '{A[start: end+1]}' and Length: {max_length}"


A = 'abcabcbb'
print(lengthOfLongestSubstring(A))


def path(mat):
	N = len(mat)
	M = len(mat[0])
	for i in range(N):
		for j in range(M):
			mat[i][j] *= -1

	ans = mat[-1][-1] * -1





need to identify data skewness and set hive.optimize.skewjoin=true;








