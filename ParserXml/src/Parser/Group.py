'''
Created on 09/02/2014

@author: Jimmy
'''

import Device
import Capability

class Group(object):

    def __init__(self):
        self.___id = str
        #@DispositivoPerteneciente
        self._device = Device()
        #@listaDeCapabilitys
        self._capabilitys = []

    def get_id(self):
        return self.__id


    def get_device(self):
        return self.__device


    def get_capabilitys(self):
        return self.__capabilitys


    def set_id(self, value):
        self.__id = value


    def set_device(self, value):
        self.__device = value


    def set_capabilitys(self, value):
        self.__capabilitys = value
