# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fie.ui'
#
# Created: Fri May 31 09:50:27 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(809, 727)
        self.frame = QtGui.QFrame(main)
        self.frame.setGeometry(QtCore.QRect(10, 10, 671, 671))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btn1File = QtGui.QPushButton(main)
        self.btn1File.setGeometry(QtCore.QRect(690, 10, 114, 32))
        self.btn1File.setObjectName(_fromUtf8("btn1File"))
        self.IEslider = QtGui.QSlider(main)
        self.IEslider.setGeometry(QtCore.QRect(290, 690, 171, 28))
        self.IEslider.setMinimum(1)
        self.IEslider.setMaximum(50)
        self.IEslider.setProperty("value", 1)
        self.IEslider.setOrientation(QtCore.Qt.Horizontal)
        self.IEslider.setObjectName(_fromUtf8("IEslider"))
        self.label = QtGui.QLabel(main)
        self.label.setGeometry(QtCore.QRect(10, 690, 271, 28))
        self.label.setObjectName(_fromUtf8("label"))
        self.lbIEValue = QtGui.QLabel(main)
        self.lbIEValue.setGeometry(QtCore.QRect(480, 690, 121, 28))
        self.lbIEValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbIEValue.setObjectName(_fromUtf8("lbIEValue"))
        self.btn2Files = QtGui.QPushButton(main)
        self.btn2Files.setGeometry(QtCore.QRect(690, 50, 114, 32))
        self.btn2Files.setObjectName(_fromUtf8("btn2Files"))

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
        main.setTabOrder(self.btn1File, self.IEslider)

    def retranslateUi(self, main):
        main.setWindowTitle(QtGui.QApplication.translate("main", "FMO Interaction Energies Analyser", None, QtGui.QApplication.UnicodeUTF8))
        self.btn1File.setText(QtGui.QApplication.translate("main", "1 File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("main", "Interaction Energy Threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbIEValue.setText(QtGui.QApplication.translate("main", "1 kcal/mol", None, QtGui.QApplication.UnicodeUTF8))
        self.btn2Files.setText(QtGui.QApplication.translate("main", "2 Files", None, QtGui.QApplication.UnicodeUTF8))

