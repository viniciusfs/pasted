"""
    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

import web

from pasted.controller import *
from pasted.config import *

app = web.application(urls, globals())

def get_wsgi():
    return app.wsgifunc()

if __name__ == "__main__":
    app.run()
