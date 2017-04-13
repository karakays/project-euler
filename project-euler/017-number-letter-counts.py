base_dict = {1: '', 2: 'HUNDRED', 3: 'THOUSAND'}

cardinals = {0: '',  1: 'ONE',	2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE',
		10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN',
		17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN',
		20: 'TWENTY', 30: 'THIRTY', 40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY', 80: 'EIGHTY',
		90: 'NINETY'}

def find_base(n):
	num = n
	base = 0
	while num / 10:
		num /= 10
		base += 1
	return base

def articulate_num(n):
	numeral = ''
	base = find_base(n)
	if base == 2:
		digit = n / 10 ** base
		numeral = cardinals[digit] + ' ' +  base_dict[base]
		n -= digit * 10 ** base
		if n:
			numeral += ' AND '
	
	if n >= 20:
		numeral += cardinals[n - n % 10] + '-' +  cardinals[n % 10]
	elif n > 0:
		numeral += cardinals[n]

	return numeral

def main():
	art = ''
	for i in range(1, 1000):
		num = articulate_num(i)
		#print('%s: %s (%s)') % (i, num, len(num))
		art += num
	art += 'ONE THOUSAND'

	trimmed = art.replace('-', '').replace(' ', '')
	print len(trimmed)

if __name__ == '__main__':
	main()
