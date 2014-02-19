'''
Created on 09/02/2014

@author: Jimmy
'''



class Device:
    
    def __init__(self):
        self.___id = ""
        self.___user_agent = ""
        self.___fallback = ""
        self.___actual_device_root=""
        #@DispositivoAsociado
        #self._deviceA = Device()
        #@listaDeGrupos
        self.__groups = []

    def get_id(self):
        return self.__id


    def get_user_agent(self):
        return self.__user_agent


    def get_fallback(self):
        return self.__fallback


    #def get_device_a(self):
    #    return self.__deviceA


    def get_groups(self):
        return self.__groups


    def set_id(self, value):
        self.__id = value


    def set_user_agent(self, value):
        self.__user_agent = value


    def set_fallback(self, value):
        self.__fallback = value


    #def set_device_a(self, value):
    #   self.__deviceA = value


    def set_groups(self, value):
        self.__groups.append(value)
        
    def set_actual_device_root(self,value):
        self.___actual_device_root=value
    
    def get_actual_device_root(self):
        return self.___actual_device_root
    
    
        