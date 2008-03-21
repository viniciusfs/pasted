"""
    Copyright (c) 2008 Vinicius de F. Silva <viniciusfs@gmail.com>

    This file is part of Pasted source code.
    Website: <http://p.oitobits.net/>

"""
import os
from sqlobject import *

db = 'db/pasted.db'
cwd = os.getcwd()
fullpath = os.path.join(cwd, db)

sqlhub.processConnection = connectionForURI('sqlite://%s' % fullpath)

class Pasted(SQLObject):
    code = StringCol()
    md5 = StringCol()
    viewed_at = StringCol()
    parent = StringCol()
