import csv, sys

class Reader:
	"""Reads file contents"""

	def csv(filepath, delimiter=','):
		with open(filepath, 'r') as c:
			return [row for row in csv.reader(c, delimiter=delimiter, skipinitialspace=True)]

	def text(filepath):
		with open(filepath, 'r') as file:
			body = file.read()
		return body

if __name__ == '__main__':
	Reader.csv(sys.argv[1])

