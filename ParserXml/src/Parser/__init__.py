from Parser import Device

def searchDevices(line):
    return line.find('<devices>')

def searchDevice(line):
    return line.find('<device ')    

def extractDeviceId(line):
    start=line.rfind('id="')+4
    end=line.rfind('" user_agent')
    return line[start:end]    

def extractDeviceUserA(line):
    start=line.rfind('user_agent="')+12
    end=line.rfind('" fall_back')
    return line[start:end]

def extractDeviceFallB(line):
    start=line.rfind('fall_back="')+11
    end=line.rfind('">')
    return line[start:end]

def extractDeviceAtt(line,device):
    device.set_id(extractDeviceId(line))
    device.set_user_agent(extractDeviceUserA(line))
    device.set_fallback(extractDeviceFallB(line))
    
def readXml(device):
    inDevicesContent=False
    inTagDevice=False
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
                    inTagDevice=True
                    extractDeviceAtt(line,device)
            
                
                
                

# Declaracion del main
if __name__ == "__main__":
    devices=[]
    device=Device.Device()
    readXml(device)



        
        

    