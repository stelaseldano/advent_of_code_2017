import sys

def passphrase(file_path):
	"""
	Finds how many valid passphrases there are in a document.
	A valid passphrase is that in which all the 'words' are different. 

	aa bb cc dd ee - valid.
	aa bb cc dd aa - invalid (the word 'aa' appears more than once)
	aa bb cc dd aaa - valid

	Takes a file as argument and
	creates a file 'output' containing the result.
	"""

	with open(file_path, 'r') as f:
		valids = 0

		for line in f:
			line = line.strip().split()

			for i in range(0, len(line)):
				valid = True

				if line.count(line[i]) > 1:
					valid = False
					break
				else:
					i += 1

			if valid:
				valids += 1

	with open('output', 'w') as f:
		f.write(str(valids))


if __name__ == '__main__':
	passphrase(sys.argv[-1])