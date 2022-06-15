
#importacion de clase QtWidgets de libreria PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets,uic,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

#Para llamar a la interfaz e importa el archivo UI generado previamente
from interfaz_agente import Ui_MainWindow


# Importacion la ventana generada con QtDesigner5 como clase
class Ui_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Clase que calcula el trafico de los estados mediante una interfaz grafica
    ...

    Atributos
    ---------
        args: list
            Lista de argumentos que se le pasan al constructor.
        kwargs: dict
            Diccionario de argumentos que se le pasan al constructor.   
    Métodos
    -------
        __init__(self, *args, **kwargs):
            Constructor de la clase Ui_MainWindow.
        calcularTrafico(self, ubicacion_objetivo, estadoA, estadoB, estadoC, estadoD, estadoE, estadoF, estadoG):
            Calcula el trafico de los estados.
        calculos(self):
            Calcula el trafico de los estados.
        mensaje(self, mensaje):
            Muestra un mensaje en la interfaz.

    """

    #Constructor
    def __init__(self, *args, **kwargs):#constructor  
        """
        Constructor de la clase UI_MainWindow.

        Parámetros
        ----------
            *args: list
                Lista de argumentos que se le pasan al constructor.
            **kwargs: dict
                Diccionario de argumentos que se le pasan al constructor.

        Retorna
        --------
            None
        
        """
        # Inicializar ventana principal
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Construir ventana con estructura base
        # Método interno para generar la interfaz
        self.setupUi(self)
        #Evento del botón al dar clic
        self.calcular.clicked.connect(self.calculos) #Boton calcular objetivo

    def calculos(self):
        """
        Calcula el trafico de los estados.
        
        Parámetros
        ----------
            None
            
        Retorna
        --------
            None
        """
        
        
        #recuperamos los datos del comboBox
        ubicacion_objetivo = str(self.comboBox.currentText())#recuperando comboBox de la ubicación objetivo 
        estadoA = str(self.comboBox_2.currentText())#recuperando comboBox de Quito
        estadoB = str(self.comboBox_3.currentText())#recuperando comboBox de Chone
        estadoC = str(self.comboBox_4.currentText())#recuperando comboBox de Lorena 
        estadoD = str(self.comboBox_5.currentText())#recuperando comboBox de Abraham Calazacon
        estadoE = str(self.comboBox_6.currentText())#recuperando comboBox de Luis Alberto
        estadoF = str(self.comboBox_7.currentText())#recuperando comboBox de Valencia
        estadoG = str(self.comboBox_8.currentText())#recuperando comboBox de Pilaton
       
        #Función calcular trafico que se le inicializa los valor con los  comboBox
        self.calcularTrafico(ubicacion_objetivo,estadoA,estadoB,estadoC ,estadoD,estadoE ,estadoF ,estadoG)
        
       
    def mensaje(self,estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico):

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
            ubicacion_objetivo: str
                Ubicación objetivo.
            mensaje_trafico: str
                Mensaje trafico.

        Retorna
        --------
            None
        """
           #si quito tiene trafico  = 1
        #si quito no tiene trafico  = 0
        if ubicacion_objetivo != 'Quito':
            if estadoA  == 'Con trafico':
                #variable acumuladora para imprimir mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubicación Quito'
                coste_acumulador += 1 #costo acumulador 
                #variable acumuladora para imprimit mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Quito'] = 'Sin Trafico'
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Quito' 
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
            
        if ubicacion_objetivo != 'Chone':   #yes  
            if estadoB  == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubicación Chone'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Chone'] = 'Sin Trafico'
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Chone' 
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
            
        if ubicacion_objetivo != 'Lorena':     
            if estadoC  == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubicación Lorena'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Lorena' 
                coste_acumulador += 1 #costo acumulado
                estado_campo['Lorena'] = 'Sin Trafico'
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
        
        if ubicacion_objetivo != 'Abraham Calazacon':   
            if estadoD == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubicación Abraham Calazacón'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Abraham Calazacón' 
                estado_campo['Abraham Calazacon'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}'#5
            
        if ubicacion_objetivo != 'Luis Alberto': 
            if estadoE == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubicación Luis Alberto'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Luis Alberto' 
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Luis Alberto'] = 'Sin Trafico'
        
        
        if ubicacion_objetivo != 'Valencia': 
            if estadoF == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubicación Valencia'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Valencia' 
                estado_campo['Valencia'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
        
        if ubicacion_objetivo != 'Pilaton': 
            if estadoG == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\nMoviendose a la ubicación Pilatón'
                coste_acumulador += 1 #costo acumulado
                estado_campo['Pilaton'] = 'Sin Trafico'
                #variable acumuladora para imprimitr mensaje de cada localidad     
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Reduciendo el tráfico en Pilatón' 
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}'
                
        #imprime los mensajes del tráfico 
        print(mensaje_trafico)
        self.mostrar.setText(mensaje_trafico)#muestra toda los mensajes recopilados
        #se establece la medición de rendimiento en textedit2
        mensaje2 = f'Medición de rendimiento: {str(coste_acumulador)}'
        self.textEdit_2.setText(mensaje2)#muestra la medida de rendimiento total
    
    #Los parametros de la función - inicializados 
    def calcularTrafico(self,ubicacion_objetivo ,estadoA ,estadoB ,estadoC ,estadoD ,estadoE,estadoF ,estadoG ):
        """
        Función que calcula el trafico en cada campo.
        Parámetros
        ----------
            ubicacion_objetivo: str
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

        if ubicacion_objetivo == 'Quito':
            mensaje_trafico = 'La ubicación selecccionado fue Quito'
            if estadoA == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Quito tiene tráfico'
                estado_campo['Quito'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                
                
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoA == 'Sin Trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Quito no tiene tráfico'
                print('Sin tráfico en Quito')
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                    
        elif ubicacion_objetivo == 'Chone':
            mensaje_trafico = 'La ubicación selecccionado fue Chone'
            if estadoB == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Chone tiene tráfico'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                estado_campo['Chone'] = 'Sin Trafico'
                
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoB == 'Sin Trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Chone no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicacion_objetivo == 'Lorena':
            mensaje_trafico = 'La ubicación selecccionado fue Lorena'
            if estadoC == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Lorena tiene tráfico'
                estado_campo['Lorena'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Lorena no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoC == 'Sin Trafico':
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
            
        elif ubicacion_objetivo == 'Abraham Calazacon':
            mensaje_trafico = 'La ubicación selecccionado fue Abraham Calazacón'
            if estadoD == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Abraham Calazacón tiene tráfico'
                estado_campo['Abraham Calazacon'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoD == 'Sin Trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Abraham Calazacón no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicacion_objetivo == 'Luis Alberto':
            mensaje_trafico = 'La ubicación selecccionado fue Luis Alberto'
            if estadoE == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Luis Alberto tiene tráfico'
                estado_campo['Luis Alberto'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoE == 'Sin Trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Luis Alberto no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicacion_objetivo == 'Valencia':
            mensaje_trafico = 'La ubicación selecccionado fue Valencia'
            if estadoE == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Valencia tiene tráfico'
                estado_campo['Valencia'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoE == 'Sin Trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Valencia no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
                
        elif ubicacion_objetivo == 'Pilaton':
            mensaje_trafico = 'La ubicación selecccionado fue Pilatón'
            if estadoG == 'Con trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Pilatón tiene tráfico'
                estado_campo['Pilaton'] = 'Sin Trafico'
                coste_acumulador += 1 #costo acumulado
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 
                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores          
            if estadoE == 'Sin Trafico':
                #variable acumuladora para imprimitr mensaje de cada localidad 
                mensaje_trafico += '\nLa ubicación Pilatón no tiene tráfico'
                mensaje_trafico += f'\n Costo actual {str(coste_acumulador)}' 

                self.mensaje(estadoA,estadoB,estadoC,estadoD,estadoE,estadoF,estadoG,coste_acumulador,estado_campo,ubicacion_objetivo,mensaje_trafico)
                #llamamos a la funcion mensaje y le inicalizamos los valores 
      
        
if __name__ == "__main__":
    """
    Función principal del agente.
    """

    app = QtWidgets.QApplication([])
    # Crear objeto ventana de la clase generada
    ventana_principal = Ui_MainWindow()
    # Mostrar ventana principal
    ventana_principal.show()
    # Dar evento de fin de programa al cerrar ventana
    app.exec_()
    