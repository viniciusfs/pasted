#!/usr/bin/env python
"""
    Copyright (c) 2008 Vinicius de F. Silva <viniciusfs@gmail.com>

    This file is part of Pasted source code.
    Website: <http://p.oitobits.net/>

    A script that pastes stuff into Pasted from command line.
"""
import sys, urllib, urllib2, re

if sys.stdin.isatty() is True:
    if len(sys.argv) < 2:
        print "Usage: pasted <filename>"
        sys.exit()
    f = open(sys.argv[1], 'r')
else:
    f = sys.stdin

code = f.read()
f.close()

code = unicode(code)

values = { 'code': code }
data = urllib.urlencode(values)
req = urllib2.Request("http://p.oitobits.net/add", data)
response = urllib2.urlopen(req)
html_buffer = response.read()

url_pattern = re.compile("\<h2\>Paste \<a href=\"(?P<URL>.*)\"\>")
url = url_pattern.search(html_buffer).group("URL")

print url
