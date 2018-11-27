class Position:
	def __init__(self, line, column):
		self.line = line
		self.column = column

	def __str__(self):
		"""returns via a print (object): the position (line: \ n column :) of the character in the terminal"""
		strToReturn = "line: " + str(self.line) + "\n"
		strToReturn = strToReturn + "column: " + str(self.column) + "\n"
		return strToReturn

	def __eq__(self, other):
		"""returns false (or true if the compared positions are the same)"""
		return (self.line == other.line) and (self.column == other.column)