# -*- coding: utf-8 -*-

from netkit.bintp import Bintp


p = Bintp()
p.body = '我爱你'
print p
print repr(p.pack())
print p.body

q = Bintp(p.pack())
print q
print q.body
print q.magic
