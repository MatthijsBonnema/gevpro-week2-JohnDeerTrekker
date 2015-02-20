#!/usr/bin/python3

# flag_color.py

import sys
from random import randrange
from PyQt4 import QtGui

class FlagColor(QtGui.QColor):

    def _init__(self):
        super(FlagColor, self).__init__()
        self.random_color()

    def random_color(self):
        self.setRed(random.randrange(256))
        self.setGreen(random.randrange(256))
        self.setBlue(random.randrange(256))