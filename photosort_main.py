#!/usr/bin/python

import sys
from PyQt4 import QtGui
from photosort_ui import Ui_Form


def main():
    
    app = QtGui.QApplication(sys.argv)
    gui = Ui_Form()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
