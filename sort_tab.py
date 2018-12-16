from PyQt4 import QtCore, QtGui
from Label import Label
from lga import lga
from parent_tab import parent_tab
import os,sys
from linkedoutput import linked_output



class Sort_Tab(QtGui.QWidget,parent_tab):
    def __init__(self,parent):
        super(Sort_Tab, self).__init__(parent= parent)

        # Variables
        self.stamvader = lga(None)
        self.container = linked_output("")
        # self.counter = 0 # =prune limit in this class, currently deactivated function

        # Widgets
        self.buttons = [
            QtGui.QPushButton(),
            QtGui.QPushButton()
        ]
        self.labels = [
            Label(),
            Label()
        ]

        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)

        self.labels[0].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/nily.png"))
        self.labels[1].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/nily.png"))

        self.buttons[0].setMinimumSize(1, 1)
        self.buttons[0].setText('Links')
        self.buttons[0].setFont(font)

        self.buttons[1].setMinimumSize(1, 1)
        self.buttons[1].setGeometry(QtCore.QRect(10, 140, 711, 261))
        self.buttons[1].setText('Rechts')
        self.buttons[1].setFont(font)

        # Layout
        cluster_1 = QtGui.QHBoxLayout()
        cluster_1.addWidget(self.labels[0],1)
        cluster_1.addWidget(self.labels[1],1)

        cluster_2 = QtGui.QHBoxLayout()
        cluster_2.addWidget(self.buttons[0],1)
        cluster_2.addWidget(self.buttons[1],1)
        
        layout = QtGui.QVBoxLayout()
        layout.addLayout(cluster_1,8)
        layout.addLayout(cluster_2,2)

        self.setLayout(layout)

        # Actions - buttons
        self.buttons[0].clicked.connect(self.commitL)
        self.buttons[1].clicked.connect(self.commitR)

    #Laat programma ook werken met "4" en "6" toetsen.
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_4:
            self.commitL()
        elif event.key() == QtCore.Qt.Key_6:
            self.commitR()
        elif event.key() == QtCore.Qt.Key_0:
            self.stitch()
        event.accept()

    def commit(self,nr):
        #Verdeel huidige foto uit (sub)array (LGA) in beter dan (nr = 0) en slechter dan (nr = 1) de pivot foto's, en ga daarna naar de volgende foto
        if self.active_lga.get_index() < len(self.active_lga.get_array()):
            if nr == 1:
                self.active_lga.lappend(self.active_lga.get_index())
            elif nr == 0:
                self.active_lga.gappend(self.active_lga.get_index())
        self.active_lga.increment()

        #Als de huidige subarray compleet verdeeld is:
        if self.active_lga.get_index() >= len(self.active_lga.get_array()):            
            self.pruning(self.active_lga)
            
            #Kijk of het sorteren gedaan is, en stitch de subarrays terug aan elkaar naar boven toe.
            while self.active_lga.get_bless() and self.active_lga.get_bmore() and self.active_lga.done != True:
                if self.active_lga.get_pivot() == None:
                    self.active_lga.array = self.active_lga.great.get_array()
                else:
                    temp_pivot = [self.active_lga.get_pivot()]
                    self.active_lga.array = self.active_lga.less.get_array() + temp_pivot + self.active_lga.great.get_array()  
                if self.active_lga.parent == None:
                    self.print_result()
                    self.active_lga.done = True
                self.active_lga = self.active_lga.parent
 
            #Ga naar groter kind, en sorteer verder
            if self.active_lga.get_bmore() == False:                    
                self.active_lga = self.active_lga.great
                self.active_lga.initialize(self.active_lga)
                self.active_lga.less.clear_array()
                self.active_lga.great.clear_array()
                self.set_new_word(1,self.active_lga.get_pivot())

            #Ga naar kleiner kind, en sorteer verder
            elif self.active_lga.get_bless() == False:        
                self.active_lga.less.initialize(self.active_lga.less)
                self.active_lga = self.active_lga.less
                self.active_lga.less.clear_array()
                self.active_lga.great.clear_array()
                self.set_new_word(1,self.active_lga.get_pivot())
            self.active_lga.increment()
        self.set_new_word(0,self.active_lga.get_array_index(self.active_lga.get_index()))

    def reset_lga(self):
        self.stamvader = lga(None)
        if len(self.dbr) > 0:
            self.stamvader.set_base_array(len(self.dbr))
        else:
            self.stamvader.set_base_array(3)
        self.reset_lga_common()

    def print_result(self):
        self.container.unlinked_raw()
        teller = len(self.stamvader.get_array())-1
        while teller >= 0:
            anwsr = self.dbr[self.stamvader.get_array()[teller]-1]
            self.container.prefix(anwsr, len(self.stamvader.get_array()) - teller)
            teller = teller-1
        self.set_image(0, os.path.join(os.path.dirname(sys.argv[0]),"img/done.png"))
        self.set_image(1, os.path.join(os.path.dirname(sys.argv[0]),"img/done.png"))



    def pruning(self, lga):
        if len(lga.less.get_array()) < self.counter and lga.get_prune() == False:
            #verwijder pivot en array
            self.counter = self.counter - len(lga.less.get_array())-1
            lga.less.clear_array()
            lga.clear_pivot()
        elif len(lga.less.get_array()) == self.counter and lga.get_prune() == False:
            #verwijder array
            self.counter = self.counter - len(lga.less.get_array())
            lga.less.clear_array()
        else:
            #stop pruning in deze branche tot ge weer op dezelfde hoogte zit
            lga.great.toggle_prune()
            if lga.get_prune() == True:
                lga.less.toggle_prune()

    def stitch(self):
        while True:
            if self.active_lga.get_index() >= len(self.active_lga.get_array()):#als ge deze subarray nog niks gesorteerd is
                temp_pivot = [self.active_lga.get_pivot()]
                self.active_lga.array = self.active_lga.less.get_array() + temp_pivot + self.active_lga.great.get_array() 
            else: #als ge deze subarray, niet juist helemaal gesorteerd hebt.
                temp_pivot = [self.active_lga.get_pivot()]
                non_sorted_part = self.active_lga.array[self.active_lga.get_index():len(self.active_lga.array)]
                self.active_lga.array = self.active_lga.less.get_array() + non_sorted_part + temp_pivot + self.active_lga.great.get_array() 
            if self.active_lga.parent == None:
                self.print_result()
                self.active_lga.done = True
                break
            self.active_lga = self.active_lga.parent
