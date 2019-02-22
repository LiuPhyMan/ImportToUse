#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  21:41 2019/2/6

@author:    Liu Jinbao
@mail:      liu.jinbao@outlook.com
@project:   ImportToUse
@IDE:       PyCharm
"""

from PyQt5 import QtWidgets as QW
import sys
from BetterQWidgets import (BetterQCheckBox,
                            BetterQDoubleSpinBox,
                            BetterQLabel,
                            BetterQPushButton, BetterQRadioButton)


class Temp(QW.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        self.cenWidget = QW.QWidget()
        self.setCentralWidget(self.cenWidget)

        _layout = QW.QVBoxLayout()
        checkbox = BetterQCheckBox()
        _layout.addWidget(BetterQCheckBox())
        _layout.addWidget(BetterQDoubleSpinBox())
        qlabel = BetterQLabel()
        qlabel.setText('QLabel')
        _layout.addWidget(qlabel)
        qbutton = BetterQPushButton()
        qbutton.setText('QPushButton')
        # qbutton.setStyleSheet("background-color:rgb(230,230,230)")
        _layout.addWidget(qbutton)
        _layout.addWidget(BetterQRadioButton())
        _layout.addStretch(1)

        self.cenWidget.setLayout(_layout)


if __name__ == "__main__":
    if not QW.QApplication.instance():
        app = QW.QApplication(sys.argv)
    else:
        app = QW.QApplication.instance()
    app.setStyle(QW.QStyleFactory.create('Fusion'))
    window = Temp()
    window.show()
    app.exec_()
