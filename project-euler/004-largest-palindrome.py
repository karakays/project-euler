import sys
from euler_commons import log_performance as log_perform

def is_palindrome_naive(n):
	s = str(n)

	i = 0
	j = len(s) - 1

	while(i<j):
		if(s[i] != s[j]):
			return False
		i += 1
		j -= 1
	return True

@log_perform
def find_largest_palindrome_naive():
	p = []
	for i in range(999, 99, -1):
		for j in range(i, 99, -1):
			if is_palindrome_naive(i*j):
				p.append(i*j)

	print(p)
	return max(p)

@log_perform
def find_largest_palindrome():
	def is_palindrome(s):
		return s == s[::-1]
	p = []
	for i in range(999, 99, -1):
		for j in range(i, 99, -1):
			if is_palindrome(str(i*j)):
				p.append(i*j)

	print(p)
	return max(p)

def main():
	#a = sys.argv[1]
	print(find_largest_palindrome_naive())
	print(find_largest_palindrome())

if __name__ == '__main__':
	main()
