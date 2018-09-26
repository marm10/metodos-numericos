#!/usr/bin/env python3
import sys

def funcao(x):
	return x**3 - 9*x + 3

def flin(x):
	return 3*(x**2) - 9


def secante(f, x0, x1, e, maxIter):
	if abs(f(x0)) < e:
		return(False, x0)

	if abs(f(x1)) < e or abs(x1 - x0) < e:
		return(False, x1)

	k = 1
	print("k\t x\t\t fx")
	
	while k <= maxIter:
		x2 = x1 - (f(x1)/(f(x1) - f(x0)))*(x1 - x0)

		print("%d\t%e\t%e" % (k, x2, f(x2)))

		if abs(f(x2)) < e or abs(x2 - x1) < e:
			return(False, x1)

		x0 = x1
		x1 = x2
		k = k+1
	return(True, maxIter)
	

try:
	x0 = 0
	x1 = 1
	e = 0.0005
	maxIter = 50
	(hasError, root) = secante(funcao, x0, x1, e, maxIter)
except IndexError:
	print("usage: bigdigits.py <number>")
except ValueError as err:
	print(err, " in ", digits)
