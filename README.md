#Boolean Algebra Toolbox
This is just a fairly simple program I am making to help with the time waste that comes with working out simple boolean algebra equation truth tables. When it is completed, the BAT will hold tools that can help with most simple issues when dealing with most types of boolean algebra.

###How To Use This Program
Before using this program for either the convertor or generator, you need to set the operators in the Configure tab. These settings will be used in every function of this program to know what each operator is and how the program should handle these operators when dealing with the equations you enter.

The Converter will use both the "Old Symbols" and "New Symbols" from the Configure tab in order to convert equations into new equations that you can use.

The Generator will look for symbols that you have set in the "New Symbols" settings in order to generate a truth table with the correct type of equation you have entered.

###Prerequisites
This program requires Qt5, PyQt5, and Python 3 in order to run properly.

###How This is Being Developed
I plan to make all the modules used in the program as portable as I can. Both the [ttConverter.py](https://github.com/alxxlc/Boolean-Algebra-Toolbox/blob/master/ttConverter.py) and [ttGenerator.py](https://github.com/alxxlc/Boolean-Algebra-Toolbox/blob/master/ttGenerator.py) can be removed entirely from this program and used separately with other programs.
