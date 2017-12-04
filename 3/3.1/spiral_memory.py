import math
import sys

def spiral_memory(file_path):
	"""
	Finds the shortest distance from a number to the middle of the table the numbers form.
	Each num is allocated in a spiral pattern starting at a location marked 1
	and then counting up while spiraling outward.

	Example
	-------
	17  16  15  14  13
	18   5   4   3  12
	19   6   1   2  11
	20   7   8   9  10
	21  22  23---> ...

	1 needs 0 steps to get to 1
	12 needs 3 steps to get to 1
	23 - 2 steps
	1024 - 31 steps

	Takes a file as argument and
	creates a file 'output' containing the result.
	"""

	with open(file_path, 'r') as f:
		result = 0
		breakpoints = [1]
		middles = []

		# gets the number from the file and keeps it in var number
		for line in f:
			number = int(line.strip())

		# creates a list that contains the last numbers for each spiral circle
		while number > breakpoints[-1]:
			breakpoints.append(math.pow(breakpoints[-1]**(1/2) + 2, 2))

		# gets the first middle point
		middles = [int(breakpoints[-1] - ((breakpoints[-1]**(1/2) - 1) / 2))]

		# adds the other 3 middle points
		for i in range(0, 3):
			middles.append(int(middles[-1] - (breakpoints[-1]**(1/2) - 1)))

		# the distance to the outer circle
		distance = breakpoints[-1]**(1/2) - 1

		# the distance from the number to the closest middle point in the outer circle 
		for i in range(0, len(middles)):
			if distance > abs(middles[i] - number):
				distance = abs(middles[i] - number)

		# the sum of the distance to the outer circle and the distance
		# from the closest middle point to the number
		result = distance + len(breakpoints) - 1

	with open('output', 'w') as f:
		f.write(str(result))


if __name__ == '__main__':
	spiral_memory(sys.argv[-1])