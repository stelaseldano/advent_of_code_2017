import sys

def scanners(file_path):
	"""
	Day 13 | Part 1 & 2
	http://adventofcode.com/2017/day/13

	Takes a file as argument and
	creates 'output_131' containing the result for Part 1
	and 'output_132' with the result for Part 2
	"""

	scanners = {}
	first_scanner = 0
	last_scanner = 0

	def find_scanner_position(d, delay = 0):
		"""
		Takes a dictionary as argument with keys that are of types int
		and changes the position of the scanner depending on the length of the dictionary
		and the cells in each item.
		"""
		for key, value in d.items():
			if len(value) == 0:
				continue
			else:
				cycles, index = divmod(key + delay, len(value) - 1)

				if cycles % 2 == 0:
					d[key] = [0 for j in range(len(d[key]))]
					d[key][index] = 1;
				else:
					d[key] = [0 for j in range(len(d[key]))]
					index = len(value) - 1 - index
					d[key][index] = 1

		return d


	def calculate_damage(d, delay = 0):
		damage = 0
		damage_counter = 0

		"""
		Calculates the damage.
		"""
		for i in range(first_scanner, last_scanner + 1):
			find_scanner_position(d, delay)

			if len(d[i]) > 0 and d[i][0] == 1:
				damage += i * len(d[i])
				damage_counter += 1 
			else:
				continue

		return damage, damage_counter

	# Part 2
	def calculate_delay(d):
		delay = 0

		while True:
			damage_counter = calculate_damage(d, delay)[1]

			if damage_counter == 0:
				break

			delay += 1

		print(delay)
		return delay


	with open(file_path, 'r') as f:

		for line in f:
			line = line.strip().split(":")
			# convert strings to ints
			line[0] = int(line[0].strip())
			line[1] = int(line[1].strip())

			if line[0] < first_scanner:
				first_scanner = line[0]

			if last_scanner < line[0]:
				last_scanner = line[0]

			# put key: value in a dict
			scanners[line[0]] = line[1]

		# prepares the scanners
		for i in range(first_scanner, last_scanner + 1):
			if not i in scanners:
				scanners[i] = []
			else:
				scanners[i] = [0 for j in range(1, scanners[i])]
				scanners[i] = [1] + scanners[i]

		with open('output_131', 'w') as f:
			f.write(str(calculate_damage(scanners)[0]))

		with open('output_132', 'w') as f:
			f.write(str(calculate_delay(scanners)))


if __name__ == '__main__':
	scanners(sys.argv[-1])