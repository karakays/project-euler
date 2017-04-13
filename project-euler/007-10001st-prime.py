
def get_next_prime(start=2):
	def is_prime(i):
		if i == 2:
			return True

		for f in range(2, (i - 1)):
			if not (i % f):
				return False
		return True

	while True:
		while not is_prime(start):
			start += 1
		yield start
		start += 1

def main():
	r = range(0, 10001)

	g = get_next_prime();

	p = -1

	for i in r:
		p = g.__next__()

	print('Solutions is ', p)	


if __name__ == '__main__':
	main()


