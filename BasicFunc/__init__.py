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


def gaussian(*, delta_wv, fwhm):
    return _np.exp(-4 * _np.log(2) * delta_wv ** 2 / fwhm ** 2)


def normal_lorentzian(x, x0, fwhm):
    return 1 / 2 / _np.pi * fwhm / ((x - x0) ** 2 + (fwhm / 2) ** 2)


def lorentzian(*, delta_wv, fwhm):
    return 1 / (4 * (delta_wv / fwhm) ** 2 + 1)


def pseudo_voigt(*, delta_wv, fwhm):
    # psedo_voigt
    # base on voigt defination on wiki.
    fG, fL = fwhm['Gaussian'], fwhm['Lorentzian']
    if fL == 0:
        return normal_gaussian(delta_wv, 0, fG)
    if fG == 0:
        return normal_lorentzian(delta_wv, 0, fL)
    _fwhm = (fG ** 5 + 2.69269 * fG ** 4 * fL + 2.42843 * fG ** 3 * fL ** 2 +
             4.47163 * fG ** 2 * fL ** 3 + 0.07842 * fG * fL ** 4 + fL ** 5) ** 0.2
    a = 1.36603 * (fL / _fwhm) - 0.47719 * (fL / _fwhm) ** 2 + 0.11116 * (fL / _fwhm) ** 3
    G_part = normal_gaussian(delta_wv, 0, _fwhm)
    L_part = normal_lorentzian(delta_wv, 0, _fwhm)
    return (1 - a) * G_part + a * L_part
