from Parser import Device
from Parser import Group


def searchDevices(line):
    return line.find('<devices>')
def searchEndDevices(line):
    return line.find('</devices>')

def searchDevice(line):
    return line.find('<device ')

def searchEndDevice(line):
    return line.find('</device>')

def searchGroup(line):
    return line.find('<group ')

def searchEndGroup(line):
    return line.find('</group>')      

def extractDeviceId(line):
    start=line.rfind('id="')+4
    end=line.rfind('" user_agent')
    return line[start:end]    

def extractDeviceUserA(line):
    start=line.rfind('user_agent="')+12
    end=line.rfind('" fall_back')
    print line[start:end]
    return line[start:end]

def extractDeviceFallB(line):
    start=line.rfind('fall_back="')+11
    end=line.rfind('">')
    return line[start:end]

def extractDeviceAtt(line,device):
    device.set_id(extractDeviceId(line))
    device.set_user_agent(extractDeviceUserA(line))
    device.set_fallback(extractDeviceFallB(line))
    
def extractGroupAtt(line,device):
    group=Group.Group()
    start=line.rfind('id="')+4
    end=line.rfind('">')
    group.set_id(line[start:end])
    group.set_device(device)
    device.set_groups(group)
    
#Obtiene el capability de cada tag <capability=#
def searchCapability(line):
    start=line.rfind('<capability ')+12
    end=line.rfind('/>')
    return line[start:end]
    
    
def extractNameCapability(line,capability):
    start=line.rfind('name="')+6
    end=line.rfind('" value="')
    capability.set_name(line[start:end])
    
def extractValueCapability(line,capability):
    start=line.rfind('value="')+7
    end=line.rfind('"')
    capability.set_value(line[start:end])

def addCapabilities(group,capability):
    group.add_capabilities(capability)
#final de linea que busca y agrega capabilities#
def readXml(devices):
    inTagGroup=False
    inDevicesContent=False
    inTagDevice=False
    inTagCapability=False
    xmlFile=open('prueba.xml','r')
    line=xmlFile.readline()
    while line!="":
        #print line
        line=xmlFile.readline()
        if not(inDevicesContent):
            if searchDevices(line)!=-1:
                inDevicesContent=True
        else:
            if not(inTagDevice):
                if searchDevice(line)!=-1:
                    #Instancia de dispositivo provisional hasta que se finalic el tag
                    device=Device.Device()
                    inTagDevice=True
                    extractDeviceAtt(line,device)
            else:
                if not(inTagGroup):
                    if searchGroup(line)!=-1:
                        inTagGroup=True
                        extractGroupAtt(line,device)
                else:
                    if searchEndGroup(line)!=-1:
                        inTagGroup=False
                if searchEndDevice(line)!=-1:
                    
                    devices.append(device)
                    inTagDevice=False
            if searchEndDevices(line)!=-1:
                inDevicesContent=False
            

# Declaracion del main
if __name__ == "__main__":
    devices=[]
    readXml(devices)
    print "hola"
    
    



        
        

    