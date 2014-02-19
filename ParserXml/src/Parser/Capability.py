'''
Created on 09/02/2014

@author: Jimmy
'''



class Capability:
    

    def __init__(self):
        self.___name = str
        self.___value = str
        #@GrupoPerteneciente
        #self._group = Group()

    def get_name(self):
        return self.__name


    def get_value(self):
        return self.__value


    def get_group(self):
        return self.__group


    def set_name(self, value):
        self.__name = value


    def set_value(self, value):
        self.__value = value


    def set_group(self, value):
        self.__group = value


        