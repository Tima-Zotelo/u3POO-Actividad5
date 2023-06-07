from zope.interface import Interface, implementer
from zope.interface.verify import verifyObject

class IColeccion(Interface):
    def insertarElemento(objeto, posicion):
        pass
    
    def agregarElemento(objeto):
        pass
    
    def mostrarElemento(posicion):
        pass

class Coleccion (IColeccion):
    __listaE: list
    def __init__(self) -> None:
        self.__listaE = []

    def insertarElemento(self, elemento, posicion):
        if posicion < 0 and posicion > len (self.__listaE):
            raise Exception ('Error, posicion incorrecta')
        self.__listaE.insert (posicion, elemento)

    def agregarElemento(self, elemento):
        self.__listaE.append(elemento)

    def mostrarElemento(self, posicion):
        if posicion < 0 and posicion > len (self.__listaE):
            raise Exception ('Error, posicion incorrecta')
        print (self.__listaE[posicion])