#!/usr/bin/env python3

"""System utility classes and functions"""

import subprocess

class System(object):
    """Allows calling of system processes as if they were local functions"""
    def __init__(self, method):
        self.method = method

    def __getattr__(self, name):
        def system_wrapper(*args, **kwargs):
            args = (name,) + args
            return self.method(args, **kwargs)
        return system_wrapper
system = System(subprocess.call)
