#!/usr/bin/python2

from contextpy import (
  base, around, activelayer, activelayers,
  globalActivateLayer, globalDeactivateLayer, layer, proceed)

a_layer = layer("LayerA")

@base
def test():
    print "Base\n"

@around(a_layer)
def test():
    print "Layer A"
    proceed()

globalActivateLayer(a_layer)
globalActivateLayer(a_layer)
test()
