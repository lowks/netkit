# -*- coding: utf-8 -*-

from netkit.box import Box

p = Box()
print p
print repr(p.pack())

tp = Box(p.pack())

print tp
