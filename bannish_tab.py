from PyQt4 import QtCore, QtGui
from Label import Label
import os,sys
import subprocess
from linkedoutput import linked_output


class Bannish_Tab(QtGui.QWidget):
    def __init__(self,parent):
        super(Bannish_Tab, self).__init__(parent= parent)

        # Variables
        self.file_list = []
        self.list_order = []
        self.act_compare = 1
        self.container = linked_output("")

        # Widgets
        self.labels = [
            Label(),
            Label()
        ]
        self.labels[0].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/nily.png"))
        self.labels[1].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/nily.png"))

        self.buttons = [
            QtGui.QPushButton()
        ]
        self.output = QtGui.QTextEdit()
        
        # Opmaak
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)

        self.buttons[0].setMinimumSize(1, 1)
        self.buttons[0].setText('Sorteer')
        self.buttons[0].setFont(font)

        # Layout
        cluster_1=QtGui.QVBoxLayout()
        cluster_1.addWidget(self.output,3)
        cluster_1.addWidget(self.buttons[0],2)

        cluster_2=QtGui.QHBoxLayout()
        cluster_2.addWidget(self.labels[0],5)
        cluster_2.addWidget(self.labels[1],5)

        layout = QtGui.QHBoxLayout()
        layout.addLayout(cluster_1,1)
        layout.addLayout(cluster_2,6)

        self.setLayout(layout)
       
        # Actions
        self.buttons[0].clicked.connect(self.read_out_list)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_4:
            self.commitB()
        elif event.key() == QtCore.Qt.Key_6:
            self.commitO()
        event.accept()

    def read_out_list(self):
        self.restart()
        self.file_list = str (self.output.toPlainText().replace("file://","")).replace("%20"," ").split("\n")
        i=0
        for item in self.file_list:
            self.list_order.append(i)
            i+=1
        self.labels[0].setPixmap(self.file_list[1])
        self.labels[1].setPixmap(self.file_list[0])
        self.labels[0].update()
        self.labels[1].update()
    
    def commitB(self):
        self.commit(0)

    def commitO(self):
        self.commit(1)

    def commit(self,nr):
        if self.act_compare < len(self.file_list):
            if nr == 1:
                #Boven
                temp = self.list_order[self.act_compare]
                self.list_order[self.act_compare] = self.list_order[self.act_compare-1]
                self.list_order[self.act_compare-1] = temp
            self.act_compare+=1

            if self.act_compare >= len(self.file_list)-1:
                self.set_image(0, os.path.join(os.path.dirname(sys.argv[0]),"img/done.png"))
                self.set_image(1, os.path.join(os.path.dirname(sys.argv[0]),"img/done.png"))
                self.verban()
            else:
               self.labels[0].setPixmap(self.file_list[self.list_order[self.act_compare]])
               self.labels[1].setPixmap(self.file_list[self.list_order[self.act_compare-1]])
               self.labels[0].update()
               self.labels[1].update()

    def verban(self):
        self.container.unlinked_raw()
        self.output.setText("")
        # self.check_bannish()
        self.container.check_or_make("verban")
        switch = False
        if self.container.is_slave(self.file_list[0]):
            self.container.switch_SM()
            switch = True
        i=0
        while i< len(self.list_order)-2:
            file = os.path.basename(self.file_list[self.list_order[i]])
            self.container.place_in_submap(file,"verban")
            i+=1
        if switch:
            self.container.switch_SM()
        self.restart


    def restart(self):
        self.file_list = []
        self.list_order = []
        self.act_compare = 1


    def set_image(self, box, img):
        self.labels[box].setPixmap(img)
        self.labels[box].update()

