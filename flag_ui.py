#!/usr/bin/python3
# File: flag_ui.py
# Author: Matthijs Bonnema
# Date: 2/13/15
# Info: 

from PyQt4 import QtGui
import sys
import flag_color, country


class Country(QtGui.QWidget):
    def __init__(self):
        super(Country, self).__init__()
        grid = QtGui.QGridLayout()
        self.combobox = QtGui.QComboBox(self)
        self.combobox.addItems(country.Country.importlist(self))
        grid.addWidget(self.combobox, 1, 0)
        self.setLayout(grid)

def main():
    app = QtGui.QApplication(sys.argv)
    country = Country()
    country.show()
    app.exec_()

if __name__ == "__main__":
    main()
