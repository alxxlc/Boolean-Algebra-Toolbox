# Created by Alex Cote'
# https://github.com/alxxlc/Boolean-Algebra-Toolbox

# This is just a test file used to ensure that ttGenerator.py is working properly.

# Test Equation: (AVB') (AVCVD') (A+B+D')

from ttGenerator import *

testGen = ttGenerator()

testGen.setEquation("(AVB') (AVCVD') (A+B+D')")
testGen.setEqLevels()

print(testGen.eqLevels)