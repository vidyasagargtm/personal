

# def serachFile(directory, filename):
# 	all_files = getAllfiles(directory)
# 	for file in all_files:
# 		if file == filename:
# 			return True


# 	all_dirs = getAllDirectories(directory):
# 	for dirs in all_dirs:
# 		return serachFile(dirs, filename)

# 	return False 





def SOD(N):
	if N==0:
		return 0
	return (N%10 + SOD(N//10))






# Write a function to calculate pow(a, n):

# 1st version - iterative
def POW1(a, n):
	ans = 1
	for i in range(n):
		ans *= a
	return ans

# 2nd version - recurresive
def POW2(a, n):
	if n == 0:
		return 1
	return a * POW2(a, n-1)


# 3rd version - optimised recurresive
def POW3(a, n, p):
	if n == 0:
		return 1
	he = POW3(a, n//2, p)
	ha = ((he % p) * (he % p)) % p
	if(n&1):
		return ((a % p) * (ha % p)) % p
	else:
		return ha


print(POW3(2, 61, 19999))

print(1/(-2000000))

