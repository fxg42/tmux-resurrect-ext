#!/usr/bin/env python3

import datetime
import humanize
import os

try:
    dirpath = os.path.expanduser('~/.tmux/resurrect')
    filename = os.readlink(os.path.join(dirpath, 'last'))
    filepath = os.path.join(dirpath, filename)
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
    relativemtime = humanize.naturaltime(datetime.datetime.now() - mtime)
    print(relativemtime)

except:
    print('no save file')
