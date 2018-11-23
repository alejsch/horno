import datetime

class Fecha:

    #------------------------------------------------------------------------------------------
    def __init__(self, fecha):

        if type(fecha) is not datetime.datetime:
            self._fecha = datetime.datetime.max
        else:
            self._fecha = fecha

    #------------------------------------------------------------------------------------------
    def __cmp__(self, fecha):
        
        if self.Date() < fecha.Date():
            return -1
        elif self.Date() > fecha.Date():
            return 1
        else:
            return 0

    #------------------------------------------------------------------------------------------
    def Date(self):
        
        return self._fecha

    #------------------------------------------------------------------------------------------
    def Anio(self):
        
        return self._fecha.year if not self._fecha is None else ''

    #------------------------------------------------------------------------------------------
    def AnioCorto(self):
        
        return int(str(self.Anio())[:-2])
    
    #------------------------------------------------------------------------------------------
    def Mes(self):
        
        return self._fecha.month if not self._fecha is None else ''

    #------------------------------------------------------------------------------------------
    def Dia(self):
        
        return self._fecha.day if not self._fecha is None else ''

    #------------------------------------------------------------------------------------------
    @staticmethod
    def Ahora():
        
        return Fecha( datetime.datetime.now() )

    #------------------------------------------------------------------------------------------
    @staticmethod
    def DesdeValores(ano, mes, dia):
        
        return Fecha.DesdeString( '%s-%s-%s' % (ano, mes, dia), '%Y-%m-%d' )
    
    #------------------------------------------------------------------------------------------
    @staticmethod
    def DesdeString(fecha_str, formato, date_default=None):
        
        try:
        
            fecha_str_norm = fecha_str.strip().upper().replace('/','-').split(' ')[0]
            formato = formato.replace('/','-').split(' ')[0]
            
            if not fecha_str_norm:
                return Fecha( date_default )

            if formato in [ '%d-%b-%Y', '%d-%m-%Y' ]:
                [dia,mes,ano] = fecha_str_norm.split('-') 
            elif formato in [ '%Y-%m-%d' ]: 
                [ano,mes,dia] = fecha_str_norm.split('-')
            elif formato in [ '%Y%m%d' ]:
                ano = fecha_str_norm[0:4]; mes = fecha_str_norm[4:6]; dia = fecha_str_norm[6:8]
            else:
                raise Exception('Fecha: Formato no reconocido')
            
            if formato in ['%d-%b-%Y']:
                mes_numero = {'ENE':1,'JAN':1,'FEB':2,'MAR':3,'ABR':4,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AGO':8,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DIC':12,'DEC':12}
                mes = str(mes_numero[mes])
    
            if len(ano) < 4:
                ano = str((2000 if int(ano) <= Fecha.Ahora().AnioCorto() else 1900) + int(ano))
                
            if int(ano) < 1900:
                ano = '1900'
            
            return Fecha( datetime.datetime.strptime('%s-%s-%s' % (dia.zfill(2), mes.zfill(2), ano.zfill(4)), '%d-%m-%Y') )
            
        except Exception as e:
            return Fecha( date_default )

    #------------------------------------------------------------------------------------------
    def AStringConFormato(self, formato):
        
        if self._fecha is None:
            return ''
        else:
            return self._fecha.strftime(formato)

    #------------------------------------------------------------------------------------------
    def AStringConFormatoDefault(self):
        
        return self.AStringConFormato('%d/%m/%Y')

