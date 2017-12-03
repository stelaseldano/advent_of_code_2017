import sys

def checksum(file_path):
	"""
	Calculates the sum of the differences between the largest
	and the smallest number for each row of a table.

	Example
	-------
	5 1 9 5 // 9 - 1
	7 5 3 // 7 - 5
	2 4 6 8 // 8 - 2

	result 18 (8 + 4 + 6)

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

			line_max = max(line_of_num)
			line_min = min(line_of_num)

			result += line_max - line_min

	with open('output', 'w') as f:
		f.write(str(result))


if __name__ == '__main__':
	checksum(sys.argv[-1])