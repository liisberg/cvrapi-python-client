from functools import partial
from .api import CVRAPI

class CVRAPIClient(object):
    METHODS = ['get', 'post']

    def __init__(self, *args):
        self.api = CVRAPI(*args)

    def __getattr__(self, method):
        return partial(getattr(self.api, 'perform'), method)
