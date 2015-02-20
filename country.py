#!/usr/bin/python3
# File: country2.py
# Author: Matthijs Bonnema and Jeroen Wilkens
# Date: 20/02/2015
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
        countrylist = []
        file = open("countries_list.txt")
        for line in file:
            separator = "\n"
            line = line.split(separator)
            for countries in line:
                if countries != "":
                    countrylist.append(countries)
        file.close()
        return countrylist

if __name__ == "__main__":
    country = Country()
