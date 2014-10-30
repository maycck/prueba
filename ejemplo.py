import urllib2

def sumaDos():
    print 10 * 20
    
def division(a, b):
    result = a/b
    print result
    
def msj():
    print "El resultado es"

class Estudiante(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        return self.nombre
    
    def esMayor(self):
        if self.edad >= 18:
            return true
        else:
            return false
def cast():
    lista = [1,2,3,"hola",{"key1":"lista1", "key2":"lista2"}, (1,2,3)]
    tupla = (1,2,3)
    diccionario = {"key1":"Miki", "key2":"Pepe","key3":"Daniel"}
    lista.append("hello")
    for k,v in diccionario.items():
        print "%s %s" % (k,v)

    for i in lista:
        print i

def getweb():
    try:
        web = urllib2.urlopen("http://itjiquilpan.edu.mx/")
        print web.read()
        web.close()
    except urllib2.HTTPError, e:
        print e
    except urllib2.URLError as e:
        print e

def main():
    cast()

if __name__ == "__main__":
    main()