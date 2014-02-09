import Device

def leerXml():
    archivo=open('read.txt','r')
    linea=archivo.readline()
    while linea!="":
        print linea
        linea=archivo.readline()
    

# Declaracion del main
if __name__ == "__main__":    
    leerXml()