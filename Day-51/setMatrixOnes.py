''' Problem statement
You have been given a non-empty grid ‘MAT’ consisting of only 0s and 1s. Your task is to modify it in such a way that if a cell has value 1 (MAT[i][j] == 1), then all the cells of the i-th row and j-th column should be changed to 1.

For Example
If the given grid is this:
[0, 0, 0]
[0, 0, 1]

Then the modified grid will be
[0, 0, 1],
[1, 1, 1] '''
from os import *
from sys import *
from collections import *
from math import *

def setMatrixOnes(mat, n, m):

	# Write your code here
	if not mat:
		return mat

	rows_to_update = set()
	cols_to_update = set()

	for i in range(n):
		for j in range(m):
			if mat[i][j] == 1:
				rows_to_update.add(i)
				cols_to_update.add(j)

	for row in rows_to_update:
		for j in range(m):
			mat[row][j]=1

	for col in cols_to_update:
		for j in range(n):
			mat[j][col]=1

	return mat

