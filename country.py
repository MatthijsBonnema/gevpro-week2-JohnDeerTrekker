#!/usr/bin/python3
# File: country2.py
# Author: Matthijs Bonnema and Jeroen Wilkens
# Date: 2/13/15
# Info: 

import sys
from random import randrange
import flag_color

class Country():
    def __init__(self):
        self.country = "None"
        self.flag = flag_color.FlagColor()

    def setcountry(self, country):
        self.country = country

    def __str__(self):
        countries = self.importlist()
        message = ("{}".format(countries))
        return message

    def importlist(self):
        countrylist=["--Select a Country--"]
        with open('countries_list.txt') as in_f:
            for line in in_f:
                x = line.split('\n')
                countrylist.append(x[0])
        return countrylist




if __name__ == "__main__":
    country = Country()
