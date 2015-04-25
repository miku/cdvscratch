# coding: utf-8
# pylint: disable=C0103,W0232

from gluish.task import BaseTask
import logging
import os

class DefaultTask(BaseTask):
    BASE = os.environ.get('CDV_DATA', '/Volumes/Data/cdv-data')

    def assets(self, path):
        """
        Return the absolute path to the asset. `path` is the relative path
        below the assets root dir.
        """
        return os.path.join(os.path.dirname(__file__), 'assets', path)

    @property
    def logger(self):
        return logging.getLogger('cdv')
