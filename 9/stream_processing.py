import sys

def stream_processing(file_path):
	"""
	Day 9 | Part 1 & 2
	http://adventofcode.com/2017/day/9

	Removes garbage blocks from a stream (string of chars)
	and finds how many valid blocks of data there are in the stream.

	Takes a file as argument and
	creates 'output_91' containing the result for Part 1
	and 'output_92' with the result for Part 2
	"""

	with open(file_path, 'r') as f:

		# prepares the date from the file
		for line in f:
			old_stream = line.strip()
			# a string with the cancelled chars removed 
			cleaner_stream = ''
			# 
			cleanest_stream = ''
			# cancelled chars flag
			skip_next = False
			# garbage flag
			skip_while = False
			# nesting info for counting the groups
			nesting = 0
			# groups
			groups = 0

			# Part 2
			# garbage chars counter
			garbage_count = 0

			# removes the '!' and the next char from the stream
			for char in range(0, len(old_stream)):
				if skip_next:
					skip_next = False
					continue

				if old_stream[char] == '!':
					skip_next = True
				else:
					cleaner_stream += old_stream[char]

			# removes the garbage
			for char in range(0, len(cleaner_stream)):
				# while skip_while is True if the char is not '>' the iteration continues
				if skip_while:
					if cleaner_stream[char] == '>':
						skip_while = False
					else:
						garbage_count += 1
						continue

				# if the char is '<', skip while is set to True
				if cleaner_stream[char] == '<':
					skip_while = True
				elif cleaner_stream[char] == '>':
					continue
				else:
					cleanest_stream += cleaner_stream[char]

			# counts the groups
			for char in cleanest_stream:

				if char == '{':
					nesting += 1

				if char == '}':
					groups += nesting
					nesting -= 1


	with open('output_91', 'w') as f:
		f.write(str(groups))

	with open('output_92', 'w') as f:
		f.write(str(garbage_count))

if __name__ == '__main__':
	stream_processing(sys.argv[-1])