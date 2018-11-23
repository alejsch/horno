from pyafs.utiles.Singleton import Singleton
import psutil

#==========================================================================================
@Singleton
class Memoria (Singleton):
    
    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        ''

    #------------------------------------------------------------------------------------------
    def GetInfoMem(self):
        return psutil.virtual_memory().total / 1024 ** 2
        
