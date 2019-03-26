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
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

_DEFAULT_FONT = QFont("Ubuntu", 10)


class BetterQPushButton(QW.QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setFont(_DEFAULT_FONT)
        self.setStyleSheet('QPushButton{background-color:#E1ECF7;}'
                           'QPushButton:hover {background-color: #87CEFA ;}')


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
        self.setFont(_DEFAULT_FONT)
        self.setCursor(QCursor(Qt.PointingHandCursor))


class BetterQCheckBox(QW.QCheckBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))


class ReadFileQWidget(QW.QWidget):
    pathChanged = pyqtSignal()
    toReadFile = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._label = BetterQLabel('FileDir')
        self._entry = QW.QLineEdit()
        self._entry.setEnabled(True)
        self._entry.setMinimumWidth(600)
        self._entry.setCursor(QCursor(Qt.IBeamCursor))
        self._entry.setFont(QFont("Ubuntu", 12))
        self._browse = BetterQPushButton("BROWSE")
        self._read_button = BetterQPushButton("READ")
        self._set_layout()
        self._set_connect()
        self._set_slot()

    def path(self):
        return self._entry.text()

    def _set_layout(self):
        _layout = QW.QHBoxLayout()
        _layout.addWidget(self._label)
        _layout.addWidget(self._entry)
        _layout.addWidget(self._browse)
        _layout.addWidget(self._read_button)
        _layout.addStretch(1)
        self.setLayout(_layout)

    def _set_connect(self):
        self._browse.clicked.connect(self._browse_callback)

    def _browse_callback(self):
        pass
        # _path = QW.QFileDialog.getOpenFileName(caption='Open File',
        #                                        filter="spec file (*.asc)")[0]
        # shorten_path = re.fullmatch(r".*(/[^/]+/[^/]+/[^/]+.asc)", _path).groups()[0]
        # self.path = _path
        # self._entry.setText(shorten_path)

    def _set_slot(self):
        def slot_emit():
            self.toReadFile.emit()

        self._read_button.clicked.connect(slot_emit)


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
        self.toolbar = NavigationToolbar(self.canvas, parent=parent, coordinates=False)
        self.toolbar.setIconSize(QSize(16, 16))
        self.toolbar.setOrientation(Qt.Vertical)
        self.toolbar.update()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)


class SciQDoubleSpinBox(QW.QWidget):
    valueChanged = pyqtSignal()

    def __init__(self, *, node_range):
        super().__init__()
        self._number = BetterQDoubleSpinBox()
        self._node = QW.QComboBox()
        self._node_dict = dict()
        assert node_range[1] > node_range[0]
        for i, v in enumerate([10 ** (_) for _ in range(node_range[0], node_range[1] + 1)]):
            sci_str = "{v:.2e}".format(v=v)
            _number, _node = sci_str.split('e')
            self._node.addItem("1E" + _node)
            self._node_dict["1E" + _node] = i
        self._node.setFont(_DEFAULT_FONT)
        self._set_layout()
        self._set_slot()
        self.setValue(10 ** (node_range[0]))

    def _set_layout(self):
        _layout = QW.QHBoxLayout()
        _layout.addWidget(self._number)
        _layout.addWidget(self._node)
        _layout.addStretch(1)
        self.setLayout(_layout)

    def value(self):
        value = self._number.value() * float(self._node.currentText())
        return value

    def setValue(self, value):
        sci_str = '{v:.2e}'.format(v=value)
        _number, _node = sci_str.split('e')
        self._number.setValue(float(_number))
        assert '1E' + _node in self._node_dict, _node
        _current_index = self._node_dict['1E' + _node]
        self._node.setCurrentIndex(_current_index)

    def _set_slot(self):
        def slot_emit():
            self.valueChanged.emit()

        self._number.valueChanged.connect(slot_emit)
        self._node.currentIndexChanged.connect(slot_emit)
