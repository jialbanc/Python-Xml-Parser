'''
Created on 09/02/2014

@author: Jimmy
'''


from Parser import Device


class Group(object):

    def __init__(self):
        self.___id = ""
        #@DispositivoPerteneciente
        self._device = Device.Device()
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
        
    def add_capabilities(self,capability):
        self._capabilitys.append(capability)
