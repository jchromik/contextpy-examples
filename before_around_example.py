#!/usr/bin/python

from contextpy import base, around, before, after, activelayer, layer, proceed

test_layer = layer("Test")

class TestClass:
    @base
    def test(self):
        print "@base"
    
    @around(test_layer)
    def test(self):
        print "@around"
        proceed()
    
    @before(test_layer)
    def test(self, *args, **kwargs):
        print "@before"
    
    @after(test_layer)
    def test(self, *args, **kwargs):
        print "@after"

with activelayer(test_layer):
    TestClass().test()