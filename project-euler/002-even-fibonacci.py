#!/usr/bin/env python3.5
from performance import log_performance as log_perform

indent = 0
fibo_memoize = []


def log(func):
	print('Calling ' + func.__name__)
	x = func()
	return x

@log
def hello():
	return 'Hello there...'
	
def fibo_series_recursive(elem):
	global indent

	if(elem == 0):
		return 0
	elif(elem == 1):
		return 1
	
	indent = indent + 1

	#print('{0:>{1}}Calling fibo({2}) + fibo({3})'.format(' ', 0, elem - 1, elem - 2))
	
	x = fibo_series_recursive(elem - 1) + fibo_series_recursive(elem - 2)

	#print('{0:>{1}}returns {2}'.format(' ', 0, x))

	return x


def fibo_series(limit):
	a = 0
	b = 1
	while(a + b < limit):
		yield(a + b)
		c = a
		a = b
		b = b + c
	return None

@log_perform
def fibo_series_even_sum_recursive(limit):
	sum = 0
	elem = 1
	while(True):
		x = fibo_series_recursive(elem)

		print('{0}th returned: {1}'.format(elem, x))

		if(x >= limit):
			return sum			

		if((x % 2) == 0):
			sum = sum + x
		
		elem = elem + 1

@log_perform
def fibo_series_even_sum(limit):
	sum = 0
	for i in fibo_series(limit):
		if((i % 2) == 0):
			sum = sum + i
	
	return sum

def counter():
	i=0
	def inner():
		#nonlocal i
		i = i + 1
		return i	 

	return inner

def main():
	print('Answer with recursive is %s' % fibo_series_even_sum_recursive(4000000))
	print('Answer with generator is {0}'.format(fibo_series_even_sum(4000000)))

if __name__ == '__main__':
	main()
