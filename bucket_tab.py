from PyQt4 import QtCore, QtGui
from Label import Label
import os, sys
from parent_tab import parent_tab

class bucket_tab(QtGui.QWidget,parent_tab):
    def __init__(self,parent):
        super(bucket_tab, self).__init__(parent= parent)

        # Variables
        self.change_location("")

        # Widgets
        self.labels = [
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label()
        ]

        self.memarrays = [
            list(),
            list(),
            list(),
            list(),
            list(),
            list()
        ]

        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)

        # Layout
        self.labels[0].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/nily.png"))
        self.labels[1].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/1.png"))
        self.labels[2].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/2.png"))
        self.labels[3].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/3.png"))
        self.labels[4].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/4.png"))
        self.labels[5].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/5.png"))
        self.labels[6].setPixmap(os.path.join(os.path.dirname(sys.argv[0]),"img/6.png"))

        cluster_1 = QtGui.QVBoxLayout()
        cluster_1.addWidget(self.labels[1],1)
        cluster_1.addWidget(self.labels[2],1)
        cluster_1.addWidget(self.labels[3],1)

        cluster_3 = QtGui.QVBoxLayout()
        cluster_3.addWidget(self.labels[4],1)
        cluster_3.addWidget(self.labels[5],1)
        cluster_3.addWidget(self.labels[6],1)

        cluster_2 = QtGui.QHBoxLayout()
        cluster_2.addWidget(self.labels[0],1)

        layout = QtGui.QHBoxLayout()
        layout.addLayout(cluster_1,2)
        layout.addLayout(cluster_2,6)
        layout.addLayout(cluster_3,2)

        self.setLayout(layout)

        # Actions - buttons
        # self.buttons[0].clicked.connect(self.commitL)
        # self.buttons[1].clicked.connect(self.commitR)

    #Laat programma ook werken met "4" en "6" toetsen.
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_7:
            self.commit(1)
        elif event.key() == QtCore.Qt.Key_8:
            self.commit(2)
        elif event.key() == QtCore.Qt.Key_9:
            self.commit(3)
        elif event.key() == QtCore.Qt.Key_4:
            self.commit(4)
        elif event.key() == QtCore.Qt.Key_5:
            self.commit(5)
        elif event.key() == QtCore.Qt.Key_6:
            self.commit(6)
        elif event.key() == QtCore.Qt.Key_0:
            self.print_result()
        event.accept()

    def commit(self,nr):
        if self.DB_size(self.counter):
            self.set_new_word(nr,self.counter)
            self.memarrays[nr-1].append(self.counter)
            self.counter = self.counter + 1
            self.set_new_word(0,self.counter)
            print self.counter
        else:
            #printresult
            self.print_result()

    def DB_size(self, counter):
        if counter <= len(self.dbr):
            return True
        else:
            return False

    def print_result(self):
        self.set_image(0, os.path.join(os.path.dirname(sys.argv[0]),"img/done.png"))
        if self.memarrays != None:
            counter_place = 0
            string1 = "%s" % (self.location)
            # self.parent().widget(0).output.append("mkdir %sbucket_1/"%(string1.replace(" ","\ "))) #print code in output window
            # self.parent().widget(0).output.append("mkdir %sbucket_2/"%(string1.replace(" ","\ "))) #print code in output window
            # self.parent().widget(0).output.append("mkdir %sbucket_3/"%(string1.replace(" ","\ "))) #print code in output window
            # self.parent().widget(0).output.append("mkdir %sbucket_4/"%(string1.replace(" ","\ "))) #print code in output window
            # self.parent().widget(0).output.append("mkdir %sbucket_5/"%(string1.replace(" ","\ "))) #print code in output window
            # self.parent().widget(0).output.append("mkdir %sbucket_6/"%(string1.replace(" ","\ "))) #print code in output window
            if not os.path.exists("%sbucket_1/"%(string1.replace(" ","\ "))):
                os.makedirs("%sbucket_1/"%(string1.replace(" ","\ "))) #execute code
            if not os.path.exists("%sbucket_2/"%(string1.replace(" ","\ "))): #execute code
                os.makedirs("%sbucket_2/"%(string1.replace(" ","\ "))) #execute code
            if not os.path.exists("%sbucket_3/"%(string1.replace(" ","\ "))):
                os.makedirs("%sbucket_3/"%(string1.replace(" ","\ "))) #execute code
            if not os.path.exists("%sbucket_4/"%(string1.replace(" ","\ "))): #execute code
                os.makedirs("%sbucket_4/"%(string1.replace(" ","\ "))) #execute code
            if not os.path.exists("%sbucket_5/"%(string1.replace(" ","\ "))):
                os.makedirs("%sbucket_5/"%(string1.replace(" ","\ "))) #execute code
            if not os.path.exists("%sbucket_6/"%(string1.replace(" ","\ "))): #execute code
                os.makedirs("%sbucket_6/"%(string1.replace(" ","\ "))) #execute code

            for subplots in self.memarrays:
                counter_place = counter_place + 1
                for item in subplots:
                    anwsr = self.dbr[item-1]
                    # self.parent().widget(0).output.append("mv %s%s %sbucket_%s/%s"%(string1.replace(" ","\ "),anwsr,string1.replace(" ","\ "),counter_place,anwsr))
                    os.rename("%s%s"%(string1.replace(" ","\ "),anwsr),"%sbucket_%s/%s"%(string1.replace(" ","\ "),counter_place,anwsr)) #execute code

            self.memarrays=None #this line makes sure your output only appears once
