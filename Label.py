from PyQt4 import QtCore, QtGui
import random
import rawpy,imageio
import os
from linkedoutput import linked_output



class Label(QtGui.QLabel):
    def __init__(self, img):
        super(Label, self).__init__()
        self.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)
        self.container = linked_output("")


    def __init__(self):
        super(Label, self).__init__()
        self.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.container = linked_output("")


    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0,0)
        scaledPix = self.pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
        # start painting the label from left upper corner
        point.setX((size.width() - scaledPix.width())/2)
        point.setY((size.height() - scaledPix.height())/2)
        painter.drawPixmap(point, scaledPix)

    # def setPixmap(self, img):
    #     self.pixmap = QtGui.QPixmap(img)

    def setPixmap(self,img):
        ext = os.path.splitext(img)[1]
        if ext == ".CR2" or ext == ".RAW" or ext == ".RAF" or ext == ".NEF" or ext == ".DNG" or ext == ".TIFF" or ext == ".TIF" or ext == ".cr2" or ext == ".raw" or ext == ".raf" or ext == ".nef" or ext == ".dng" or ext == ".tiff" or ext == ".tif" or ext == ".crw" or ext == ".CRW":
            if not self.container.is_linked():
                dirname = os.path.dirname(img)
                self.container.check_or_make("tmp_tiff")
                tiff_file = os.path.join(os.path.dirname(img),"tmp_tiff",os.path.splitext(os.path.basename(img))[0])+".tiff"
                if not os.path.isfile(tiff_file):
                    with rawpy.imread(img) as raw:
                        rgb = raw.postprocess(half_size=True,output_bps=8)
                        imageio.imsave(tiff_file, rgb)
            else:
                tiff_file = os.path.join(self.container.get_bloc(1),str(os.path.splitext(os.path.basename(img))[0])+str(self.container.get_ext(1)))
            img = tiff_file
        self.pixmap = QtGui.QPixmap(img)
