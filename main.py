#importacion de clase QtWidgets de libreria PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

#Importacionde la clase Grafo del paquete AlgortimoBusqueda
from lib.algoritmoBusqueda import Grafo

# Importacion la ventana generada con QtDesigner5 como clase
from interfaz import Ui_ventanaPrincipal

class Ui_ventanaPrincipal(QtWidgets.QMainWindow, Ui_ventanaPrincipal):
    '''
    Clase herada que representa la ventana de interfaz grafica

    Attributos
    ----------
    por defectos el mismo ya que es una clase heredada

    Methodos
    -------
	__init__(self, *args, **kwargs):
		---Construye evenetos y acciones de la ventana principal
    
    '''
    def __init__(self, *args, **kwargs):
        '''
		
        Construye la venta dando acciones a elementos.

        Parametros
        ----------
        None

        Returno
        -------
        None
        
        '''
        # Inicializar ventana principal
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Construir ventana con estructura base
        self.setupUi(self)
        #---------para cargar todos los datos de la interfaz---------
        
        
        # Variable de conteo de seleccion de boton
        self.botones_presionados = 0
        # Variables de los nodos inicial y final
        self.nodo_inicial = 0
        self.nodo_final = 0
        
        
        self.elemento_inicial = self.nodo
        self.elemento_final = self.nodo
        
        # Variables de los nodos
        self.nodos = [self.nodo, self.nodo_2,self.nodo_3, self.nodo_4, self.nodo_5,
                    self.nodo_6, self.nodo_7, self.nodo_8, self.nodo_9, self.nodo_10,
                    self.nodo_11, self.nodo_12, self.nodo_13, self.nodo_14, self.nodo_15,
                    self.nodo_16, self.nodo_17, self.nodo_18, self.nodo_19, self.nodo_20,
                    self.nodo_21]
        
        
        #-----------------------------------------------------
        # Activacion de simulacion
        self.simulacion_activada = 0
        # Paso de simulacion
        self.paso_simulacion = 300 #milisegundos
        
        #Configurar reloj de simulacion
        self.temporizador = QtCore.QTimer(self)#creamos un objeto
        self.temporizador.setInterval(self.paso_simulacion) # cada 1000 ms / 1 segundo
        #Evento de relos
        self.temporizador.timeout.connect(self.simular_ruta)#una vez que pase el tiempo que se conecte en simular ruta
        self.temporizador.start()#temporizador
        self.nodos_simulacion = []#para cargar la ruta de la simulación 
        #-----------------------------------------------------
        self.contador = 0

        #1.  ----Eventos de los botones q reprentan los nodos
        self.nodo.clicked.connect(self.eleccion_puntos)
        self.nodo_2.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_3.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_4.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_5.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_6.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_7.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_8.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_9.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_10.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_11.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_12.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_13.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_14.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_15.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_16.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_17.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_18.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_19.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_20.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        self.nodo_21.clicked.connect(self.eleccion_puntos)#Evente del boton al dar clic  
        # Evento de boton Generar Ruta
        self.boton_generar.clicked.connect(self.generar_ruta)
        #Evento de Boton Reiniciar
        self.boton_reiniciar.clicked.connect(self.reiniciar)

        #2. Inicializacion de arbol y nodos  -- aplicamos automizaticamente
        self.bordes_nodos = [(1,2,3.55),(1,3,3.64),(2,7,0.82),(2,8,4.62),
            (3,6,2.39),(3,4,2.57),(3,5,2.63),(4,11,1.96),
            (5,11,1.02),(5,12,1.65),(5,17,2.06),(5,6,3.20),(5,13,3.82),
            (6,13,2.30),(6,7,2.36),(6,8,3.55),(6,16,6.81),
            (8,9,0.5),(9,10,2.23),(11,12,1),(12,17,1.5),
            (13,14,1),(13,18,2.77),(13,17,4.49),(14,15,1.5),
            (14,18,2.08),(15,18,2.70),(15,16,2.97),(17,19,1.62),
            (17,18,3.88),(18,20,2.45),(18,19,4.72),(19,21,2.90)]
        
        #----------------------------------------------------------------------
        #3. Creacion de Grafo    ---     Le enviamos todos los bordes de nodo
        self.grafo = Grafo(21, self.bordes_nodos,dirigido=False)
        #----------------------------------------------------------------------


    #4. 
    def eleccion_puntos(self):
        '''
        Verifica si se aplasto un boton.
        Si el primero (self.botones_presionados == 0) se pone verde y se toma como nodo inicial
        Si es el segundo (self.botones_presionados == 1) se pone rojo y se toma como nodo final
        Si self.botones_presionados >= 2 no hace nada

        Parametros
        ----------
        None

        Returno
        -------
        None
        
        '''
        #Verifica si se presiona un nodo por primera vez
        if self.botones_presionados == 0:
            #Se guarda el nodo inicial del boton
            self.nodo_inicial = int(self.sender().text())
            #Se guardo el boton del nodo inicial
            self.elemento_inicial = self.sender()
            #Aumentar conteo de botones presionados
            self.botones_presionados += 1
            #Cambiar color de fondo de nodo inicial
            self.elemento_inicial.setStyleSheet("background-color: rgb(0, 255, 0);")
        #Verifica si se presiona un nodo por segunda vez
        elif self.botones_presionados == 1:
            #Se guarda el nodo final
            self.nodo_final =  int(self.sender().text())
            #Se guardo el boton del nodo inicial
            self.elemento_final = self.sender()
            #Cambiar color de fondo de nodo inicial
            self.elemento_final.setStyleSheet("background-color: rgb(255, 0, 0);")
            #Aumentar conteo de botones presionados
            self.botones_presionados += 1
            

        
     #5 ....   
    def generar_ruta(self):
        '''
		
        Calcula la ruta mediante un algoritmo de busqueda
        Imprime en la etiqueta distancia la distancia total de la ruta
        Encera valores llamdo a self.reiniciar

        Parametros
        ----------
        None

        Returno
        -------
        None
        
        '''
        #sms de inicio
        print("Calculando ruta")
        #Algoritmo de Ruta
        ruta = []#para genera la ruta en un array
        distancia = 0#distancia 
        print(self.nodo_inicial, self.nodo_final)
        #--llamamos a la ruta y distancia y obetenenos la ruta
        #5.   --primer valor me obtiene la ruta y el segundo la distancia 
        [ruta, distancia]=self.grafo.obtener_ruta(int(self.nodo_inicial),int(self.nodo_final))
        print(ruta)
        print(distancia)
        
        
        # Arreglo de Botones
        self.nodos_simulacion = []#nodo simulacion no funciono 
        # Verificar cada punto de ruta con cada nodo
        for i in ruta:
            for j in self.nodos:
                if int(j.text()) == i and int(j.text()) != ruta[0]:
                    self.nodos_simulacion.append(j)#simulacion que no funciono 
        self.simulacion_activada = 1#Simulacion en proceso 
        self.contador = 0
        
        #Mostrar distancia en ventana
        self.distancia.setText(str(round(distancia,2)))
        #Mostrar ruta
        self.ruta_contenedor.setText(str(ruta))#me guarda un arreglo de la rta
        
        
        
    
    def reiniciar(self):
        '''
		
        Reinicia la accion, volviendo al color original los botones y encerando las variables

        Parametros
        ----------
        None

        Returno
        -------
        None
        
        '''
        # Reiniciar conteo de botones aplastados
        self.botones_presionados = 0#
        # Reiniciar color de fondo de los botones tomados
        for i in self.nodos:#reinicia todos los valores por defecto  
            #agregamos el color
            i.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.distancia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.distancia.setText("")
        self.ruta_contenedor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ruta_contenedor.setText("")

    def simular_ruta(self):
        '''
		
        Simula ruta generado cambiando los colores de los nodos que pasan la ruta
        Usa el evento de reloj

        Parametros
        ----------
        None
        Returno
        -------
        None
        
        '''
        if self.simulacion_activada == 1 and self.contador < len(self.nodos_simulacion):
            self.nodos_simulacion[self.contador].setStyleSheet("background-color: rgb(0, 0, 255);")
            self.contador +=1
        if self.simulacion_activada == 1 and self.contador == len(self.nodos_simulacion):
            # Resaltar etiqueta de distancia
            self.distancia.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.ruta_contenedor.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.simulacion_activada = 0
            self.contador = 0


#Correr programa si este es la raiz de ejecucion
if __name__ == "__main__":
    # Evento de cierre de la ventana tomanod ruta de archivo ejecutado con sys
    app = QtWidgets.QApplication([])
    # Crear objeto ventana de la clase generada
    ventana_principal = Ui_ventanaPrincipal()
    # Mostrar ventana principal
    ventana_principal.show()
    # Dar evento de fin de programa al cerrar ventana
    app.exec_()
    
    

