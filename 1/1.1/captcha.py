import sys

def captcha(file_path):
	"""
	Finds the the sum of all digits that match the next digit in the list.
	The last digit is compared to the first one.

	Example
	-------
	1122 produces 3
	1111 produces 4
	1234 produces 0
	91212129 produces 9

	Takes a file as argument and
	creates a file 'output' containing the result.
	"""

	with open(file_path, 'r') as f:
		result = 0

		for line in f:
			line = line.strip()

		if line[0] == line[-1]:
			result += int(line[0])

		for i in range(1, len(line)):
			if line[i] == line[i-1]:
				result += int(line[i])
				i += 1
			else:
				i += 1

	with open('output', 'w') as f:
		f.write(str(result))


if __name__ == '__main__':
	captcha(sys.argv[-1])