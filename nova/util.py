#!/usr/bin/env python3

"""Basic utilities for nova"""

class _superpass(object):
    """Simple object to be a placeholder"""
    def __init__(self, name = "superpass"):
        self.repr = name

    def __getattr__(self, name):
        return self
    
    def __setattr__(self, name, value):
        return

    def __delattr__(self, name):
        return

    def __getitem__(self, name):
        return self

    def __setitem__(self, name, value):
        return

    def __delitem__(self, name):
        return

    def __repr__(self):
        return self.repr

    def __eq__(self, other):
        return True

    def __call__(self, *args, **kwargs):
        return self
superpass = _superpass()
