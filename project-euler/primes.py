def get_next_prime_number(n=2):
	def is_prime(i):
		if i == 2:
			return True

		for f in range(2, (i - 1)):
			if((i % f) == 0):
				return False
		return True

	while not is_prime(n):
		n += 1
	return n

def prime_gen_trial_div(n):
	def is_prime(i):
		for f in range(3, (i - 1)):
			if not (i % f):
				return False
		return True
	yield 2
	n = 3
	while True:
		while not is_prime(n):
			n += 2
		yield n
		n += 2

def is_prime(n):
	for d in xrange(2, int(n ** 0.5)):
		if not n % d:
			return False	
	else:
		return True

def primes_sieve(n):
	composites = n * [True] 
	composites[0] = composites[1] = False
	for i in xrange(2, int(n ** 0.5), 1):
		if composites[i]:
			print 'Next prime is %s' % i
			for j in range(0, n):
				k = (i**2) + (i * j)
				if k >= n:
					break
				else:
					composites[k] = False
	return [i for i, is_prime in enumerate(composites) if is_prime]

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
	print 'Solution is %s' % is_prime(1383)
main()	
