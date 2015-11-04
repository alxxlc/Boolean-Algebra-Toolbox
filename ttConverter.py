# Created by Alex Cote'
# https://github.com/alxxlc/Boolean-Algebra-Toolbox

# This is a module that can be used to change one boolean algebra equation into a new equation with a different type of operators.

class ttConverter():
	def __init__(self):
		self.removeSpaces = True
		self.newEquation = ""

		self.changeOrBool = True
		self.oldOr = "+"
		self.newOr = "+"

		self.changeAndBool = True
		self.changeImpliedAndBool = True
		self.oldAnd = "∧"
		self.newAnd = "&"

		self.changeNotBool = True
		self.oldNot = "'"
		self.newNot = "~"
		# Variables used to determine if a not originally was made to go before or after a variable and ensure they are changed to the correct placement.
		self.oldNotOrder = "suffix"
		self.newNotOrder = "prefix"

		self.changeCaseBool = True
		self.newCase = "lower" # Either "capital" or "lower"

		self.oldSymbolList = [self.oldOr, self.oldAnd, self.oldNot]
		self.symbolRegister = []
		self.symbolRegisterVal = []

	def keepSpaces(self, tmpBool):
		self.removeSpaces = (not tmpBool)

	def changeOr(self, tmpBool, tmpOldOr, tmpNewOr):
		self.oldOr = str(tmpOldOr)
		self.newOr = str(tmpNewOr)
		if self.oldOr == self.newOr:
			self.changeOrBool = False
		else:
			self.changeOrBool = tmpBool

	def changeAnd(self, tmpAndBool, tmpImpliedBool, tmpOldAnd, tmpNewAnd):
		self.oldAnd = tmpOldAnd
		self.newAnd = tmpNewAnd
		self.changeImpliedAndBool = tmpImpliedBool
		if self.oldAnd == self.newAnd:
			self.changeAndBool = False
		else:
			self.changeAndBool = tmpAndBool

	def changeNot(self, tmpBool, tmpOldNot, tmpOldOrder, tmpNewNot, tmpNewOrder):
		self.oldNot = tmpOldNot
		self.oldNotOrder = tmpOldOrder
		self.newNot = tmpNewNot
		self.newNotOrder = tmpNewOrder
		if self.oldNot == self.newNot:
			self.changeNotBool = False
		else:
			self.changeNotBool = tmpBool

	def changeCase(self, tmpBool, tmpCase):
		self.changeCaseBool = tmpBool
		self.newCase = tmpCase

	def convertEquation(self, tmpEquation):
		self.newEquation = tmpEquation

		# Anylize the equation and log which characters are operators.
		# Enters as STRING
		self.newEquation = list(self.newEquation)
		for curIndex in range(0, len(self.newEquation)):
			for curSymbol in self.oldSymbolList:
				if self.newEquation[curIndex] == curSymbol:
					self.symbolRegister.append(int(curIndex))
					self.symbolRegisterVal.append(curSymbol)
		self.newEquation = ''.join(self.newEquation)
		# Leaves as STRING

		# Change equation variable case and ensure any alpha symbols are kept the same.
		# Enters as STRING
		if self.changeCaseBool:
			if self.newCase == "lower":
				self.newEquation = self.newEquation.lower()
			elif self.newCase == "captal":
				self.newEquation = self.newEquation.upper()

			self.newEquation = list(self.newEquation)

			for curIndex in range(0, len(self.symbolRegister)):
				self.newEquation[self.symbolRegister[curIndex]] = self.symbolRegisterVal[curIndex]
			self.newEquation = ''.join(self.newEquation)
		# Leaves as STRING

		# Change all the Or symbols in the equation to the new Or symbol
		self.newEquation = self.newEquation.replace(str(self.oldOr), str(self.newOr))

		# Check for and remove any spaces
		# Enters as STRING
		if self.removeSpaces:
			self.newEquation = list(self.newEquation)
			for curChar in self.newEquation:
				if curChar == " ":
					del self.newEquation[self.newEquation.index(curChar)]
		# Leaves as LIST

		# Check for negations and remove spaces.
		# Enters as LIST
		if self.changeNotBool:
			for charNum in range(0, len(self.newEquation)):
				if (self.newEquation[charNum] == "'") or (self.newEquation[charNum] == "’"):
					del self.newEquation[charNum]
					self.newEquation.insert((charNum - 1), "~")
		# Leaves as LIST

		# Check for implied Ands. Ex: (ABC)v(BCD)
		# Enters as LIST
		if self.changeImpliedAndBool:
			loopAgain = True
			while loopAgain == True:
				loopAgain = False
				for charNum in range(1, len(self.newEquation)):
					if charNum == 1:
						lastChar = self.newEquation[0]
					if (self.newEquation[charNum] != str(self.newOr)) and (lastChar != str(self.newOr)):
						if str(lastChar).isalpha() and (str(self.newEquation[charNum]).isalpha() or (self.newEquation[charNum] == "~")):
							self.newEquation.insert(charNum, "&")
							loopAgain = True
						elif (lastChar == ")") and (self.newEquation[charNum] == "("):
							self.newEquation.insert(charNum, "&")
							loopAgain = True
					lastChar = self.newEquation[(charNum)]
		self.newEquation = ''.join(self.newEquation)
		# Leaves as STRING

		# Clear registers in case converter is run again.
		self.symbolRegister = []
		self.symbolRegisterVal = []

		return self.newEquation