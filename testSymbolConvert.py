newEquation = "(AVB') (AVCVD') (A+B+D')"
oldSymbolList = ["+", "V", "Q"]
symbolRegister = []
symbolRegisterVal = []
newCase = "lower"

print(newEquation)
newEquation = newEquation.upper()
newEquation = list(newEquation)

newEquation = list(newEquation)
for curIndex in range(0, len(newEquation)):
	for curSymbol in oldSymbolList:
		if newEquation[curIndex] == curSymbol:
			symbolRegister.append(int(curIndex))
			symbolRegisterVal.append(curSymbol)
newEquation = ''.join(newEquation)

if newCase == "lower":
	newEquation = newEquation.lower()
elif newCase == "captal":
	newEquation = newEquation.upper()

newEquation = list(newEquation)
for curIndex in range(0, len(symbolRegister)):
	newEquation[symbolRegister[curIndex]] = symbolRegisterVal[curIndex]
newEquation = ''.join(newEquation)

print(newEquation)