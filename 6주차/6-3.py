# 연쇄행렬 최소 곱셈을 이용, 행렬의 최소 곱셈 수 계산

import sys

def MatrixOrder(arr, size):
	m = [[0 for x in range(size)] for x in range(size)]
	# for i in range(size):
	# 	m[i][i] = 0
	
	for L in range(2, size):
		for i in range(1, size - L + 1):
			j = i + L - 1
			m[i][j] = sys.maxsize
			for k in range(i, j):
				q = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j]
				if q < m[i][j]:
					m[i][j] = q

	return m[1][size-1]	

arr = list(map(int, input().split()))
size = len(arr)

print("최소 연산 수: "+ str(MatrixOrder(arr, size)))