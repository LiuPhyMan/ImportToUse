#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  15:56 2019/3/14

@author:    Liu Jinbao
@mail:      liu.jinbao@outlook.com
@project:   ImportToUse
@IDE:       PyCharm
"""

from . import constants
import numpy as _np


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("called : {n:.0f} numbers".format(n=self.calls))
        return self.func(*args, **kwargs)


def normal_gaussian(x, x0, fwhm):
    return _np.sqrt(4 * _np.log(2) / _np.pi) / fwhm * _np.exp(
        -4 * _np.log(2) * (x - x0) ** 2 / fwhm ** 2)
