# Created by Alex Cote'
# https://github.com/alxxlc/Boolean-Algebra-Toolbox

# Test Equation: (AVB') (AVCVD') (A+B+D')

import sys
from PyQt5 import QtCore, QtWidgets, uic

from ttConverter import *
from ttGenerator import *
import pyperclip

form_class = uic.loadUiType("T3Window.ui")[0]
eqConverter = ttConverter()
tableGenerator = ttGenerator()

oldOrder = "suffix"
newOrder = "prefix"

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)

		# Set symbols in eqConverter object equal to combobox symbols.
		eqConverter.changeOr(False, self.oldOrCombo.currentText(), self.newOrCombo.currentText())
		eqConverter.changeAnd(False, True, self.oldAndCombo.currentText(), self.newAndCombo.currentText())
		eqConverter.changeNot(False, self.oldNotCombo.currentText(), oldOrder, self.newNotCombo.currentText(), newOrder)
		

		# Bind the event listener to the event handler. (convertBtn.clicked listen to convertBtn_Clicked() function)
		self.convertBtn.clicked.connect(self.convertBtn_Clicked)
		self.pasteBtn.clicked.connect(self.pasteBtn_Clicked)
		self.copyBtn.clicked.connect(self.copyBtn_Clicked)
		self.autoBtn.clicked.connect(self.autoBtn_Clicked)

		#Listeners for combo box changes
		self.oldOrCombo.currentIndexChanged.connect(self.orCombo_Changed)
		self.newOrCombo.currentIndexChanged.connect(self.orCombo_Changed)

		self.oldAndCombo.currentIndexChanged.connect(self.andCombo_Changed)
		self.newAndCombo.currentIndexChanged.connect(self.andCombo_Changed)

		self.oldNotCombo.currentIndexChanged.connect(self.notCombo_Changed)
		self.newNotCombo.currentIndexChanged.connect(self.notCombo_Changed)

		self.oldNotOrderCombo.currentIndexChanged.connect(self.notCombo_Changed)
		self.newNotOrderCombo.currentIndexChanged.connect(self.notCombo_Changed)

		# DEBUGGING BUTTONS #
		self.testStringBtn.clicked.connect(self.testStringBtn_Clicked)

	###############
	# CONVERT TAB #
	###############

	def convertBtn_Clicked(self):
		self.newEqTBox.setPlainText(eqConverter.convertEquation(self.oldEqTBox.toPlainText()))

	def pasteBtn_Clicked(self):
		self.oldEqTBox.setPlainText(pyperclip.paste())

	def copyBtn_Clicked(self):
		pyperclip.copy(self.newEqTBox.toPlainText())

	def autoBtn_Clicked(self):
		self.oldEqTBox.setPlainText(pyperclip.paste())
		self.newEqTBox.setPlainText(eqConverter.convertEquation(self.oldEqTBox.toPlainText()))
		pyperclip.copy(self.newEqTBox.toPlainText())

	##############
	# CONFIG TAB #
	##############

	def orCombo_Changed(self):
		if self.oldOrCombo.currentText() == self.newOrCombo.currentText():
			eqConverter.changeOr(False, self.oldOrCombo.currentText(), self.newOrCombo.currentText())
		else:
			eqConverter.changeOr(True, self.oldOrCombo.currentText(), self.newOrCombo.currentText())

	def andCombo_Changed(self):
		if self.oldAndCombo.currentText() == self.newAndCombo.currentText():
			eqConverter.changeAnd(False, True, self.oldAndCombo.currentText(), self.newAndCombo.currentText())
		else:
			eqConverter.changeAnd(True, True, self.oldAndCombo.currentText(), self.newAndCombo.currentText())

	def notCombo_Changed(self):
		if self.oldNotOrderCombo.currentText() == "Before":
			oldOrder = "prefix"
		elif self.oldNotOrderCombo.currentText() == "After":
			oldOrder = "suffix"

		if self.newNotOrderCombo.currentText() == "Before":
			newOrder = "prefix"
		elif self.newNotOrderCombo.currentText() == "After":
			newOrder = "suffix"

		if self.oldNotCombo.currentText() == self.newNotCombo.currentText():
			eqConverter.changeNot(False, self.oldNotCombo.currentText(), oldOder, self.newNotCombo.currentText(), newOrder)
		else:
			eqConverter.changeNot(True, self.oldNotCombo.currentText(), oldOder, self.newNotCombo.currentText(), newOrder)

	###########
	# TESTING #
	###########

	def testStringBtn_Clicked(self):
		self.oldEqTBox.setPlainText("(AVB') (AVCVD') (A+B+D')")

app = QtWidgets.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()