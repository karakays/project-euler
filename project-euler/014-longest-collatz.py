def collatz_gen(n):
	non_local_n = [n]
	def collatz_next():
		while non_local_n[0] != 1:
			if non_local_n[0] % 2:
				on_local_n[0] =  non_local_n[0] * 3 + 1
			else:
				non_local_n[0] = non_local_n[0] / 2	
			yield non_local_n[0]
	return collatz_next()

def get_collatz_seq_len(n):
	l = 0
	collatz_gen_func = collatz_gen(n)
	for c in collatz_gen_func:
		l = l + 1
	return l 

def main():
	max_len = 0
	for i in xrange(1000000, 1, -1):
		l = get_collatz_seq_len(i)
		if l > max_len:
			print l, i
			max_len = l

if __name__ == '__main__':
	main()
