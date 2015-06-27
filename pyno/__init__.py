#! /usr/bin/python
# -*- coding: utf-8 -*-

import atexit
import inspect
import os

from pync import Notifier

curfile = os.path.abspath(inspect.getfile(inspect.stack()[-1][0]))
notify = lambda: Notifier.notify('Check %s.' % curfile, title='pyno')
atexit.register(notify)
