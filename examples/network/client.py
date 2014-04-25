# -*- coding: utf-8 -*-

from netkit.bintp import Bintp
from netkit.stream import Stream

import time
import logging
import socket

logger = logging.getLogger('netkit')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

address = ('127.0.0.1', 7777)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

stream = Stream(s)

tp = Bintp()
tp.body = '我爱你'

stream.write(tp.pack())

while True:
    # 阻塞
    buf = stream.read_with_checker(Bintp().unpack)

    if buf:
        rtp = Bintp()
        rtp.unpack(buf)
        print rtp

    if stream.closed():
        print 'server closed'
        break

s.close()
