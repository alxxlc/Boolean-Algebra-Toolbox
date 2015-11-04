# Created by Alex Cote'
# https://github.com/alxxlc/Boolean-Algebra-Toolbox

# Module used for generating truth tables from a given boolean algebra equation.
# Once the module is complete, it will be able to check for multiple types of operators and equation formats.

# Test Equation: (AVB') (AVCVD') (A+B+D')

class ttGenerator():
	def __init__(self):
		self.equationStr = "" # Equation variable that will contain the equation that the truth table is being generated from.

		# Symbols that will be used as operators for the equation
		self.orSymbol = "+"
		self.andSymbol = "&"
		self.notSymbol = "~"
		self.notOrder = "prefix" # Either "prefix" or "sufix"

		self.symbolRegister = []
		self.symbolRegisterVal = []

		self.variableRegister = []

		self.eqLevels = []

	def setEquation(self, tmpNewEquation):
		self.equationStr = str(tmpNewEquation)

	def checkOr(self):
		pass

	def checkAnd(self):
		pass

	def checkIfThen(self):
		pass

	def checkIfOnly(self):
		pass

	def setEqLevels(self):
		tmpEquation = list(self.equationStr)
		curStepLevel = 0

		for curIndex in range(0, len(self.equationStr)):
			if tmpEquation[curIndex] == "(":
				curStepLevel += 1
				self.eqLevels.append(curStepLevel)
			elif tmpEquation[curIndex] == ")":
				self.eqLevels.append(curStepLevel)
				curStepLevel -= 1
			else:
				self.eqLevels.append(curStepLevel)

	def generateTable(self):
		pass