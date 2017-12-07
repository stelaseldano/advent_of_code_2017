import sys

def maze(file_path):
	'''
	Day 5 | Part 2
	Finds the number of steps needed to escape a 'maze'.

	The task: http://adventofcode.com/2017/day/5
	'''

	with open(file_path, 'r') as f:
		steps = 0
		li = []
		i = 0

		# creates a list with numbers from the input
		for line in f:
			li.append(int(line.strip()))

		while True:
			if i < 0 or i >= len(li):
				break
			else:
				new_location = i + li[i]

				if new_location < 0 or new_location > len(li):
					break
				else:
					if li[i] >= 3:
						li[i] -= 1
						i = new_location
						steps += 1
					else:
						li[i] += 1
						i = new_location
						steps += 1


	with open('output', 'w') as f:
		f.write(str(steps))


if __name__ == '__main__':
	maze(sys.argv[-1])