
def mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico):
            if ubicaion_objetivo != 'Quito':
                if estadoA  == 'Con trafico':
                    mensaje_trafico += f'\nMoviendose a la ubucación Quito'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    estado_campo['Quito'] = 'Sin Trafico'
                    mensaje_trafico += f'\n Reduciendo el tráfico en Quito' 
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
               
            if ubicaion_objetivo != 'Chone':     
                if estadoB  == 'Con trafico':
                    mensaje_trafico += f'\nMoviendose a la ubucación Chone'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    estado_campo['Chone'] = 'Sin Trafico'
                    mensaje_trafico += f'\n Reduciendo el tráfico en Chone' 
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
             
            if ubicaion_objetivo != 'Lorena':     
                if estadoC  == 'Con trafico':
                    mensaje_trafico += f'\nMoviendose a la ubucación Lorena'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    mensaje_trafico += f'\n Reduciendo el tráfico en Lorena' 
                    coste_acumulador += 1
                    estado_campo['Lorena'] = 'Sin Trafico'
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
            
            if ubicaion_objetivo != 'Abraham Calazacon':   
                if estadoD == 'Con trafico':
                    mensaje_trafico += f'\nMoviendose a la ubucación Abraham Calazacón'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    mensaje_trafico += f'\n Reduciendo el tráfico en Abraham Calazacón' 
                    estado_campo['Abraham Calazacon'] = 'Sin Trafico'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                
            if ubicaion_objetivo != 'Luis Alberto': 
                if estadoE == 'Con trafico':
                    mensaje_trafico += f'\nMoviendose a la ubucación Luis Alberto'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    mensaje_trafico += f'\n Reduciendo el tráfico en Luis Alberto' 
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    estado_campo['Luis Alberto'] = 'Sin Trafico'
            
            
            if ubicaion_objetivo != 'Valencia': 
                if estadoF == 'Con trafico':
                    mensaje_trafico += f'\nMoviendose a la ubucación Valencia'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    mensaje_trafico += f'\n Reduciendo el tráfico en Valencia' 
                    estado_campo['Valencia'] = 'Sin Trafico'
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
            
            if ubicaion_objetivo != 'Pilaton': 
                if estadoG == 'Con trafico':
                    mensaje_trafico += f'\nMoviendose a la ubucación Pilatón'
                    coste_acumulador += 1
                    estado_campo['Pilaton'] = 'Sin Trafico'
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                    mensaje_trafico += f'\n Reduciendo el tráfico en Pilatón' 
                    coste_acumulador += 1
                    mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}'
            print(mensaje_trafico)
                
def calcularTrafico(self,ubicaion_objetivo = 'Chone',estadoA = 'Con trafico',estadoB = 'Con trafico',estadoC = 'Con trafico' ,estadoD = 'Con trafico',estadoE = 'Con trafico',estadoF = 'Con trafico',estadoG = 'Con trafico'):
  
    estado_campo = {'Quito': 'Con trafico', 'Chone': 'Sin Trafico', 'Lorena': 'Sin Trafico', 'Abraham Calazacon': 'Sin Trafico','Luis Alberto': 'Sin Trafico', 'Valencia': 'Sin Trafico', 'Pilaton': 'Sin Trafico'}  # Creamos un diccionario con su (key, value)
    coste_acumulador = 0 #variable acumuladore
    mensaje_trafico = ''

    if ubicaion_objetivo == 'Quito':
        mensaje_trafico = 'La ubicación selecccionado fue Quito'
        if estadoA == 'Con trafico':
            mensaje_trafico += '\nLa ubicación Quito tiene tráfico'
            estado_campo['Quito'] = 'Sin Trafico'
            coste_acumulador += 1
            
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)         
        if estadoA == 'Sin Trafico':
            mensaje_trafico += '\nLa ubicación Quito no tiene tráfico'
            print('Sin tráfico en Quito')
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
                
    elif ubicaion_objetivo == 'Chone':
        mensaje_trafico = 'La ubicación selecccionado fue Chone'
        if estadoB == 'Con trafico':
            mensaje_trafico += '\nLa ubicación Chone tiene tráfico'
            coste_acumulador += 1
            mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
            estado_campo['Chone'] = 'Sin Trafico'
            
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)         
        if estadoB == 'Sin Trafico':
            mensaje_trafico += '\nLa ubicación Chone no tiene tráfico'
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
            
    elif ubicaion_objetivo == 'Lorena':
        mensaje_trafico = 'La ubicación selecccionado fue Lorena'
        if estadoC == 'Con trafico':
            mensaje_trafico += '\nLa ubicación Lorena tiene tráfico'
            estado_campo['Lorena'] = 'Sin Trafico'
            coste_acumulador += 1
            mensaje_trafico += '\nLa ubicación Lorena no tiene tráfico'
            
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)         
        if estadoC == 'Sin Trafico':
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
        
    elif ubicaion_objetivo == 'Abraham Calazacon':
        mensaje_trafico = 'La ubicación selecccionado fue Abraham Calazacón'
        if estadoD == 'Con trafico':
            mensaje_trafico += '\nLa ubicación Abraham Calazacón tiene tráfico'
            estado_campo['Abraham Calazacon'] = 'Sin Trafico'
            coste_acumulador += 1
            
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)         
        if estadoD == 'Sin Trafico':
            mensaje_trafico += '\nLa ubicación Abraham Calazacón no tiene tráfico'
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
            
    elif ubicaion_objetivo == 'Luis Alberto':
        mensaje_trafico = 'La ubicación selecccionado fue Luis Alberto'
        if estadoE == 'Con trafico':
            mensaje_trafico += '\nLa ubicación Luis Alberto tiene tráfico'
            estado_campo['Luis Alberto'] = 'Sin Trafico'
            coste_acumulador += 1
            
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)         
        if estadoE == 'Sin Trafico':
            mensaje_trafico += '\nLa ubicación Luis Alberto no tiene tráfico'
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
              
    elif ubicaion_objetivo == 'Valencia':
        mensaje_trafico = 'La ubicación selecccionado fue Valencia'
        if estadoE == 'Con trafico':
            mensaje_trafico += '\nLa ubicación Valencia tiene tráfico'
            estado_campo['Valencia'] = 'Sin Trafico'
            coste_acumulador += 1
            
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)         
        if estadoE == 'Sin Trafico':
            mensaje_trafico += '\nLa ubicación Valencia no tiene tráfico'
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
               
                
    elif ubicaion_objetivo == 'Pilaton':
        mensaje_trafico = 'La ubicación selecccionado fue Pilatón'
        if estadoG == 'Con trafico':
            mensaje_trafico += '\nLa ubicación Pilatón tiene tráfico'
            estado_campo['Pilaton'] = 'Sin Trafico'
            coste_acumulador += 1
            
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)         
        if estadoE == 'Sin Trafico':
            mensaje_trafico += '\nLa ubicación Pilatón no tiene tráfico'
            mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicaion_objetivo,mensaje_trafico)
    
    # print(mensaje_trafico)
calcularTrafico('Quito')
