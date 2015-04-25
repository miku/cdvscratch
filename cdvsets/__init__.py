# coding: utf-8

import logging
import os
import tempfile

tempfile.tempdir = os.environ.get('CDV_TMPDIR', '/Volumes/Data/tmp')
logging.getLogger().setLevel(logging.ERROR)

__version__ = '0.0.1'
