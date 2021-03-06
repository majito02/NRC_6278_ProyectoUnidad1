"""
        
Archivo generado con ayuda de QtDesigner5
Crear la interfaz gráfica de aplicación
Clases:
        Ui_ventanaPrincipal
Metodos:
		setupUi
        retranslateUi
"""

# Importacion de libreria PyQt5 para generacion de interfaz gráfica
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaPrincipal(object):
    '''
    Clase que representa la ventana de interfaz grafica

    Attributos
    ----------
    None

    Methodos
    -------
	setupUi(self, ventanaPrincipal):
		Construir estructura de la ventana grafica
    etranslateUi(self, ventanaPrincipal):
        Inicializa texto delos elementos que se encuentran en la ventana
    '''
    def setupUi(self, ventanaPrincipal):
        '''
		
        Estructura y crea la ventana principal.

        Parametros
        ----------
        ventanaPrincipal : QtWidgets.QMainWindow()
            Objeto de la clase QMainWindows del paquete QtWidgets

        Returno
        -------
        None
        
		'''
		# Dar propiedades de la ventana principal
        ventanaPrincipal.setObjectName("ventanaPrincipal")
        ventanaPrincipal.resize(985, 600)
        ventanaPrincipal.setMinimumSize(QtCore.QSize(985, 600))
        ventanaPrincipal.setMaximumSize(QtCore.QSize(985, 600))
        ventanaPrincipal.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
		# Crea un widget central para contener elementos y dar nombre
        self.centralwidget = QtWidgets.QWidget(ventanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
		# Crear botones con sus propiedades
        self.boton_generar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_generar.setGeometry(QtCore.QRect(0, 560, 101, 25))
        self.boton_generar.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.boton_generar.setObjectName("boton_generar")
        self.boton_reiniciar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_reiniciar.setGeometry(QtCore.QRect(110, 560, 89, 25))
        self.boton_reiniciar.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.boton_reiniciar.setObjectName("boton_reiniciar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 560, 81, 17))
		# Crear etiqueta  con texto distancia
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.distancia = QtWidgets.QLabel(self.centralwidget)
        self.distancia.setEnabled(True)
        self.distancia.setGeometry(QtCore.QRect(290, 560, 67, 17))
		# Crea un tipo de fuente para texto
        font = QtGui.QFont()
        font.setKerning(True)
		#Crear etiqueta  donde se observera la distancia recorrida
        self.distancia.setFont(font)
        self.distancia.setToolTip("")
        self.distancia.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"selection-background-color: rgb(252, 233, 79);\n"
"background-color: rgb(255, 255, 255);")
        self.distancia.setText("")
        self.distancia.setObjectName("distancia")
		#Crear etiqueta para texto km
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 560, 21, 17))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
		#Crear contenedor de imagen
        self.contenedor_imagen = QtWidgets.QLabel(self.centralwidget)
        self.contenedor_imagen.setGeometry(QtCore.QRect(-10, -10, 1000, 610))
        self.contenedor_imagen.setMinimumSize(QtCore.QSize(1000, 610))
        self.contenedor_imagen.setMaximumSize(QtCore.QSize(1000, 610))
        self.contenedor_imagen.setStyleSheet("")
        self.contenedor_imagen.setText("")
        self.contenedor_imagen.setPixmap(QtGui.QPixmap("img/nodos_mapa.png"))
        self.contenedor_imagen.setObjectName("contenedor_imagen")
		#Crear nodos como botones
        self.nodo = QtWidgets.QPushButton(self.centralwidget)
        self.nodo.setGeometry(QtCore.QRect(140, 60, 20, 20))
        self.nodo.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo.setObjectName("nodo")
        self.nodo_2 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_2.setGeometry(QtCore.QRect(300, 50, 20, 20))
        self.nodo_2.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_2.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_2.setObjectName("nodo_2")
        self.nodo_3 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_3.setGeometry(QtCore.QRect(280, 150, 20, 20))
        self.nodo_3.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_3.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_3.setObjectName("nodo_3")
        self.nodo_4 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_4.setGeometry(QtCore.QRect(180, 200, 20, 20))
        self.nodo_4.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_4.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_4.setObjectName("nodo_4")
        self.nodo_5 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_5.setGeometry(QtCore.QRect(250, 260, 20, 20))
        self.nodo_5.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_5.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_5.setObjectName("nodo_5")
        self.nodo_6 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_6.setGeometry(QtCore.QRect(400, 160, 20, 20))
        self.nodo_6.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_6.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_6.setObjectName("nodo_6")
        self.nodo_7 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_7.setGeometry(QtCore.QRect(330, 100, 20, 20))
        self.nodo_7.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_7.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_7.setObjectName("nodo_7")
        self.nodo_8 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_8.setGeometry(QtCore.QRect(510, 100, 20, 20))
        self.nodo_8.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_8.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_8.setObjectName("nodo_8")
        self.nodo_9 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_9.setGeometry(QtCore.QRect(550, 90, 20, 20))
        self.nodo_9.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_9.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_9.setObjectName("nodo_9")
        self.nodo_10 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_10.setGeometry(QtCore.QRect(640, 100, 20, 20))
        self.nodo_10.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_10.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.nodo_10.setObjectName("nodo_10")
        self.nodo_11 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_11.setGeometry(QtCore.QRect(200, 270, 20, 20))
        self.nodo_11.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_11.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_11.setObjectName("nodo_11")
        self.nodo_12 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_12.setGeometry(QtCore.QRect(190, 320, 20, 20))
        self.nodo_12.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_12.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_12.setObjectName("nodo_12")
        self.nodo_13 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_13.setGeometry(QtCore.QRect(420, 270, 20, 20))
        self.nodo_13.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_13.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_13.setObjectName("nodo_13")
        self.nodo_14 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_14.setGeometry(QtCore.QRect(450, 300, 20, 20))
        self.nodo_14.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_14.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_14.setObjectName("nodo_14")
        self.nodo_15 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_15.setGeometry(QtCore.QRect(510, 330, 20, 20))
        self.nodo_15.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_15.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_15.setObjectName("nodo_15")
        self.nodo_16 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_16.setGeometry(QtCore.QRect(670, 340, 20, 20))
        self.nodo_16.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_16.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_16.setObjectName("nodo_16")
        self.nodo_17 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_17.setGeometry(QtCore.QRect(250, 360, 20, 20))
        self.nodo_17.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_17.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_17.setObjectName("nodo_17")
        self.nodo_18 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_18.setGeometry(QtCore.QRect(420, 390, 20, 20))
        self.nodo_18.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_18.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_18.setObjectName("nodo_18")
        self.nodo_19 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_19.setGeometry(QtCore.QRect(200, 410, 20, 20))
        self.nodo_19.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_19.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_19.setObjectName("nodo_19")
        self.nodo_20 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_20.setGeometry(QtCore.QRect(360, 480, 20, 20))
        self.nodo_20.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_20.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_20.setObjectName("nodo_20")
        self.nodo_21 = QtWidgets.QPushButton(self.centralwidget)
        self.nodo_21.setGeometry(QtCore.QRect(120, 510, 20, 20))
        self.nodo_21.setMinimumSize(QtCore.QSize(20, 20))
        self.nodo_21.setMaximumSize(QtCore.QSize(20, 20))
        self.nodo_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nodo_21.setObjectName("nodo_21")
		#Crear etiqueta de ruta
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 560, 41, 17))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
		#Creae etiqueta para muestra de ruta
        self.ruta_contenedor = QtWidgets.QLabel(self.centralwidget)
        self.ruta_contenedor.setEnabled(True)
        self.ruta_contenedor.setGeometry(QtCore.QRect(440, 560, 361, 17))
        font = QtGui.QFont()
        font.setKerning(True)
        self.ruta_contenedor.setFont(font)
        self.ruta_contenedor.setToolTip("")
        self.ruta_contenedor.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"selection-background-color: rgb(252, 233, 79);\n"
