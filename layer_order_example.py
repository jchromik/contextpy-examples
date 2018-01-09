#!/usr/bin/python2

from contextpy import (
  base, around, activelayer, activelayers,
  globalActivateLayer, globalDeactivateLayer, layer, proceed)

a_layer = layer("LayerA")
b_layer = layer("LayerB")

@base
def test():
    print "Base\n"

@around(a_layer)
def test():
    print "Layer A"
    proceed()
@around(b_layer)
def test():
    print "Layer B"
    proceed()
    
globalActivateLayer(a_layer)
globalActivateLayer(b_layer)
test()
globalDeactivateLayer(b_layer)
globalDeactivateLayer(a_layer)

globalActivateLayer(b_layer)
globalActivateLayer(a_layer)
test()
globalDeactivateLayer(a_layer)
globalDeactivateLayer(b_layer)

with activelayer(a_layer):
    with activelayer(b_layer):
        test()

with activelayer(b_layer):
    with activelayer(a_layer):
        test()

with activelayers(a_layer, b_layer):
    test()

with activelayers(b_layer, a_layer):
    test()
