#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from pyafs.utiles.Singleton import Singleton
import unidecode


@Singleton
class Encoding (Singleton):

    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        self.TablaTran = {
            '\x80':'C',
            '\x82':'e',
            '\xa0':'a',
            '\xa1':'i', # char = ¡
            '\xa2':'o', # char = ¢
            '\xa3':'u', # char = £
            '\xa4':'?', # char = ¤
            '\xa5':'Ñ', # char = ¥
            '\xa6':'?', # char = ¦
            '\xa7':'?', # char = §
            '\xa8':'?', # char = ¨
            '\xa9':'?', # char = ©
            '\xaa':'?', # char = ª
            '\xab':'?', # char = «
            '\xac':'?', # char = ¬
            '\xad':'0', # char = 
            '\xae':'?', # char = ®
            '\xaf':'?', # char = ¯
            '\xb0':'?', # char = °
            '\xb1':'?', # char = ±
            '\xb2':'?', # char = ²
            '\xb3':'?', # char = ³
            '\xb4':'?', # char = ´
            '\xb5':'?', # char = µ
            '\xb6':'?', # char = ¶
            '\xb7':'?', # char = ·
            '\xb8':'?', # char = ¸
            '\xb9':'?', # char = ¹
            '\xba':'?', # char = º
            '\xbb':'?', # char = »
            '\xbc':'?', # char = ¼
            '\xbd':'?', # char = ½
            '\xbe':'?', # char = ¾
            '\xbf':'?', # char = ¿
            '\xc0':'A', # char = À
            '\xc1':'A', # char = Á
            '\xc2':'A', # char = Â
            '\xc3':'A', # char = Ã
            '\xc4':'A', # char = Ä
            '\xc5':'A', # char = Å
            '\xc6':'AE', # char = Æ
            '\xc7':'C', # char = Ç
            '\xc8':'E', # char = È
            '\xc9':'E', # char = É
            '\xca':'E', # char = Ê
            '\xcb':'E', # char = Ë
            '\xcc':'I', # char = Ì
            '\xcd':'I', # char = Í
            '\xce':'I', # char = Î
            '\xcf':'I', # char = Ï
            '\xd0':'D', # char = Ð
            '\xd1':'Ñ', # char = Ñ
            '\xd2':'O', # char = Ò
            '\xd3':'O', # char = Ó
            '\xd4':'O', # char = Ô
            '\xd5':'O', # char = Õ
            '\xd6':'O', # char = Ö
            '\xd7':'?', # char = ×
            '\xd8':'O', # char = Ø
            '\xd9':'U', # char = Ù
            '\xda':'U', # char = Ú
            '\xdb':'U', # char = Û
            '\xdc':'U', # char = Ü
            '\xdd':'Y', # char = Ý
            '\xde':'?', # char = Þ
            '\xdf':'ss', # char = ß
            '\xe0':'a', # char = à
            '\xe1':'a', # char = á
            '\xe2':'a', # char = â
            '\xe3':'a', # char = ã
            '\xe4':'a', # char = ä
            '\xe5':'a', # char = å
            '\xe6':'ae', # char = æ
            '\xe7':'c', # char = ç
            '\xe8':'e', # char = è
            '\xe9':'e', # char = é
            '\xea':'e', # char = ê
            '\xeb':'e', # char = ë
            '\xec':'i', # char = ì
            '\xed':'i', # char = í
            '\xee':'i', # char = î
            '\xef':'i', # char = ï
            '\xf0':'d', # char = ð
            '\xf1':'ñ', # char = ñ
            '\xf2':'o', # char = ò
            '\xf3':'o', # char = ó
            '\xf4':'o', # char = ô
            '\xf5':'o', # char = õ
            '\xf6':'o', # char = ö
            '\xf7':'?', # char = ÷
            '\xf8':'o', # char = ø
            '\xf9':'u', # char = ù
            '\xfa':'u', # char = ú
            '\xfb':'u', # char = û
            '\xfc':'u', # char = ü
            '\xfd':'y', # char = ý
            '\xfe':'?', # char = þ
            '\xff':'y', # char = ÿ
        }

    #------------------------------------------------------------------------------------------
    def Lower(self, texto, extendido=False):
    
        return texto.lower() if not extendido else texto.lower().replace('Ñ', 'ñ')

    #------------------------------------------------------------------------------------------
    def Upper(self, texto, extendido=False):
    
        return texto.upper() if not extendido else texto.upper().replace('ñ', 'Ñ')

    #------------------------------------------------------------------------------------------
    def Capitalizar(self, texto):
    
        def capitalizar_palabra(s):
            return '' if not s else '%s%s' % (self.Upper(s[0], True), self.Lower(s[1:], True))
    
        return ' '.join([ capitalizar_palabra(s) for s in texto.split(' ') ])

    #------------------------------------------------------------------------------------------
    def NormalizarTexto(self, texto):

        return unidecode.unidecode(texto)

    #------------------------------------------------------------------------------------------
    def NormalizarTextoViejo(self, texto):

        if texto is None:
            return texto
        
        texto = self.ToUnicode(texto)
        for (k, v) in self.TablaTran.items():
            texto = texto.replace(self.ToUnicode(k), self.ToUnicode(v))

        return self.ToString(texto)
    
    #------------------------------------------------------------------------------------------
    def NormalizarLista(self, datos):

        return [ Encoding.I().NormalizarTexto(t) for t in datos ]

    #------------------------------------------------------------------------------------------
    def ToUnicode(self, dato, code='latin1'):

        try:        
            #return dato if isinstance(dato, unicode) else str(dato).decode(code)
            return dato
        except:
            return '<ERROR_ENC_UNI>'
     
    #------------------------------------------------------------------------------------------
    def ToString(self, dato, code='latin1'):

        try:        
            #return dato.encode(code) if isinstance(dato, unicode) else str(dato)
            return dato
        except:
            return '<ERROR_ENC_STR>'

