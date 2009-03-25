"""
    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

from sqlobject import *

class Pasted(SQLObject):
    code = StringCol()
    md5 = StringCol()
    viewed_at = StringCol()
    parent = StringCol()
