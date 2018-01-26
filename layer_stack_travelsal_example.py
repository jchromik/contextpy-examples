#!/usr/bin/python2

from contextpy import (
    base, around, before, after, layer, proceed,
    globalActivateLayer, globalDeactivateLayer)

a_layer = layer("LayerA")
b_layer = layer("LayerB")

@base
def test():
    print "Base"

@around(a_layer)
def test():
    print "Layer A Around"
    proceed()
    print "Layer A Around Continued"

@around(b_layer)
def test():
    print "Layer B Around"
    proceed()
    print "Layer B Around Continued"

@before(a_layer)
def test(*args, **kwargs):
    print "Layer A Before"

@before(b_layer)
def test(*args, **kwargs):
    print "Layer B Before"

@after(a_layer)
def test(*args, **kwargs):
    print "Layer A After"

@after(b_layer)
def test(*args, **kwargs):
    print "Layer B After"

globalActivateLayer(a_layer)
globalActivateLayer(b_layer)
test()
globalDeactivateLayer(b_layer)
globalDeactivateLayer(a_layer)
