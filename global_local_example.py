#!/usr/bin/python

from contextpy import (
  base, around, activelayer, globalActivateLayer, layer, proceed)

test_a_layer = layer("TestA")
test_b_layer = layer("TestB")

class TestClass:
    @base
    def test(self):
        print "Base\n"
    
    @around(test_a_layer)
    def test(self):
        print "Test A"
        proceed()

    @around(test_b_layer)
    def test(self):
        print "Test B"
        proceed()
    
globalActivateLayer(test_a_layer)

with activelayer(test_b_layer):
    TestClass().test()