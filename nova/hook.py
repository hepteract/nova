"""Simple API for registering hooks"""

class HookTarget(object):
    def __init__(self, *args, **kwargs):
        self.hooks = ()

        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        self.hooks += (func,)
        return func

    def run(self, *args, **kwargs):
        args = self.args + args
        if "check" in kwargs:
            check = False
            for hook in self.hooks:
                if hook(*args, **self.kwargs) == kwargs["check"]:
                    check = True
            return check
        else:
            for hook in self.hooks:
                hook(*args, **self.kwargs)
            return
