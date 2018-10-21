#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 14:13 2018/9/30

@author:    Liu Jinbao
@mail:      liu.jinbao@outlook.com
@project:   ImportToUse
@IDE:       PyCharm
"""

from PyQt5 import QtWidgets as QW
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import Qt, QSize
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

_DEFAULT_FONT = QFont("Ubuntu", 10)


class BetterQPushButton(QW.QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setFont(_DEFAULT_FONT)
        self.setStyleSheet(':hover {background-color: #87CEFA ;}')


class BetterQDoubleSpinBox(QW.QDoubleSpinBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(_DEFAULT_FONT)


class BetterQLabel(QW.QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(_DEFAULT_FONT)


class BetterQRadioButton(QW.QRadioButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = QFont('Ubuntu', 10)
        self.setFont(font)
        self.setCursor(QCursor(Qt.PointingHandCursor))


class BetterQCheckBox(QW.QCheckBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))


class PlotCanvas(FigureCanvas):

    def __init__(self, parent, _figure):
        FigureCanvas.__init__(self, _figure)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QW.QSizePolicy.Expanding, QW.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class QPlot(QW.QWidget):

    def __init__(self, parent=None, figsize=(5, 4), dpi=100):
        super().__init__(parent)
        self.figure = Figure(figsize=figsize, dpi=dpi)
        self.canvas = PlotCanvas(parent, self.figure)
        self.canvas.setFixedSize(figsize[0] * dpi, figsize[1] * dpi)
        layout = QW.QHBoxLayout(parent)
        toolbar = NavigationToolbar(self.canvas, parent=parent, coordinates=False)
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setOrientation(Qt.Vertical)
        toolbar.update()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
