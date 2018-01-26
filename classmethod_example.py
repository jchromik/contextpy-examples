#!/usr/bin/python2

from contextpy import (around, base, proceed, layer, activelayer)

layer_a = layer("A")

class TestClass:
    
    @base
    @classmethod
    def test_method(cls):
        print "Classmethod base."

    @around(layer_a)
    @classmethod
    def test_method(cls):
        print "Classmethod around."

TestClass.test_method()

with activelayer(layer_a):
    TestClass.test_method()