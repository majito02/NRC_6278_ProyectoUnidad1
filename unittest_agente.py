# Importar libreria para test
import unittest
from unittest import result
# Importar archico a testear

#importamos la clase grafo
from  lib.unittest_agente_funcional import Agente 
#Clase TestAlgoritmoDeBusqueda
class TestAlgoritmoDeBusqueda(unittest.TestCase):
       
      """
      Clase para testear algoritmo

      ...

      Attributos
      ----------
      None

      Metodos de prueba
      -------
      test_costo_acumulado(self):
        Verifica si la medida de rendimiento es correcta  

      test_ubicacion_objetivo(self):
         Verifica si la ciudad escogida es correcta 

      test_estados_esperados(self):
         Prueba para ver sin los resultados esperados son correctos 
      
      """
      
      def test_costo_acumulador(self):     
         #Creación del objeto agente 
         agente =  Agente ()
         #Calculamos la medida de rendimiento
         agente.calcularTrafico()
         #Comprobación si el resultado de la medida de rendimiento es la correcta 
         self.assertEqual(agente.resultado_costo_acumulador(), 13,'El resultado es incorrecto')
         
      def test_ubicacion_objetivo(self):     
         #Creación del objeto agente 
         agente =  Agente ()
         #Calculamos la medida de rendimiento
         agente.calcularTrafico()
         #Comprobación si la ciudad objetiva es correcta 
         self.assertEqual(agente.ubicacion_objetivo(), 'Chone','Ciudad incorecta')
         
      def test_estados_esperados(self):     
            #Creación del objeto agente 
            agente =  Agente ()
            #Calculamos la medida de rendimiento
            agente.calcularTrafico()
            #Comprobación si los resultados esperados son los correspondientes
            self.assertEqual(agente.estados_esperados(), {'Quito': 'Sin Trafico', 'Chone': 'Sin Trafico', 'Lorena': 'Sin Trafico', 'Abraham Calazacon': 'Sin Trafico', 'Luis Alberto': 'Sin Trafico', 'Valencia': 'Sin Trafico', 'Pilaton': 'Sin Trafico'},'Ciudad incorecta')
#Principal              
if __name__ == '__main__':
    unittest.main()