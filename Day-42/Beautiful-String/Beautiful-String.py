def makeBeautiful(str):
	# Write your code here
	n = len(str)

	pattern1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(n)])
	pattern2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(n)])

	count1 = 0
	count2 = 0

	for i in range(n) :
		if str[i] != pattern1[i] :
			count1 += 1
		if str[i] != pattern2[i] :
			count2 += 1

	return min(count1, count2)