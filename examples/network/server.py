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


def handle(socket, address):
    stream = Stream(socket)
    status = dict(
        alive=True
    )
    while status['alive']:
        # 必须要启动一个新的greenlet，在greenlet里面执行readline
        # 否则会有内存泄漏
        def spawn_read():
            buf = stream.read_with_checker(bintp.from_buf)
            print buf
            logger.info('closed: %s', stream.closed())
            logger.info('sock: %s', stream.sock)

            if stream.closed():
                status['alive'] = False
                logger.info('client closed')
                # 说明客户端断掉链接了
                return

        logger.error('status: %s', status)
        t = gevent.spawn(spawn_read)
        t.join()


    # 即使不调用close，handle结束也会自动关闭
    #socket.close()

server = StreamServer(('127.0.0.1', 7777), handle)
server.serve_forever()
