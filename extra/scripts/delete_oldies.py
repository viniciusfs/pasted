#!/usr/bin/env python
"""
    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

import datetime
import logging

from pasted.model import Pasted

LOG_FILENAME = '/tmp/pasted-delete.log'

logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

seven_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)
seven_days_ago = seven_days_ago.strftime("%Y-%m-%d %H:%M")

logging.info('Starting maintenance at %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

list_old = Pasted.select(Pasted.q.viewed_at < seven_days_ago)

for paste in list_old:
    logging.info('Deleting entry %d, last viewed at %s' % (paste.id, paste.viewed_at))
    paste.destroySelf()
