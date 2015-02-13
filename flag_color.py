#!/usr/bin/python3

# flag_color.py

import sys
from random import randrange

class FlagColor(QtGui.Qcolor):

    def _init__(self):
        super(FlagColor, self).__init__()

    def random_color(self):
        self.setRed(randrange(0, 255))
        self.setGreen(randrange(0,255))
        self.setBlue(randrange(0, 255))

def main():

if __name__ == "__main__":
    main()
