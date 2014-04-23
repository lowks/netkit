# -*- coding: utf-8 -*-

import bintp


p = bintp.new()
p.body = '我爱你'
print p
print repr(p.pack())
print p.body

buf = p.pack()

for i in range(bintp.HEADER_LEN, len(buf)+1):
    tmp_buf = buf[0:i]

    ret, q = bintp.from_buf(tmp_buf)
    print ret, q
