# -*- coding: utf-8 -*-

from netkit.box import Box


p = Box()
p.body = '我爱你'
print p
print repr(p.pack())
print p.body

q = Box(p.pack())
print q
print q.body
print q.magic
