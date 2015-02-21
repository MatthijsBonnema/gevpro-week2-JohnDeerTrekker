#!/usr/bin/python3
# File: flag_color.py
# Author: Matthijs Bonnema and Jeroen Wilkens
# Date: 2/13/15
# Info:

import sys
from random import randrange
from PyQt4 import QtGui

class FlagColor(QtGui.QColor):

    def _init__(self):
        super(FlagColor, self).__init__()

    def random_color(self):
        self.setRed(randrange(256))
        self.setGreen(randrange(256))
        self.setBlue(randrange(256))
        return self
