"""
    This file is part of Pasted source code.
    Copyright (c) 2008 2009 by Vinicius Figueiredo <viniciusfs@gmail.com>
"""

import web
import datetime

from pasted.config import *
from pasted.utils import *
from pasted.model import Pasted

class index:
    def GET(self):
        return render.base(render.form())

class about:
    def GET(self):
        return render.base(render.about())

class help:
    def GET(self):
        return render.base(render.help())

class add:
    def POST(self):
        form_input = web.input(_unicode=False)
        if form_input.code.strip():
            hexdigest = calc_md5(form_input.code)

            try:
                paste = Pasted.select(Pasted.q.md5==hexdigest).getOne()
            except:
                try: form_input.parent
                except: form_input.parent = None

                paste = Pasted(code=form_input.code,
                    md5=hexdigest,
                    viewed_at=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
                    parent=form_input.parent)

            web.seeother('/view/'+str(paste.id))
        else:
            web.seeother('/')

    def GET(self, paste_id):
        try:
            original = Pasted.get(paste_id)
        except:
            web.seeother('/')

        return render.base(render.form(original))

class view:
    def GET(self, paste_id, mode=None):
        try:
            paste = Pasted.get(paste_id)
            paste.viewed_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        except:
            web.seeother('/')
            return

        if mode is not None:
            if mode == '.txt':
                web.header('content-type', 'text/plain; charset=utf-8')
                return paste.code
            elif mode == '.colorful':
                colorful_code = syntax_highlight(paste)

                if colorful_code is None:
                    web.seeother('/view/'+str(paste.id))
                else:
                   return render.base(render.view(paste,colorful_code))
        else:
            return render.base(render.view(paste))

class diff:
    def GET(self, original, new, raw=None):
        try:
            original = Pasted.get(original)
            new = Pasted.get(new)
        except:
            web.seeother('/')
            return

        diff = create_udiff(original, new)

        if raw is not None:
            web.header('content-type', 'text/plain; charset=utf-8')
            return diff
        else:
            diff = render_udiff(diff)
            return render.base(render.diff(original, new, diff))

class latest:
    def GET(self):
        latest_pastes = Pasted.select(orderBy=Pasted.q.id).reversed()
        latest_pastes = list(latest_pastes[:5])

        return render.base(render.list(latest_pastes))
