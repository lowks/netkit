# -*- coding: utf-8 -*-

from netkit import bintp

p = bintp.new()
print p
print repr(p.pack())

print bintp.from_buf(p.pack())
