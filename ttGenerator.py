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
		# This was a bad idea but I'm keeping it in case I can use it for 
		# something else.

		# tmpEquation = list(self.equationStr)
		# curStepLevel = 0
		# baseStepLevel = 0

		# for curIndex in range(len(self.equationStr)):
		# 	if tmpEquation[curIndex] == "(":
		# 		if curStepLevel == 0:
		# 			curStepLevel = baseStepLevel
		# 		curStepLevel += 1
		# 		self.eqLevels.append(curStepLevel)
		# 	elif tmpEquation[curIndex] == ")":
		# 		self.eqLevels.append(curStepLevel)
		# 		curStepLevel -= 1

		# 		if curStepLevel == baseStepLevel:
		# 			# Ensure that different sets of parentheses are seen as separate parts.
		# 			baseStepLevel = max(self.eqLevels)
		# 			curStepLevel = 0
		# 	else:
		# 		self.eqLevels.append(curStepLevel)

	def generateTable(self):
		pass

# Design:

# This should probably have some small function that anylizes the equation 
# and ensures that there is no improper syntax. Once the generating begins, 
# it might be best to have a recursive function that generates a truth value 
# for each set of parentheses and calls itself again if there is a nested 
# equation enclosed in parentheses.

# I'm not sure how well this will work out but it seems a lot better than my 
# original plan.