import sys

def passphrase(file_path):
	"""
	Finds how many passphrases there are
	which contain no two words that are anagrams of each other.
	A passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase 

	abcde fghij - valid
	abcde xyz ecdab - invalid
	a ab abc abd abf abj - valid
	iiii oiii ooii oooi oooo - valid
	oiii ioii iioi iiio - invalid

	Takes a file as argument and
	creates a file 'output' containing the result.
	"""

	with open(file_path, 'r') as f:
		valids = 0

		for line in f:
			line = line.strip().split()
			line = [sorted(i) for i in line]

			for word in line:
				valid = True

				if line.count(word) > 1:
					valid = False
					break

			if valid:
				valids += 1

	with open('output', 'w') as f:
		f.write(str(valids))


if __name__ == '__main__':
	passphrase(sys.argv[-1])