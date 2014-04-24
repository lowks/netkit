# -*- coding: utf-8 -*-

from netkit import bintp


p = bintp.new()
p.body = '我爱你'
print p
print repr(p.pack())
print p.body

q = bintp.from_buf(p.pack())
print q
print q.body
print q.magic
