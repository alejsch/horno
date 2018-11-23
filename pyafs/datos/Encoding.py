#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from pyafs.utiles.Singleton import Singleton


@Singleton
class Encoding (Singleton):

    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        self.TablaTran = {
            '\x80':'C',
            '\x82':'e',
            '\xa0':'a',
            '\xa1':'i', # char = �
            '\xa2':'o', # char = �
            '\xa3':'u', # char = �
            '\xa4':'?', # char = �
            '\xa5':'�', # char = �
            '\xa6':'?', # char = �
            '\xa7':'?', # char = �
            '\xa8':'?', # char = �
            '\xa9':'?', # char = �
            '\xaa':'?', # char = �
            '\xab':'?', # char = �
            '\xac':'?', # char = �
            '\xad':'0', # char = 
            '\xae':'?', # char = �
            '\xaf':'?', # char = �
            '\xb0':'?', # char = �
            '\xb1':'?', # char = �
            '\xb2':'?', # char = �
            '\xb3':'?', # char = �
            '\xb4':'?', # char = �
            '\xb5':'?', # char = �
            '\xb6':'?', # char = �
            '\xb7':'?', # char = �
            '\xb8':'?', # char = �
            '\xb9':'?', # char = �
            '\xba':'?', # char = �
            '\xbb':'?', # char = �
            '\xbc':'?', # char = �
            '\xbd':'?', # char = �
            '\xbe':'?', # char = �
            '\xbf':'?', # char = �
            '\xc0':'A', # char = �
            '\xc1':'A', # char = �
            '\xc2':'A', # char = �
            '\xc3':'A', # char = �
            '\xc4':'A', # char = �
            '\xc5':'A', # char = �
            '\xc6':'AE', # char = �
            '\xc7':'C', # char = �
            '\xc8':'E', # char = �
            '\xc9':'E', # char = �
            '\xca':'E', # char = �
            '\xcb':'E', # char = �
            '\xcc':'I', # char = �
            '\xcd':'I', # char = �
            '\xce':'I', # char = �
            '\xcf':'I', # char = �
            '\xd0':'D', # char = �
            '\xd1':'�', # char = �
            '\xd2':'O', # char = �
            '\xd3':'O', # char = �
            '\xd4':'O', # char = �
            '\xd5':'O', # char = �
            '\xd6':'O', # char = �
            '\xd7':'?', # char = �
            '\xd8':'O', # char = �
            '\xd9':'U', # char = �
            '\xda':'U', # char = �
            '\xdb':'U', # char = �
            '\xdc':'U', # char = �
            '\xdd':'Y', # char = �
            '\xde':'?', # char = �
            '\xdf':'ss', # char = �
            '\xe0':'a', # char = �
            '\xe1':'a', # char = �
            '\xe2':'a', # char = �
            '\xe3':'a', # char = �
            '\xe4':'a', # char = �
            '\xe5':'a', # char = �
            '\xe6':'ae', # char = �
            '\xe7':'c', # char = �
            '\xe8':'e', # char = �
            '\xe9':'e', # char = �
            '\xea':'e', # char = �
            '\xeb':'e', # char = �
            '\xec':'i', # char = �
            '\xed':'i', # char = �
            '\xee':'i', # char = �
            '\xef':'i', # char = �
            '\xf0':'d', # char = �
            '\xf1':'�', # char = �
            '\xf2':'o', # char = �
            '\xf3':'o', # char = �
            '\xf4':'o', # char = �
            '\xf5':'o', # char = �
            '\xf6':'o', # char = �
            '\xf7':'?', # char = �
            '\xf8':'o', # char = �
            '\xf9':'u', # char = �
            '\xfa':'u', # char = �
            '\xfb':'u', # char = �
            '\xfc':'u', # char = �
            '\xfd':'y', # char = �
            '\xfe':'?', # char = �
            '\xff':'y', # char = �
        }

    #------------------------------------------------------------------------------------------
    def Lower(self, texto, extendido=False):
    
        return texto.lower() if not extendido else texto.lower().replace('�', '�')

    #------------------------------------------------------------------------------------------
    def Upper(self, texto, extendido=False):
    
        return texto.upper() if not extendido else texto.upper().replace('�', '�')

    #------------------------------------------------------------------------------------------
    def Capitalizar(self, texto):
    
        def capitalizar_palabra(s):
            return '' if not s else '%s%s' % (self.Upper(s[0], True), self.Lower(s[1:], True))
    
        return ' '.join([ capitalizar_palabra(s) for s in texto.split(' ') ])

    #------------------------------------------------------------------------------------------
    def NormalizarTexto(self, texto):

        if texto is None:
            return texto
        
        texto = self.ToUnicode(texto)
        for (k, v) in self.TablaTran.iteritems():
            texto = texto.replace(self.ToUnicode(k), self.ToUnicode(v))

        return self.ToString(texto)
    
    #------------------------------------------------------------------------------------------
    def NormalizarLista(self, datos):

        return [ Encoding.I().NormalizarTexto(t) for t in datos ]

    #------------------------------------------------------------------------------------------
    def ToUnicode(self, dato, code='latin1'):

        try:        
            return dato if isinstance(dato, unicode) else str(dato).decode(code)
        except:
            return '<ERROR_ENC_UNI>'
     
    #------------------------------------------------------------------------------------------
    def ToString(self, dato, code='latin1'):

        try:        
            return dato.encode(code) if isinstance(dato, unicode) else str(dato)
        except:
            return '<ERROR_ENC_STR>'

