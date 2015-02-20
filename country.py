#!/usr/bin/python3
# File: country2.py
# Author: Matthijs Bonnema and Jeroen Wilkens
# Date: 20-02-2015
# Info: 

import sys


class Country():
    def __init__(self):
        self.country = "None"

    def setcountry(self, country):
        self.country = country

    def __str__(self):
        message = "Hello from {0}".format(self.country)
        return message


if __name__ == "__main__":
    country1 = Country()
    country1.setcountry("Holland")

    country2 = Country()
    country2.setcountry("Germany")

    print(country1)
    print(country2)
