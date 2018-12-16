#Bucket_tab
#sort_tab
#screening_tab
#ervern allemaal methodes en variables uit parent_tab

class parent_tab():
    def __init__(self):
        #Variables
        self.dbr = []
        self.counter = 1
        self.location = ""


    #Methods: 
    def set_dbr(self,dbr):
        self.dbr = dbr

    def set_new_word(self, box, img):
        if self.dbr[img-1] >= 0:
            txt = "%s%s" % (self.location,self.dbr[img-1])
            self.labels[box].setPixmap(txt)
            self.labels[box].update()

    def set_image(self, box, img):
        self.labels[box].setPixmap(img)
        self.labels[box].update()

    def change_location(self, locat):
        self.location = locat

    def reset_lga_common(self):
        self.stamvader.initialize(self.stamvader)
        self.stamvader.less.clear_array()
        self.stamvader.great.clear_array()
        self.stamvader.increment()
        self.active_lga= self.stamvader
        self.active_lga.lga_status()

    def set_counter(self, counter):
        self.counter = counter

    def commitL(self):
        self.commit(0)

    def commitR(self):
        self.commit(1)

    #Abstract methods
    def commit(self,nr):
        pass
    def print_result(self):
        pass
    def commit(self,nr):
        pass
    def keyPressEvent(self, event):
        pass