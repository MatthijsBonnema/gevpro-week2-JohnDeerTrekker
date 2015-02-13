#!/usr/bin/python3
# File: flag_ui.py
# Author: Matthijs Bonnema
# Date: 2/13/15
# Info: 

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QComboBox, QDialog, QDoubleSpinBox
from PyQt4.QtGui import QApplication, QGridLayout, QLabel
import sys
import flag_color, country


class Country(QDialog):
    super(Country, self).__init__(parent)
    grid = QGridLayout()
    self.combobox = QComboBox()
    self.combobox.addItems(country.Country.importlist())
    grid.addWidget(self.combobox, 1, 0)

def main(QDialog):
    app = QApplication(sys.argv)
    country = Country()
    country.show()
    app.exec_()

if __name__ == "__main__":
    main()