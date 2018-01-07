#!/usr/bin/python2

from contextpy import base, around, activelayer, layer, proceed

employerLayer = layer("Employer")

class Person(object):
    def __init__(self, name, employer):
        self.name = name
        self.employer = employer

    @base
    def getDetails(self):
        return self.name

    @around(employerLayer)
    def getDetails(self):
        return proceed() + "\n" + self.employer

person = Person("Michael Perscheid" , "HPI")

print person.getDetails()

with activelayer(employerLayer):
    print person.getDetails()
