def fib(n):
	index = 0
	a,b = 0,1
	while index < n:
		print(b)
		c = b
		b = a+b
		a = c
		index += 1

fib(7)


def fib_nub_2(n):
	index = 0
	a,b = 0,1
	while index < n:
		yield b
		c = b
		b = a+b
		a = c
		index += 1

for x in fib_nub_2(7):
	print(x)
