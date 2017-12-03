import sys

def checksum(file_path):
	"""
	Finds of the only two numbers in each row where one evenly divides the other.
	Calculates the sum of the division of these two number for every row.

	Example
	-------
	5 9 2 8 // 8 / 2
	9 4 7 3 // 9 / 3
	3 8 6 5 // 6 / 3

	result 9 (4 + 3 + 2)

	Takes a file as argument and
	creates a file 'output' containing the result.
	"""

	with open(file_path, 'r') as f:
		result = 0

		for line in f:
			line = line.strip().split('\n')
			line = line[0].split()
			line_of_num = []

			for i in range(0, len(line)):
				line_of_num.append(int(line[i]))

			for i in range(0, len(line)):
				for j in range(0, len(line)):
					if not i == j and line_of_num[i] % line_of_num[j] == 0:
						result += line_of_num[i] / line_of_num[j]


	with open('output', 'w') as f:
		f.write(str(result))


if __name__ == '__main__':
	checksum(sys.argv[-1])