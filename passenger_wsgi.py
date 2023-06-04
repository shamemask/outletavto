import sys

import os

INTERP = os.path.expanduser("/var/www/u2040455/data/venv/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from manage import application