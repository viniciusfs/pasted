"""
    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

import os
import web

from sqlobject import sqlhub, connectionForURI
from pasted.controller import *
from pasted.model import Pasted

urls = (
    '/', 'index',
    '/add', 'add',
    '/view/(\d+)', 'view',
    '/view/(\d+)(.\w+)', 'view',
    '/reply/(\d+)', 'add',
    '/reply/add', 'add',
    '/diff/(\d+)/(\d+)', 'diff',
    '/diff/(\d+)/(\d+)/(\w+)', 'diff',
    '/latest', 'latest',
    '/about', 'about',
    '/help', 'help'
)

CWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB = 'db/pasted.db'
DB_FULLPATH = os.path.join(CWD, DB)

sqlhub.processConnection = connectionForURI('sqlite://%s' % DB_FULLPATH)

if not os.path.isfile(DB_FULLPATH):
    os.mkdir(os.path.join(CWD, 'db'))
    Pasted.createTable()

TEMPLATES = 'templates'
TEMPLATES_FULLPATH = os.path.join(CWD, TEMPLATES)

render = web.template.render(TEMPLATES_FULLPATH)

URLS_LIMIT = 10
URLS_PERCENTAGE = 25
