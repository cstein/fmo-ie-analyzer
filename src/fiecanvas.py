from numpy import array, where, abs
from numpy.random import random

from canvas import Canvas

import customcolormap

class FIECanvas(Canvas):
    """
    """
    def __init__(self,parent,dpi=100.0):
        Canvas.__init__(self,parent,dpi)
        self.has_data = False
        self.sqplot = None
        self.cb = None
        self.colormap = customcolormap.make_colormap("mymap", 1.0, 0.001, 10)
        self.cmaplimits = 2.0

    def reinitialize(self):
        self.redraw()

    def set_data(self, data):
        if not self.has_data:
            self.data = data
            self.has_data = True

    def set_clim(self,value):
        self.cmaplimits = float(value)

    def set_axislim(self,i,j):
        self.ifg = i-1
        self.jfg = j-1

    def on_draw(self):
        if not self.has_data: return
        self.axes.clear()
        self.sqplot = self.axes.imshow(self.data, cmap=self.colormap, interpolation='nearest')
        self.sqplot.set_clim(-self.cmaplimits,self.cmaplimits)
        self.axes.set_xlim((self.ifg, self.jfg))
        self.axes.set_ylim((self.ifg, self.jfg))
        self.axes.set_xticks(range(self.ifg+1, self.jfg+1, 20))
        self.axes.set_yticks(range(self.ifg+1, self.jfg+1, 10))
        self.axes.tick_params(axis='both', direction='out')
        self.axes.get_xaxis().tick_bottom()
        self.axes.get_yaxis().tick_left()

        #print self.axes.get_xticks()
        #print self.axes.get_xlabels()
        #self.axes.set_xticks(range(302))
        #self.axes.set_yticks([])
        #self.axes.set_axis_off()
        #if self.cb is None:
        self.cb = self.figure.colorbar(self.sqplot, cax=self.axcb, orientation='horizontal')
        #self.axes.draw_artist(self.sqplot)
        self.draw()
