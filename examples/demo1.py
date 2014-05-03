# -*- coding: utf-8 -*-

from netkit.box import Box

box1 = Box()
print box1
print repr(box1.pack())

box2 = Box(box1.pack())

print box2
