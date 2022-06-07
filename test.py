#Importacionde la clase Grafo del paquete AlgortimoBusqueda
from lib.algoritmoBusqueda import Grafo

#Inicializacion de arbol y nodos
bordes_nodos = [(1,2,3.55),(1,3,3.64),(2,7,0.82),(2,8,4.62),
            (3,6,2.39),(3,4,2.57),(3,5,2.63),(4,11,1.96),
            (5,11,1.02),(5,12,1.65),(5,17,2.06),(5,6,3.20),(5,13,3.82),
            (6,13,2.30),(6,7,2.36),(6,8,3.55),(6,16,6.81),
            (8,9,0.5),(9,10,2.23),(11,12,1),(12,17,1.5),
            (13,14,1),(13,18,2.77),(13,17,4.49),(14,15,1.5),
            (14,18,2.08),(15,18,2.70),(15,16,2.97),(17,19,1.62),
            (17,18,3.88),(18,20,2.45),(18,19,4.72),(19,21,2.90)]
grafo = Grafo(21, bordes_nodos,dirigido=False)

print(grafo.obtener_ruta(1,8))
print(grafo.obtener_ruta(1,8))
