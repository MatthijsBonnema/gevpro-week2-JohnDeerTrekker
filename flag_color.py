#!/usr/bin/python3

# flag_color.py

import sys
from random import randrange
from PyQt4 import QtGui

class FlagColor(QtGui.QColor):

    def _init__(self):
        super(FlagColor, self).__init__()

    def random_color(self):
        red = self.setRed(randrange(0, 255))
        green = self.setGreen(randrange(0, 255))
        blue = self.setBlue(randrange(0, 255))
        return red, green, blue

if __name__ == "__main__":
    flag = FlagColor()
    red, green, blue = flag.random_color()