'''
Created on 21/11/2013

@author: Administrador
'''
import urllib2

#================================================================================================
class WebDoc:

    #-------------------------------------------------------------------------------------
    def __init__(self):

        self._url = ''
        
    #-------------------------------------------------------------------------------------
    def Cargar(self, url):

        self._url = url
        
        resp = urllib2.urlopen(url)
        html = resp.read()
        
        return html
        