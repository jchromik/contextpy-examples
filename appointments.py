#!/usr/bin/python2

from contextpy import (
    layer, base, around, proceed, globalActivateLayer, globalDeactivateLayer,
    activelayers, inactivelayer, inactivelayers)    
from datetime import datetime

time_layer = layer("Time")
location_layer = layer("Location")

class Appointment:
    def __init__(self, datetime=datetime.now(), location="Anywhere"):
        self.datetime = datetime
        self.location = location

    @base
    def __str__(self):
        return self.datetime.strftime(format="%Y-%m-%d")

    @around(time_layer)
    def __str__(self):
        return proceed() + self.datetime.strftime(format=", %H:%M")

    @around(location_layer)
    def __str__(self):
        return proceed() + ", " + self.location

appointment = Appointment()

print "Global Layer Activation:"

print appointment
globalActivateLayer(time_layer)
print appointment
globalActivateLayer(location_layer)
print appointment
globalDeactivateLayer(time_layer)
print appointment
globalDeactivateLayer(location_layer)
print appointment

print "---"
print "Thread-Local Layer Activation:"

with activelayers(time_layer, location_layer):
    print appointment
    with inactivelayer(time_layer):
        print appointment
    with inactivelayer(location_layer):
        print appointment
    with inactivelayers(time_layer, location_layer):
        print appointment
    print appointment
print appointment