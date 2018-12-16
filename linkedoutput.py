import os

class linked_output(object):
    __shared_state={}
    def __init__(self, *args):
        self.__dict__=self.__shared_state
        self.bloc = []
        self.ext=[]
        print args[0]
        if not self.is_empty():
            self.bloc.append(args[0])
            if len(args) > 1:
                self.bloc.append(args[1])

    def is_empty(value):
        if value == "":
            return True
        else:
            return False

    def get_bloc(self,locid):
        return self.bloc[locid]

    def is_linked(self):
        if len(self.bloc) > 1:
            return True
        else:
            return False

    def check_or_make(self,dir):
        #import een submap van de basedirectories: check of die bestaat en anders aanmaken
        toMake = os.path.join(self.bloc[0],dir)
        if not os.path.exists(toMake):
            os.makedirs(toMake)
        if self.is_linked():
            toMake = os.path.join(self.bloc[1],dir)
            if not os.path.exists(toMake):
                os.makedirs(toMake)

    def place_in_submap(self,file, target):
        original = os.path.join(self.bloc[0],file)
        result = os.path.join(self.bloc[0],target,file)
        os.rename(original,result)
        if self.is_linked():
            original = os.path.join(self.bloc[1],self.ext_switch(file))
            result = os.path.join(self.bloc[1],target,self.ext_switch(file))
            os.rename(original,result)

    def prefix(self,name,prefix):
        original = os.path.join(self.bloc[0],name)
        result = os.path.join(self.bloc[0],str(prefix)+"_"+name)
        os.rename(original,result)
        if self.is_linked():
            original = os.path.join(self.bloc[1],self.ext_switch(name))
            result = os.path.join(self.bloc[1],str(prefix)+"_"+self.ext_switch(name))
            os.rename(original,result)

    def set_ext(self,master_ext):
        self.ext.append(os.path.splitext(master_ext)[1])
        if self.is_linked():
            mark = True
            for f in os.listdir(self.bloc[1]): 
                if os.path.isfile(os.path.join(self.bloc[1], f)) and mark:
                    mark = False
                    self.ext.append(os.path.splitext(f)[1])

    def get_ext(self,mos):
        return self.ext[mos]

    def ext_switch(self,file):
        basename = os.path.splitext(file)[0]
        ori_ext = os.path.splitext(file)[1]
        if ori_ext == self.get_ext(0):
            new_name = basename + self.get_ext(1)
        elif ori_ext == self.get_ext(1):
            new_name = basename + self.get_ext(0)
        return new_name

    def unlinked_raw(self):
        print "unlinked"
        if len(self.bloc) == 1 and os.path.exists(os.path.join(self.bloc[0],"tmp_tiff")):
            print "linked"
            self.bloc.append(os.path.join(self.bloc[0],"tmp_tiff"))
            self.ext.append(".tiff")

    def switch_SM(self):
        master = self.bloc[0]
        self.bloc[0] = self.bloc[1]
        self.bloc[1] = master

    def is_slave(self,file):
        if os.path.basename(file) == self.get_bloc(1):
            return True
        else:
            return False