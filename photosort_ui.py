from PyQt4 import QtCore, QtGui
import sort_tab
import config_tab
import bannish_tab
import screening_tab
import bucket_tab

###
#Setup main UI window
#Has no functionality except for setting up the GUI.
###

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.tabWidget = QtGui.QTabWidget(self)
        self.tabs = [
            sort_tab.Sort_Tab(self),
            config_tab.Config_Tab(self),
            bannish_tab.Bannish_Tab(self),
            screening_tab.Screening_Tab(self),
            bucket_tab.bucket_tab(self)
        ]

        # tab-order variables
        sort = 1
        config = 0
        bannish = 2
        screening = 3
        bucket = 4

        self.tabs[sort].setObjectName("Config")
        self.tabWidget.addTab(self.tabs[sort], "Config")
        self.tabs[config].setObjectName("Sort")
        self.tabWidget.addTab(self.tabs[config], "Sort")
        self.tabWidget.addTab(self.tabs[bannish],"Duplicates")
        self.tabs[bannish].setObjectName("Duplicates)")
        self.tabWidget.addTab(self.tabs[screening],"Screening")
        self.tabs[screening].setObjectName("Screening")
        self.tabWidget.addTab(self.tabs[bucket],"Bucket")
        self.tabs[bucket].setObjectName("Bucket")


        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.tabWidget)
        self.setLayout(layout)

        # Show yourself
        self.setGeometry(100, 10, 1200, 700)
        self.setWindowTitle("Photosort")
        self.show()

