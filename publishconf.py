#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

OUTPUT_PATH = 'published/'

SITEURL = 'https://padme-am.ins.uni-bonn.de/'
RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

LINKS = (('Institute for Numerical Simulation', 'https://ins.uni-bonn.de/'),
         ('Institute for Software Technology', 'http://www.dlr.de/sc'),
         ('Access Technology', 'https://access-technology.de/'),
         ('Imprint', 'https://ins.uni-bonn.de/content/impressum'),
         ('Privacy', 'https://ins.uni-bonn.de/content/privacy'))


# Following items are often useful when publishing

# DISQUS_SITENAME = "..."
GOOGLE_ANALYTICS = "UA-134418253-1"
