from pyafs.utiles.IO import IOEscritor, IOArchivo, IOSistema
from pyafs.utiles.Singleton import Singleton

#================================================================================================
@Singleton
class Logger (Singleton):
    
    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        self.archivo_log = IOArchivo('nul')            

    #------------------------------------------------------------------------------------------
    def Resetear(self):
        with IOEscritor(self.archivo_log).Abrir(False) as iow:
            iow.EscribirLinea('LOG FILE RESETEADO!')

    #------------------------------------------------------------------------------------------
    def Redireccionar(self, archivo_log_):
        self.archivo_log = archivo_log_
        self.Resetear()

    #------------------------------------------------------------------------------------------
    def Log(self, texto, printear=True):
        if printear:
            IOSistema.I().PrintLine(texto)
            
        with IOEscritor(self.archivo_log).Abrir(True) as iow:
            iow.EscribirLinea(texto)            

    #------------------------------------------------------------------------------------------
    def LogSep(self, texto, printear=True):
        self.Log('=' * IOSistema.I().CharSep(), printear)
        self.Log('%s' % texto, printear)
        self.Log('=' * IOSistema.I().CharSep(), printear)
    
