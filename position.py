class Position:
	def __init__(self, line, column):
		self.line = line
		self.column = column

	def __str__(self):
		strToReturn = "line: " + str(self.line) + "\n"
		strToReturn = strToReturn + "column: " + str(self.column) + "\n"
		return strToReturn

	def __eq__(self, other):
		return (self.line == other.line) and (self.column == other.column)