"background-color: rgb(255, 255, 255);")
        self.ruta_contenedor.setText("")
        self.ruta_contenedor.setObjectName("ruta_contenedor")
		#Levantar elementos creados
        self.contenedor_imagen.raise_()
        self.boton_generar.raise_()
        self.boton_reiniciar.raise_()
        self.label.raise_()
        self.distancia.raise_()
        self.label_3.raise_()
        self.nodo.raise_()
        self.nodo_2.raise_()
        self.nodo_3.raise_()
        self.nodo_4.raise_()
        self.nodo_5.raise_()
        self.nodo_6.raise_()
        self.nodo_7.raise_()
        self.nodo_8.raise_()
        self.nodo_9.raise_()
        self.nodo_10.raise_()
        self.nodo_11.raise_()
        self.nodo_12.raise_()
        self.nodo_13.raise_()
        self.nodo_14.raise_()
        self.nodo_15.raise_()
        self.nodo_16.raise_()
        self.nodo_17.raise_()
        self.nodo_18.raise_()
        self.nodo_19.raise_()
        self.nodo_20.raise_()
        self.nodo_21.raise_()
        self.label_2.raise_()
        self.ruta_contenedor.raise_()
		# Dar contenedor padre a objeto creado
        ventanaPrincipal.setCentralWidget(self.centralwidget)
		# Inicializar el texto de cada elemento
        self.retranslateUi(ventanaPrincipal)
		# Iniciar ventana
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipal)

    def retranslateUi(self, ventanaPrincipal):
        """
        Inicializa el texto de cada elemento creado

        Parametros
        ----------
        ventanaPrincipal : QtWidgets.QMainWindow()
            Objeto de la clase QMainWindows del paquete QtWidgets

        Retorno
        -------
        None
        """
		#variable para idioma
        _translate = QtCore.QCoreApplication.translate
		# Nombre de titulo de ventana
        ventanaPrincipal.setWindowTitle(_translate("ventanaPrincipal", "Santo Domingo - Rutas"))
		#Texto de elementos ingresados
        self.boton_generar.setText(_translate("ventanaPrincipal", "Calcular Ruta"))
        self.boton_reiniciar.setText(_translate("ventanaPrincipal", "Reiniciar"))
        self.label.setText(_translate("ventanaPrincipal", "Distancia: "))
        self.label_3.setText(_translate("ventanaPrincipal", "km"))
        self.nodo.setText(_translate("ventanaPrincipal", "1"))
        self.nodo_2.setText(_translate("ventanaPrincipal", "2"))
        self.nodo_3.setText(_translate("ventanaPrincipal", "3"))
        self.nodo_4.setText(_translate("ventanaPrincipal", "4"))
        self.nodo_5.setText(_translate("ventanaPrincipal", "5"))
        self.nodo_6.setText(_translate("ventanaPrincipal", "6"))
        self.nodo_7.setText(_translate("ventanaPrincipal", "7"))
        self.nodo_8.setText(_translate("ventanaPrincipal", "8"))
        self.nodo_9.setText(_translate("ventanaPrincipal", "9"))
        self.nodo_10.setText(_translate("ventanaPrincipal", "10"))
        self.nodo_11.setText(_translate("ventanaPrincipal", "11"))
        self.nodo_12.setText(_translate("ventanaPrincipal", "12"))
        self.nodo_13.setText(_translate("ventanaPrincipal", "13"))
        self.nodo_14.setText(_translate("ventanaPrincipal", "14"))
        self.nodo_15.setText(_translate("ventanaPrincipal", "15"))
        self.nodo_16.setText(_translate("ventanaPrincipal", "16"))
        self.nodo_17.setText(_translate("ventanaPrincipal", "17"))
        self.nodo_18.setText(_translate("ventanaPrincipal", "18"))
        self.nodo_19.setText(_translate("ventanaPrincipal", "19"))
        self.nodo_20.setText(_translate("ventanaPrincipal", "20"))
        self.nodo_21.setText(_translate("ventanaPrincipal", "21"))
        self.label_2.setText(_translate("ventanaPrincipal", "Ruta:"))

#Funcion de corrida si se habre desde esta venta - para test
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_ventanaPrincipal()
    ui.setupUi(ventanaPrincipal)
    ventanaPrincipal.show()
    sys.exit(app.exec_())
