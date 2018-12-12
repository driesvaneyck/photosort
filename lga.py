from PyQt4 import QtCore, QtGui
import random

class lga():
    def __init__(self, parent):
        self.array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
        self.less = None            # Dochterarray van items die slechter zijn dan de pivot
        self.great = None           # Dochterarray van items die beter zijn dan de pivot
        self.index = 0              
        self.pivot = None
        self.parent = parent        # Van welke array is dit een subarray
        self.done = False
        self.prune = False
        self.quickersort = 20
        self.quickersortp = 20

    def initialize(self, parent):
        if len(self.array) > 1:
            self.less = lga(parent)
            self.great =lga(parent)
            self.pivot = self.array[0]
        else:
            self.done = True
    def append(self,number):
        self.array.append(number)
    def lappend(self,index):
        self.less.append(self.array[index])
    def gappend(self,index):
        self.great.append(self.array[index])
    def increment(self):
        self.index = self.index + 1
    def done():
        return self.done
    def combine():
        if self.less.done() == True and self.great.done() == True:
            pivo = [self.pivot]
            return self.less.array + pivo + self.great.array
    def get_pivot(self):
        return self.pivot
    def get_array_index(self,index):
        return self.array[index]
    def get_index(self):
        return self.index
    def get_array(self):
        return self.array
    def clear_array(self):
        self.array = []
    def clear_pivot(self):
        self.pivot = None
    def toggle_prune(self):
        if self.prune == True:
            self.prune = False
        else:
            self.prune = True
    def get_prune(self):
        return self.prune;
    #kijk of er naar beneden toe nog meer gesorteerd moet worden
    def get_bless(self):
        #Kijk of kleiner_dan_dochterarray leeg is of 1 element bevat
        if len(self.less.get_array()) <= 1: 
            return True
        #Kijk of kleiner_dan_dochterarray niet leeg is en nog verder gesorteerd kan worden.
        elif self.less.get_array() > 1 and self.less.great == None and self.less.less == None:
            return False
        elif self.less.get_bmore() and self.less.get_bless():
            return True
        else:
            return False
    def get_bmore(self):
        if len(self.great.get_array()) <= 1: 
            return True
        elif self.great.get_array() > 1 and self.great.great == None and self.great.less == None:
            return False
        elif self.great.get_bmore() and self.great.get_bless():
            return True
        else:
            return False
    def lga_status(self):
        print "self.array       = %s" % (self.array)
        print "self.less        = %s"% (self.less.get_array())
        print "self.great       = %s"% (self.great.get_array())
        print "self.pivot       = %s"% (self.get_pivot())
        if self.parent == None:
            print "self.parent      = None"
        else:
            print "self.parent      = %s"%(self.parent)
        print 'self.get_bless() = %s'  %(self.get_bless())
        print 'self.get_bmore() = %s' %(self.get_bmore())
    def set_base_array(self, nr):
        self.array = []
        counter = 1
        while counter <= nr:
            self.array.append(counter)
            counter = counter + 1
