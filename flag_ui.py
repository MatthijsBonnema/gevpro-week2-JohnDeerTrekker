#!/usr/bin/python3
# File: flag_ui.py
# Author: Matthijs Bonnema and Jeroen Wilkens
# Date: 2/13/15
# Info:

from PyQt4 import QtGui
import sys
import flag_color, country


class Country(QtGui.QWidget):
    def __init__(self):
        super(Country, self).__init__()

        self.initUI()

    def initUI(self):

        self.col = QtGui.QColor(0, 0, 0)

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        self.combobox = QtGui.QComboBox(self)
        self.combobox.addItems(country.Country.importlist(self))
        self.combobox.setCurrentIndex(0)
        self.combobox.currentIndexChanged.connect(self.update_flag)

        grid.addWidget(self.combobox, 1, 0)

        self.flag = QtGui.QFrame(self)
        self.flag.setFixedSize(250, 100)
        self.flag.setStyleSheet("QFrame { background-color: %s}" % self.col.name())

        grid.addWidget(self.flag, 3, 0)

    def update_flag(self):
        self.col = flag_color.FlagColor.random_color(self.col)
        self.flag.setStyleSheet("QFrame { background-color: %s}" % self.col.name())


def main():
    app = QtGui.QApplication(sys.argv)
    country = Country()
    country.show()
    country.setWindowTitle("Country Flags")
    app.exec_()

if __name__ == "__main__":
    main()
