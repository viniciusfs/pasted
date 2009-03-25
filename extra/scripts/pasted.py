#!/usr/bin/env python
"""
    Pasted command line script

    Usage examples:
        pasted file.txt
        cat file.txt file2.txt | pasted

    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

import sys
import urllib
import urllib2
import re

if sys.stdin.isatty() is True:
    if len(sys.argv) < 2:
        print "Usage: pasted <filename>"
        sys.exit()
    f = open(sys.argv[1], 'r')
else:
    f = sys.stdin

code = f.read()
f.close()

values = { 'code': code }
data = urllib.urlencode(values)
req = urllib2.Request("http://p.oitobits.net/add", data)
response = urllib2.urlopen(req)
html_buffer = response.read()

url_pattern = re.compile("\<h2\>Paste \<a href=\"(?P<URL>.*)\"\>")
url = url_pattern.search(html_buffer).group("URL")

print url
