"""Simple API for registering hooks"""

class HookTarget(object):
    def __init__(self):
        self.hooks = ()

    def __call__(self, func):
        self.hooks += (func,)
        return func

    def run(self, *args, **kwargs):
        for hook in self.hooks:
            hook(*args, **kwargs)
