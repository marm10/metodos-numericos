#!/usr/bin/env python3
import sys

def funcao(x):
	return x**3 - 9*x + 3


def bisseccao(f, a, b, e, maxIter):
	fa = f(a)
	fb = f(b)
	if fa*fb > 0:
		print("A função não muda de sinal.")
		return(True, None)

	print("k\t a\t\t fa\t\t b\t\t fb\t\t x\t\t fx\t\t intervalo")

	intervalo = abs(b-a)
	x = (a+b)/2
	fx = f(x)

	print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, fa, b, fb, x, fx, intervalo))

	if intervalo <= e:
		return (False, x)

	k = 1
	while k <= maxIter:
		if fa * fx > 0:
			a = x
			fa = fx
		else:
			b = x
			fb = fx

		intervalo = abs(b-a)
		x = (a+b)/2
		fx = f(x)

		print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, fa, b, fb, x, fx, intervalo))

		if intervalo <= e:
			return(False, x)

		k = k+1
	print("Numero maximo de interações atingido.")
	return(True,)

try:
	a = 0
	b = 2
	e = 0.001
	maxIter = 20
	(hasError, root) = bisseccao(funcao, a, b, e, maxIter)
except IndexError:
	print("usage: bigdigits.py <number>")
except ValueError as err:
	print(err, " in ", digits)
