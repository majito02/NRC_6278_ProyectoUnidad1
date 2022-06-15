# Importar libreria para test
import unittest
from unittest import result
# Importar archico a testear
from lib.algoritmoBusqueda import Grafo

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
    test_arbol_simple(self):
        Verifica busqueda dfs de un arbol simple

    test_ruta_simple(self):
        Prueba la ruta y peso de un arbol simple

    test_pesos_diferentes(self):
        Prueba un arbol con diferentes pasos
    
    test_arbol_ciclo(self):
        Prueba un arbol con conexin de nodos ciclcos

    test_no_dirigido(self):
        Prueba un arbol ciclico no dirigido
    """
    def test_arbol_simple(self):
        #Colección de tipo arreglo con sus bordes respectivos 
        bordes =[(1,2,1),(1,3,1),(2,4,1),(2,5,1),(3,6,1),(3,7,1)]
        #Inicialización de la clase Grafo 
        grafo1 = Grafo(7,bordes)
        resultado = grafo1.buscar_dfs(1,7,[],set())
        print(resultado)
        #Comprobación de la busqueda por DFS
        self.assertEqual(resultado, [1,3,7],'Busqueda DFS incorrecta')
    
    def test_ruta_simple(self):
        #Colección de tipo arreglo con sus bordes respectivos 
        bordes =[(1,2,1),(1,3,1),(2,4,1),(2,5,1),(3,6,1),(3,7,1)]
        #Inicialización de la clase Grafo 
        grafo = Grafo(7,bordes)
        resultado = grafo.obtener_ruta(1,7)
        #Comprobación si el resultado de la ruta es la correspondiente
        self.assertEqual(resultado,[[1, 3, 7], 2],'Ruta y distancia incorrecta')

    def test_pesos_diferentes(self):
        #Colección de tipo arreglo con sus bordes respectivos 
        bordes =[(1,2,5),(1,3,1),(2,4,0.5),(4,5,7.2),(3,6,1.04),(6,5,0.3)]
        #Inicialización de la clase Grafo 
        grafo = Grafo(6,bordes)
        #Comprobación si el resultado de la ruta es la correspondiente
        self.assertEqual(grafo.obtener_ruta(2,5),[[2, 4, 5], 7.7], 'Error con pesos diferentes')
    
    def test_arbol_ciclo(self):

        #Colección de tipo arreglo con sus bordes respectivos 
        bordes =[(1,2,1),(1,3,1),(2,4,1),(4,5,1),(3,6,1),(6,5,1)]
        #Inicialización de la clase Grafo 
        grafo = Grafo(6,bordes)
        resultado = grafo.buscar_dfs(1,5,[],set())
        #Comprobación si el resultado de la busqueda es la correspondiente
        self.assertEqual(resultado,[1, 3, 6, 5], 'Error en arbol ciclico')

    def test_no_dirigido(self):

        #Colección de tipo arreglo con sus bordes respectivos 
        bordes =[(1,2,5),(1,3,1),(2,4,0.5),(4,5,7.2),(3,6,1.04),(6,5,0.3),(6,7,1)]
        #Inicialización de la clase Grafo 
        grafo = Grafo(7,bordes,False)
        #Comprobación si el resultado de la ruta es la correspondiente
        self.assertEqual(grafo.obtener_ruta(6,1),[[6, 3, 1], 2.04], 'Error con arbol no dirigido')

#Funcion principal 
if __name__ == '__main__':
    unittest.main()