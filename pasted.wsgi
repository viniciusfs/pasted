"""
    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

import sys
import site
import os

CWD = os.path.dirname((os.path.abspath(__file__)))
VIRTUALENV = os.path.join(CWD, 'ENV')
PACKAGES = os.path.join(VIRTUALENV, 'lib/python2.5/site-packages')

sys.path.insert(0, CWD)
site.addsitedir(PACKAGES)

from pasted_start import *
application = get_wsgi()
