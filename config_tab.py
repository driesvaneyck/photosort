from PyQt4 import QtCore, QtGui
import os

class Config_Tab(QtGui.QWidget):
    def __init__(self,parent):
        super(Config_Tab, self).__init__(parent=parent)
        self.buttons = [QtGui.QPushButton(),QtGui.QPushButton()]
        self.location = None

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)

        self.buttons[0].setMinimumSize(1, 1)
        self.buttons[0].setGeometry(QtCore.QRect(10, 140, 711, 261))
        self.buttons[0].setText('SelectFile')
        self.buttons[0].setFont(font)

        self.buttons[1].setMinimumSize(1, 1)
        self.buttons[1].setGeometry(QtCore.QRect(10, 140, 711, 261))
        self.buttons[1].setText('Rechts')
        self.buttons[1].setFont(font)

        self.output = QtGui.QTextEdit()
        self.line = QtGui.QLineEdit()

        # cluster_1 = QtGui.QHBoxLayout()
        # cluster_1.addWidget(self.buttons[1])
        # cluster_1.addWidget(self.line)

        cluster_2 = QtGui.QHBoxLayout()
        cluster_2.addWidget(self.buttons[0],1)
        # cluster_2.addLayout(cluster_1,1)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.output,8)
        layout.addLayout(cluster_2,2)

        self.setLayout(layout)

        # Actions - buttons
        self.buttons[0].clicked.connect(self.commitL)
        self.buttons[1].clicked.connect(self.commitR)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_0:
            self.copy_rank(self.location)
        if event.key() == QtCore.Qt.Key_1:
            self.name_security(self.location,True)
        if event.key() == QtCore.Qt.Key_2:
            self.name_security(self.location,False)
        event.accept()

    def commitL(self):
        selectFolder = QtGui.QFileDialog()
        selectFolder.setFileMode(QtGui.QFileDialog.Directory)
        selectFolder.setOption(QtGui.QFileDialog.ShowDirsOnly, True)
        filename = selectFolder.getOpenFileName(None, 'Select Folder')
        filename2 = os.path.dirname(str(filename))+"/"
        dbr = self.insert_photo_list_dbr(filename2)
        self.location = filename2

        # De regels code hieronder verwijzen naar functies en variables uit de andere *_tab.py files, verwijzing gebeurt via de tabs widget (parent)
        sort = 1
        config = 0
        bannish = 2
        screening = 3
        bucket = 4

        self.parent().widget(screening).set_counter(1)
        self.parent().widget(bucket).set_counter(1)
        self.parent().widget(sort).set_counter(0)
        self.parent().widget(sort).set_dbr(dbr)
        self.parent().widget(sort).reset_lga()
        self.parent().widget(sort).change_location(filename2)
        self.parent().widget(screening).change_location(filename2)
        self.parent().widget(bucket).change_location(filename2)
        self.parent().widget(screening).set_dbr(dbr)
        self.parent().widget(screening).set_counter(1)
        self.parent().widget(screening).set_new_word(0,1)
        self.parent().widget(sort).set_new_word(1,self.parent().widget(sort).stamvader.get_pivot())
        self.parent().widget(sort).set_new_word(0,self.parent().widget(sort).stamvader.get_array_index(self.parent().widget(sort).stamvader.get_index()))
        self.parent().widget(config).line.setText(str(len(self.parent().widget(sort).stamvader.get_array())))
        self.parent().widget(bucket).set_dbr(dbr)
        self.parent().widget(bucket).set_new_word(0,1)


    def commitR(self):
        self.parent().widget(1).prune_limit = len(self.parent().widget(1).stamvader.get_array())-int(self.line.text())

    def insert_photo_list_dbr(self,dirz):
        abc = []
        onlyfiles = [f for f in os.listdir(dirz) if os.path.isfile(os.path.join(dirz, f))]
        for file in onlyfiles:
            abc.append(os.path.basename(file))
        self.output.append("Loaded %s pictures"%(len(abc)))
        return abc

    def copy_rank(self,location):
        #if this location has a subfolder named RAW or RAF mimic the naming scheme of this folder onto that one
        baselocation = None
        ext = None
        if os.path.exists(os.path.join(location,"RAF")):
            baselocation = os.path.join(location,"RAF")
            ext = "RAF"
        elif os.path.exists(os.path.join(location,"RAW")):
            baselocation = os.path.join(location,"RAW")
            ext = "RAW"
        if baselocation != None:
            dbr = self.insert_photo_list_dbr(location)
            for x in dbr:
                stripname = os.path.splitext(x)[0]
                print stripname
                stripname = stripname+"."+ext
                print stripname
                counter = 0
                if "_" in stripname:
                    while stripname[counter] != "_":
                        counter = counter + 1
                    strippername = stripname[counter+1:]
                    strippername = os.path.join(baselocation,strippername)
                else:
                    strippername = os.path.join(baselocation,stripname)
                if os.path.exists(strippername):
                    stripname = os.path.join(baselocation, stripname)
                    os.rename(strippername,stripname)

    def name_security(self, location, switch ):
        if switch:
            onlyfiles = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]
            for file in onlyfiles:
                os.rename(os.path.join(location,file),os.path.join(location,file.replace("_","---")))
        else:
            onlyfiles = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]
            for file in onlyfiles:
                os.rename(os.path.join(location,file),os.path.join(location,file.replace("---","_")))






