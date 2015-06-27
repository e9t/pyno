#! /usr/bin/python
# -*- coding: utf-8 -*-

import atexit
import inspect
import os

from pync import Notifier

stack = inspect.stack()
if 'ipython' not in stack[-1][1]:
    curfile = os.path.abspath(inspect.getfile(stack[-1][0]))
    notify = lambda: Notifier.notify('Check %s.' % curfile, title='pyno')
    atexit.register(notify)
