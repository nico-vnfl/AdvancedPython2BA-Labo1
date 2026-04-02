import math
from scipy.integrate import quad

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n < 0:
		raise ValueError("n must be >= 0")
	
	result = 1
	for i in range(1, n+1): #car range s'arrête au dernier elem non compris
		result *= i
	return result
	

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	if a == 0:
		if b == 0:
			return ()
		return (-c/b,)
	
	delta = b*b - 4*a*c

	if delta < 0:
		return ()
	elif delta ==0:
		return (-b/(2*a),)
	else:
		sqrt_delta = math.sqrt(delta)
		x1 = (-b-sqrt_delta) / (2*a)
		x2 = (-b+sqrt_delta) / (2*a)
		return (x1, x2)
	

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower' and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	#créer une fonction python apd string
	def f(x):
		return eval(function, {"x": x})
	#quad retourne (resultat, erreur)
	result, _ = quad(f, lower, upper)
	return result


if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
