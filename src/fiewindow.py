from PyQt4 import QtGui, QtCore

from fie_ui import Ui_main
from fiecanvas import FIECanvas
from fie import FIE

class MainForm(QtGui.QMainWindow):
    """ The main window. All events are taken care
        of here.
    """
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.c = FIECanvas(self.ui.frame, 100.0)
        self.data = None

    """
    USE DECORATORS TO SELECT THE CORRECT NUMBER OF SLOTS
    http://www.eurion.net/python-snippets/snippet/Connecting%20signals%20and%20slots.html
    """
    @QtCore.pyqtSlot()
    def on_btn1File_clicked(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        if len(filename) == 0: return
        if self.data is None:
            self.data = FIE(filename)
            #self.data = FIE("/home/cstein/1-3-uco-opt-pm6-1.0-15-001.log")
            #d1 = FIE("/home/cstein/1-3-uco-opt-pm6-1.0-15-001.log")
            #d2 = FIE("/home/cstein/1-3-uco-opt-pm6-1.0-15-005.log")
            #self.data = d2 - d1
            #self.data = d1

        self.on_IEslider_sliderReleased()

    @QtCore.pyqtSlot()
    def on_btn2Files_clicked(self):
        file1 = QtGui.QFileDialog.getOpenFileName(self, 'Open File 1')
        file2 = QtGui.QFileDialog.getOpenFileName(self, 'Open File 2')
        if len(file1) == 0 or len(file2) == 0: return
        if self.data is None:
            d1 = FIE(file1)
            d2 = FIE(file2)
            self.data = d2 - d1

        self.on_IEslider_sliderReleased()

    @QtCore.pyqtSlot()
    def on_IEslider_sliderReleased(self):
        value = self.ui.IEslider.value()
        self.ui.lbIEValue.setText("%3i kcal/mol" % (value))
        if self.data is not None:
            self.c.set_data(self.data.toSquareMap())
            self.c.set_clim(value)
            self.c.set_axislim(1,302)
        self.c.redraw()

#    @QtCore.pyqtSlot()
#    def on_IEslider_valueChanged(self, value):
#        lbIEValue.setText("LOL")
#        print "LOL"
#        if self.data is not None:
#            self.c.set_data(self.data.toSquareMap())
#            self.c.set_clim(value)
#            self.c.set_axislim(1,302)
#        self.c.redraw()
