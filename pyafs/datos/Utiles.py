from pyafs.utiles.Singleton import Singleton
import re

#=============================================================================================
@Singleton
class Textos (Singleton):

    #------------------------------------------------------------------------------------------
    def __init__(self):

        ''

    #------------------------------------------------------------------------------------------
    def ContieneDigitos(self, texto):
    
        return not re.match(".*[0-9]+.*", texto) is None

#=============================================================================================
@Singleton
class Listas (Singleton):

    #------------------------------------------------------------------------------------------
    def __init__(self):

        ''

    #------------------------------------------------------------------------------------------
    def ElegirValor(self, key, default, dic):
        
        return dic.get(key, default)

    #------------------------------------------------------------------------------------------
    def ElegirPrimeroNoVacio(self, default, lista):
        
        lista_no_vacios = [e for e in lista if len(e)]
        return lista_no_vacios[0] if len(lista_no_vacios) else default
