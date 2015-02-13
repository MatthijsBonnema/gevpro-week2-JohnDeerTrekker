#!/usr/bin/python3
# File: country2.py
# Author: Matthijs Bonnema and Jeroen Wilkens
# Date: 20/02/2015
# Info: 

import sys


class Country():
    def __init__(self):
        self.country = "None"

    def setcountry(self, country):
        self.country = country

    def __str__(self):
        countries = self.importlist()
        message = "Hello from {0}".format(countries)
        return message

    def importlist(self):
        countrylist = []
        file = open("countries_list.txt")
        for line in file:
            separator = "\n"
            line = line.split(separator)
            for countries in line:
                countrylist.append(countries)
        file.close()
        return countrylist

if __name__ == "__main__":
    country1 = Country()
    country1.setcountry("Holland")

    country2 = Country()
    country2.setcountry("Germany")

    print(country1)
    print(country2)
