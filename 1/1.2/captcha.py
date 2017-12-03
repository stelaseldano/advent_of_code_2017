import sys

def captcha(file_path):
	"""
	Finds the the sum of all digits that are the same as the digit
	halfway through the number. The digits in the second half are compared to the ones in the first.

	Example
	-------
    1212 produces 6
    1221 produces 0
    123425 produces 4
    123123 produces 12
    12131415 produces 4

	Takes a file as argument and
	creates a file 'output' containing the result.
	"""

	with open(file_path, 'r') as f:
		result = 0

		for line in f:
			line = line.strip()

		for i in range(0, int(len(line)/2)):
			if line[i] == line[i + int(len(line)/2)]:
				result += int(line[i]) * 2
				i += 1
			else:
				i += 1

	with open('output', 'w') as f:
		f.write(str(result))


if __name__ == '__main__':
	captcha(sys.argv[-1])