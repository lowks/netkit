# -*- coding: utf-8 -*-

from netkit.bintp import Bintp

p = Bintp()
print p
print repr(p.pack())

tp = Bintp(p.pack())

print tp
