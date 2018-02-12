#!/usr/bin/env python3

"""System utility classes and functions"""

import subprocess

class System(object):
    """Allows calling of system processes as if they were local functions"""
    def __init__(self, method, **extra):
        self.method = method
        self.extra = extra

    def __getattr__(self, name):
        def system_wrapper(*args, **kwargs):
            kwargs.update(self.extra)
            args = (name,) + args
            ret = self.method(args, **kwargs)

            if hasattr(ret, "communicate"):
                output, err = ret.communicate()
                return output
            
            return ret
        return system_wrapper

system = System(subprocess.call)
local = System(subprocess.Popen, stdout = subprocess.PIPE)
