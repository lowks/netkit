# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gevent import monkey;monkey.patch_all()

from netkit import bintp
from netkit.stream import Stream
import gevent
from gevent.server import StreamServer
import logging

logger = logging.getLogger('netkit')
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler('s.log'))
logger.setLevel(logging.DEBUG)


class Connection(object):

    def __init__(self, sock, address):
        self.stream = Stream(sock)
        self.process()

    def process(self):
        while not self.stream.closed():
            # 必须要启动一个新的greenlet，在greenlet里面执行readline
            # 否则会有内存泄漏
            def spawn_read():
                message = self.stream.read_with_checker(bintp.from_buf)
                if self.stream.closed():
                    print 'client closed'
                    # 说明客户端断掉链接了
                    return
                print "message, len: %s, content: %r" % (len(message), message)

                ret, tp = bintp.from_buf(message)
                tp.cmd += 1
                self.stream.write(tp.pack())

            t = gevent.spawn(spawn_read)
            t.join()


        # 即使不调用close，handle结束也会自动关闭
        #sock.close()


server = StreamServer(('127.0.0.1', 7777), Connection)
server.serve_forever()
