#!/usr/bin/env python3
import sys
	
def gauss_det(A, b):
	n = len(A)
	k = 0

	while k < n:
		i = k+1
		while i < n:
			m = A[i][k]/A[k][k]
			A[i][k] = 0
			j = k+1
			while j < n:
				A[i][j] = A[i][j] - m*A[k][j]
				j = j+1
			b[i] = b[i]- m*b[k]
			i = i+1
		k = k+1

	detr = det(A)
	x = substituicoes_retroativas(A, b)
	return (x, detr)

def det(A):
	n = len(A)
	det = 1
	k = 0
	while k < n:
		det = det * A[k][k]
		k = k + 1

	return det

def eliminacao_gauss(A, b):
	n = len(A)
	k = 0

	while k < n:
		i = k+1
		while i < n:
			m = A[i][k]/A[k][k]
			A[i][k] = 0
			j = k+1
			while j < n:
				A[i][j] = A[i][j] - m*A[k][j]
				j = j+1
			b[i] = b[i]- m*b[k]
			i = i+1
		k = k+1

	return substituicoes_retroativas(A, b)

def substituicoes_retroativas(A, b):
	n = len(A)
	x = n * [0]
	
	x[n-1] = b[n-1]/A[n-1][n-1]
	k = n - 1

	while k >= 0:
		s = 0
		j = k+1
		while j < n:
			s = s + A[k][j] * x[j]
			j = j + 1
		x[k] = (b[k] - s)/A[k][k]
		k = k - 1

	return x


A = [[1, -3, 2],
     [-2, 8, -1],
     [4, -6, 5]]

b =  [11, -15, 29]
print(gauss_det(A,b))


