import sys

def registers(file_path):
	"""
	Day 8 | Part 1 & 2
	http://adventofcode.com/2017/day/8

	Takes a file as argument and
	creates 'output_91' containing the result for Part 1
	and 'output_92' with the result for Part 2
	"""

	registers = []
	# name: value
	id_value = {}
	largest_val = 0
	largest_val_ever = 0
	change_val = False

	def apply_instructions(direction, name, how_much):
		"""
		if change value is True, then apply the changes
		"""
		if direction == 'dec':
			id_value[name] -= how_much
		elif direction == 'inc':
			id_value[name] += how_much
		else:
			print(direction, ' - no such direction')

	with open(file_path, 'r') as f:
		for line in f:
			line = line.strip().split()
			# converts nums to ints
			line[2] = int(line[2])
			line[6] = int(line[6])
			# adds initial value of that register
			line.append(0)

			# dict of name and current value
			id_value[line[0]] = line[7]
			registers.append(line)

		for i in range(0, len(registers)):
			# the value of the corresponding register
			actual_value = id_value[registers[i][4]]
			# this register's name
			name = registers[i][0]
			# the value actual_value is compared to
			compare_to = registers[i][6]
			# the sign (<, >=, ==..)
			sign = registers[i][5]

			if sign == '==':
				if actual_value == compare_to:
					change_val = True

			elif sign == '>=':
				if actual_value >= compare_to:
					change_val = True

			elif sign == '<=':
				if actual_value <= compare_to:
					change_val = True

			elif sign == '>':
				if actual_value > compare_to:
					change_val = True

			elif sign == '<':
				if actual_value < compare_to:
					change_val = True

			elif sign == '!=':
				if actual_value != compare_to:
					change_val = True
			else:
				print(sign, ' - this sign is missing')

			if change_val:
				apply_instructions(registers[i][1], name, registers[i][2])
				change_val = False

			# finds the largest value ever
			if id_value[name] > largest_val_ever:
				largest_val_ever = id_value[name]

		# finds the largest value after all the instructions are applied
		for key in id_value:
			if id_value[key] > largest_val:
				largest_val = id_value[key]

		with open('output_81', 'w') as f:
			f.write(str(largest_val))

		with open('output_82', 'w') as f:
			f.write(str(largest_val_ever))

if __name__ == '__main__':
	registers(sys.argv[-1])