import sys

def memory_relocation(file_path):
	"""
	Day 6 | Part 1 & Part 2
	http://adventofcode.com/2017/day/6

	Takes a file as argument and
	creates a file 'output_61' containing the result for Part 1
	and a file named 'output_62' with the result for Part 2
	"""

	with open(file_path, 'r') as f:

		# prepares the date from the file
		for line in f:
			li = line.strip().split()

		# converts the stringss into ints
		li = list(map(int, li))

		# Part 1: a list that contains all the seen configurations before
		seen = []
		# Part 2: a list with all seen configs plus the given list
		seen_cycles = [list(li)]

		# if the configuraiton hasn't been seen before, the largest block is redistributed
		while seen.count(li) <= 1:
			location = li.index(max(li))
			value = int(li[location])
			start = location + 1
			end = location +  value + 1

			li[location] = 0

			for i in range(start, end):
				if i < len(li):
					li[i] += 1
				else:
					new_loc = i % len(li)
					li[new_loc] += 1

			seen.append(list(li))
			seen_cycles.append(list(li))

		# Part 2
		# cycles calculator
		if seen_cycles.count(li) == 2:
			# minus 1 because the last item appears twice in the list
			cycles = len(seen_cycles) - seen_cycles.index(li) - 1
	

	with open('output_61', 'w') as f:
		f.write(str(len(seen)))

	with open('output_62', 'w') as f:
		f.write(str(cycles))

if __name__ == '__main__':
	memory_relocation(sys.argv[-1])