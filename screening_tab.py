from PyQt4 import QtCore, QtGui
from Label import Label
from lga import lga
from parent_tab import parent_tab
import os,sys
from linkedoutput import linked_output



class Screening_Tab(QtGui.QWidget,parent_tab):
    def __init__(self,parent):
        super(Screening_Tab, self).__init__(parent= parent)

        # Variables
        self.container = linked_output("")

        # Widgets
        self.buttons = [
            QtGui.QPushButton(),
            QtGui.QPushButton()
        ]
        self.labels = [
            Label()
        ]

        self.labels[0].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/nily.png"))

        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)

        self.buttons[0].setMinimumSize(1, 1)
        self.buttons[0].setText('Wel')
        self.buttons[0].setFont(font)

        self.buttons[1].setMinimumSize(1, 1)
        self.buttons[1].setGeometry(QtCore.QRect(10, 140, 711, 261))
        self.buttons[1].setText('Niet')
        self.buttons[1].setFont(font)


        # Layout
        cluster_1 = QtGui.QHBoxLayout()
        cluster_1.addWidget(self.labels[0],1)

        cluster_3 = QtGui.QHBoxLayout()
        cluster_3.addWidget(self.buttons[0],2)
        cluster_3.addWidget(self.buttons[1],2)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(cluster_1,8)
        layout.addLayout(cluster_3,1)

        self.setLayout(layout)

        # Actions - buttons
        self.buttons[0].clicked.connect(self.commitL)
        self.buttons[1].clicked.connect(self.commitR)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_4:
            self.commitL()
        elif event.key() == QtCore.Qt.Key_6:
            self.commitR()
        elif event.key() == QtCore.Qt.Key_0:
            self.print_result()
        event.accept()

    def commit(self,nr):
        if nr == 0:
            #bannish
            self.delete_photo(self.counter)
        if self.DB_size(self.counter):
            self.counter = self.counter + 1
            self.set_new_word(0, self.counter)
        else:
            #printresult
            self.print_result()

    def reset_lga(self):
        self.stamvader = lga(None)
        self.stamvader.set_base_array(len(self.dbr))
        self.reset_lga_common()

    def delete_photo(self, counter):
        self.dbr[counter-1]=None

    def DB_size(self, counter):
        if counter < len(self.dbr):
            return True
        else:
            return False

    def print_result(self):
        self.container.unlinked_raw()
        self.set_image(0, os.path.join(os.path.dirname(sys.argv[0]),"img/done.png"))
        if self.dbr !=None:
            self.container.check_or_make("verban")
            counter = 0
            for x in self.dbr:
                if x != None and counter <= self.counter:
                    self.container.place_in_submap(x,"verban")
            self.dbr=None #this line makes sure your output only appears once
