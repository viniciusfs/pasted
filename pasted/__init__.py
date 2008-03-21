"""
    Copyright (c) 2008 Vinicius de F. Silva <viniciusfs@gmail.com>

    This file is part of Pasted source code.
    Website: <http://p.oitobits.net/>
"""
import web

from pasted.controller import *

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

web.webapi.internalerror = web.debugerror

def run():
   # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    web.run(urls, globals(), web.reloader)
