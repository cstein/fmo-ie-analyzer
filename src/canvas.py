from time import sleep

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.rcParams.update({'font.size': 8})

class Canvas(FigureCanvas):
    def __init__(self,parent,dpi=300.0):
        size = parent.size()
        self.dpi = dpi
        self.width = size.width() / dpi
        self.height = size.height() / dpi
        self.figure = Figure(figsize=(self.width, self.height), dpi=self.dpi, facecolor='white', edgecolor='k', frameon=True)
        self.figure.subplots_adjust(left=0.00, bottom=0.00, right=1, top=1, wspace=None, hspace=None)
        # left, bottom, width, height
        self.axes = self.figure.add_axes([0.10,0.15,0.80,0.80])
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        self.axes.set_axis_off()
        self.axcb = self.figure.add_axes([0.1,    0.05, 0.8, 0.05])
        self.axcb.set_xticks([])
        self.axcb.set_yticks([])
        FigureCanvas.__init__(self, self.figure)
        self.updateGeometry()
        self.draw()
        self.setParent(parent)

    def on_pre_draw(self):
        pass

    def on_draw(self):
        raise NotImplementedError

    def on_post_draw(self):
        sleep(0.005)

    def redraw(self):
        self.on_pre_draw()
        self.on_draw()
        self.on_post_draw()
