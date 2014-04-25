# -*- coding: utf-8 -*-

from netkit.bintp import Bintp


p = Bintp()
p.body = '我爱你'
print p
print repr(p.pack())
print p.body

buf = p.pack()

q = Bintp()
for i in range(0, len(buf)+1):
    tmp_buf = buf[0:i]

    if q.unpack(tmp_buf) > 0:
        print q
        break
