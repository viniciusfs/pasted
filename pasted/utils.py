"""
    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

import hashlib
import difflib
import re

from pasted.config import URLS_LIMIT
from pasted.config import URLS_PERCENTAGE

def calc_md5(code):
    md5 = hashlib.md5()
    md5.update(code)
    return md5.hexdigest()

def create_udiff(original, new):
    udiff = difflib.unified_diff(
        original.code.splitlines(),
        new.code.splitlines(),
        fromfile='Paste #%d' % original.id,
        tofile='Paste #%d' % new.id,
        lineterm='',
        n=4)
    udiff = '\n'.join(udiff)
    return udiff

def render_udiff(udiff):
    change_pattern = re.compile(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@')

    lines = udiff.splitlines()
    line_iter = iter(lines)

    mods = {}

    try:
        line = line_iter.next()
        mods['old'] = line[4:]
        line = line_iter.next()
        mods['new'] = line[4:]

        mods['lines'] = []

        line = line_iter.next()

        while True:
            match = change_pattern.match(line)
            if match is not None:
                old_line, old_end, new_line, new_end = [int(x or 1) for x in match.groups()]
                old_line -= 1
                new_line -= 1
                old_end += old_line
                new_end += new_line

                line = line_iter.next()

                while old_line < old_end or new_line < new_end:
                    old_change = new_change = False
                    command, content = line[0], line[1:]

                    if command == ' ':
                        old_change = new_change = True
                        action = 'none'
                    elif command == '-':
                        old_change = True
                        action = 'del'
                    elif command == '+':
                        new_change = True
                        action = 'add'

                    old_line += old_change
                    new_line += new_change

                    mods['lines'].append({
                        'old_line': old_change and old_line or u'',
                        'new_line': new_change and new_line or u'',
                        'action': action,
                        'content': content
                        })

                    line = line_iter.next()
    except StopIteration:
        pass

    return mods

def is_spam(paste):
    urlfind = re.compile("[A-Za-z]+://.*?")
    urls = urlfind.findall(paste)
    url_count = len(urls)

    if url_count > URLS_LIMIT:
        return True
    else:
        word_count = len(paste.split())
        urls_percentage = (url_count * 100) / word_count
        
        if urls_percentage > URLS_PERCENTAGE:
            return True
        else:
            return False
