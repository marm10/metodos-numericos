#!/usr/bin/env python3
import sys

def funcao(x):
	return x**3 - x + 1

def flin(x):
	return 3*(x**2) - 1


def newtonRaphson(f, flin, x0, e, maxIter):
	if abs(f(x0)) < e:
		return(False, x0)

	k = 1
	print("k\t x\t\t fx")
	print("%d\t%e\t%e" % (0, x0, f(x0)))
	while k <= maxIter:
		x1 = x0 - f(x0)/flin(x0)
		print("%d\t%e\t%e" % (k, x1, f(x1)))

		if abs(f(x1)) < e or abs(x1 - x0) < e:
			return(False, x1)

		x0 = x1
		k = k+1
	return(True, maxIter)
	

try:
	x0 = 1
	e = 0.0001
	maxIter = 50
	(hasError, root) = newtonRaphson(funcao, flin,x0, e, maxIter)
except IndexError:
	print("usage: bigdigits.py <number>")
except ValueError as err:
	print(err, " in ", digits)
