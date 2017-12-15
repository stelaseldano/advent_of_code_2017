import sys

def villages(file_path):
	"""
	Day 12 | Part 1 & 2
	http://adventofcode.com/2017/day/12

	Finds how many numbers are connected to 0

	Takes a file as argument and
	creates 'output_121' containing the result for Part 1
	and 'output_122' with the result for Part 2
	"""

	villages = {}
	same_group = set()
	group_count = 0

	# finds how many items there are in the same group where
	def find_connections(location):
		same_group.add(location)

		for i in villages[location]:
			# remove the commas if there are such
			if i[-1] == ',':
				i = i[0:-1]

			if i in same_group:
				pass
			else:
				find_connections(i)


	with open(file_path, 'r') as f:
		for line in f:
			line = line.strip().split()
			villages[line[0].strip()] = line[2::]

		# Part 1
		# finds how many items there are in the group where '0' is
		find_connections('0')
		same_group = set(same_group)

		with open('output_121', 'w') as f:
			f.write(str(len(same_group)))

		# Part 2
		while len(villages) > 0:
			same_group = set()
			item = list(villages.keys())
			find_connections(item[0])
			group_count += 1

			for i in same_group:
				del villages[i]

	with open('output_122', 'w') as f:
		f.write(str(group_count))

if __name__ == '__main__':
	villages(sys.argv[-1])
