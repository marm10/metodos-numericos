#!/usr/bin/env python3
import sys

def ajusta_linhas(i, A, b):
	#itera entre as linhas
	for j in range(n):
		#achou uma linha satisfatoria, troca linhas
		if A[j][i] != 0:
			aux = A[i]
			auxb = b[i]
			A[i] = A[j]
			A[j] = aux
			b[i] = b[j]
			b[j] = auxb
	
def gauss_jordan(A, b):
	n = len(A)
	i = 0
	j = 0
	while i < n:
		#pivot igual a zero, ajusta linhas
		if  A[j][i] == 0:
			ajusta_linhas(i, A, b)

		m = A[i][i]
		for j in range(n):
			A[i][j] = A[i][j]/m
		b[i] = b[i]/m

		for k in range(n):
			if k != i:
				m = A[k][i]
				print(m)
				for j in range(n):
					A[k][j] = A[k][j] - m * A[i][j]
				b[k] = b[k]- m*b[i]
		i = i+1

	return b

def identidade(n):
	I = [[0 for y in range(n)]for x in range (n)]
	for i in range(n):
		I[i][i] = 1
	
	return I


A = [[3, 2, 1, -1],
     [0, 1, 0, 3],
     [0, -3, -5, 7],
     [0, 2, 4, 0]]

b =  [5, 6, 7, 15]
print(gauss_jordan(A,b))


