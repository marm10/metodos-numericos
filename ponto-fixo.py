#!/usr/bin/env python3
import sys

def funcao(x):
	return x**3 - 9*x + 3

def phi(x):
	return (x**3)/9 + (1/3)


def pontoFixo(f, phi, x0, e, maxIter):
	if abs(f(x0)) < e:
		return(False, x0)
	k = 1

	print("k\t x\t\t fx\t\t phix")
	
	while k <= maxIter:
		x1 = phi(x0)
		
		print("%d\t%e\t%e\t%e" % (k, x1, f(x1), phi(x1)))

		if abs(f(x1)) < e or abs(x1 - x0) < e:
			return(False, x1)
		
		x0=x1
		k = k+1
	return(True, maxIter)

try:
	x0 = 0.5
	e = 0.0005
	maxIter = 50
	(hasError, root) = pontoFixo(funcao, phi, x0, e, maxIter)
except IndexError:
	print("usage: bigdigits.py <number>")
except ValueError as err:
	print(err, " in ", digits)
