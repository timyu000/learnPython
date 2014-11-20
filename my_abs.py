def my_abs(x):
	if not isinatance(x,(int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x