#!/usr/bin/python3

# flag_color.py

import sys
from random import randrange
from PyQt4 import QtGui

class FlagColor(QtGui.QColor):

    def _init__(self):
        super(FlagColor, self).__init__()

    def random_color(self):
        self.setRed(250)
        self.setGreen(randrange(256))
        self.setBlue(randrange(256))
        return self
