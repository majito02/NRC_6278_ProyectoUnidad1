   

class Agente ():
    
    def __init__(self) :
        self.m_costo_acumulaod = 0
        self.m_ubicacion_objetivo = ''
        self.resultado_esperado = {}
        

    def mensaje(self,estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico):

        """
        Muestra un mensaje en la interfaz.
        
        Parámetros
        ----------
            estadoA: str
                Estado A.
            estadoB: str
                Estado B.
            estadoC: str
                Estado C.
            estadoD: str
                Estado D.
            estadoE: str
                Estado E.
            estadoF: str
                Estado F.
            estadoG: str
                Estado G.
            coste_acumulador: int
                Coste acumulador.
            estado_campo: str
                Estado campo.
            ubicaion_objetivo: str
                Ubicación objetivo.
            mensaje_trafico: str
                Mensaje trafico.

        Retorna
        --------
            None
        """
            #si quito tiene trafico  = 1
        #si quito tiene trafico  = 0
        if ubicaion_objetivo != 'Quito':
            if estadoA  == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubucación Quito'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Quito'] = 'Sin Trafico'
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Quito' 
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
            
        if ubicaion_objetivo != 'Chone':   #yes  
            if estadoB  == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubucación Chone'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Chone'] = 'Sin Trafico'
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Chone' 
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
            
        if ubicaion_objetivo != 'Lorena':     
            if estadoC  == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubucación Lorena'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Lorena' 
                coste_acumulador += 1 #consto acumulador 
                estado_campo['Lorena'] = 'Sin Trafico'
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
        
        if ubicaion_objetivo != 'Abraham Calazacon':   
            if estadoD == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubucación Abraham Calazacón'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Abraham Calazacón' 
                estado_campo['Abraham Calazacon'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}'#5
            
        if ubicaion_objetivo != 'Luis Alberto': 
            if estadoE == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubucación Luis Alberto'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Luis Alberto' 
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Luis Alberto'] = 'Sin Trafico'
        
        
        if ubicaion_objetivo != 'Valencia': 
            if estadoF == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubucación Valencia'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Valencia' 
                estado_campo['Valencia'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
        
        if ubicaion_objetivo != 'Pilaton': 
            if estadoG == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubucación Pilatón'
                coste_acumulador += 1 #consto acumulador 
                estado_campo['Pilaton'] = 'Sin Trafico'
                #variable cumulador para imprimit mensaje de cada localidad     
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Pilatón' 
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}'
   
        print(mensaje_trafico)
        self.m_costo_acumulaod = coste_acumulador
        self.resultado_esperado = estado_campo
                #Los parametros de la función - inicializados 
    def calcularTrafico(self,ubicaion_objetivo = 'Chone',estadoA = 'Con trafico',estadoB = 'Con trafico',estadoC = 'Con trafico',estadoD = 'Con trafico',estadoE= 'Con trafico',estadoF = 'Con trafico',estadoG = 'Con trafico'):
        """
        Función que calcula el trafico en cada campo.
        Parámetros
        ----------
            ubicaion_objetivo: str
                Ubicación objetivo.
            estadoA: str
                Estado del campo A.
            estadoB: str
                Estado del campo B.
            estadoC: str
                Estado del campo C.
            estadoD: str
                Estado del campo D.
            estadoE: str
                Estado del campo E.
            estadoF: str
                Estado del campo F.
            estadoG: str
                Estado del campo G.

        Retorno
        -------
            trafico: int
                Trafico en cada campo.
        """

        # Creamos un diccionario con su (key, value)  - resultado esperado  
        estado_campo = {'Quito': 'Sin Trafico', 'Chone': 'Sin Trafico', 'Lorena': 'Sin Trafico', 'Abraham Calazacon': 'Sin Trafico','Luis Alberto': 'Sin Trafico', 'Valencia': 'Sin Trafico', 'Pilaton': 'Sin Trafico'}
        coste_acumulador = 0 #variable acumuladore los costos
        mensaje_trafico = '' #mensaje que va a imprimir todos los resultados 
        self.m_ubicacion_objetivo = ubicaion_objetivo
        if ubicaion_objetivo == 'Quito':
            mensaje_trafico = 'La ubicación selecccionado fue Quito'
            if estadoA == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Quito tiene tráfico'
                estado_campo['Quito'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
          
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoA == 'Sin Trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Quito no tiene tráfico'
                print('Sin tráfico en Quito')
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
        
        elif ubicaion_objetivo == 'Chone':
            mensaje_trafico = 'La ubicación selecccionado fue Chone'
            if estadoB == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Chone tiene tráfico'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Chone'] = 'Sin Trafico'
                
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoB == 'Sin Trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Chone no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicaion_objetivo == 'Lorena':
            mensaje_trafico = 'La ubicación selecccionado fue Lorena'
            if estadoC == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Lorena tiene tráfico'
                estado_campo['Lorena'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Lorena no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoC == 'Sin Trafico':
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
            
        elif ubicaion_objetivo == 'Abraham Calazacon':
            mensaje_trafico = 'La ubicación selecccionado fue Abraham Calazacón'
            if estadoD == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Abraham Calazacón tiene tráfico'
                estado_campo['Abraham Calazacon'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoD == 'Sin Trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Abraham Calazacón no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicaion_objetivo == 'Luis Alberto':
            mensaje_trafico = 'La ubicación selecccionado fue Luis Alberto'
            if estadoE == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Luis Alberto tiene tráfico'
                estado_campo['Luis Alberto'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoE == 'Sin Trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Luis Alberto no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicaion_objetivo == 'Valencia':
            mensaje_trafico = 'La ubicación selecccionado fue Valencia'
            if estadoE == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Valencia tiene tráfico'
                estado_campo['Valencia'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoE == 'Sin Trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Valencia no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicaion_objetivo == 'Pilaton':
            mensaje_trafico = 'La ubicación selecccionado fue Pilatón'
            if estadoG == 'Con trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Pilatón tiene tráfico'
                estado_campo['Pilaton'] = 'Sin Trafico'
                coste_acumulador += 1 #consto acumulador 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoE == 'Sin Trafico':
                #variable cumulador para imprimit mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Pilatón no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
      
    def resultado_costo_acumulador(self):
        return self.m_costo_acumulaod
    
    def ubicacion_objetivo(self):
        return self.m_ubicacion_objetivo
    
    def estados_esperados(self):
        return self.resultado_esperado
if __name__ == "__main__":

    agente = Agente()
    agente.calcularTrafico()
    print(agente.estados_esperados())

