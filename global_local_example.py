#!/usr/bin/python2

from contextpy import (
  base, around, activelayer, inactivelayer, globalActivateLayer, layer, proceed)

test_a_layer = layer("TestA")
test_b_layer = layer("TestB")

@base
def test():
    print "Base\n"

@around(test_a_layer)
def test():
    print "Test A"
    proceed()
@around(test_b_layer)
def test():
    print "Test B"
    proceed()
    
globalActivateLayer(test_a_layer)

with activelayer(test_b_layer):
    test() # A and B active (A from global, B from local stack)

with activelayer(test_a_layer):
    test() # A active twice (global and local stack)

with inactivelayer(test_a_layer):
    test() # A active anyway (from global stack)