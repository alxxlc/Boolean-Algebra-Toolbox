# Created by Alex Cote'
# https://github.com/alxxlc/Boolean-Algebra-Toolbox

# This is now just a test file to ensure that ttConverter.py is working properly.

input("\n***Warning***:\nThis program automatically copies and pastes to and from your clipboard. If you have anything important copied, you should save it in an external source before continuing. Press any key to continue. Press Ctrl+C to exit this program.")

import pyperclip
from ttConverter import *

eqConverter = ttConverter()

continueLoop = 1
while continueLoop == 1:
	usrInput = str(input("\nEnter original equation (enter nothing to paste in equation): "))
	if usrInput == "":
		usrInput = pyperclip.paste()

	##### Converting goes here ####
	newEquation = eqConverter.convertEquation(usrInput)

	print("\nOld equation:")
	print(usrInput)
	# Print new equation
	print("New equation:")
	#for charNum in  range(0, len(newEquation)):
	#	print(newEquation[charNum], end="")
	print(newEquation + " (now copied to your clipboard)\n")
	pyperclip.copy(newEquation)

	print("#################################################")