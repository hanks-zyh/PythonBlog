#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio,orm
from models import User, Blog, Comment
import logging; logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop = loop,user='root', password='root', db='awesome')
    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
    yield from u.save()

def test():
    logging.info("0")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
for x in test():
    pass
