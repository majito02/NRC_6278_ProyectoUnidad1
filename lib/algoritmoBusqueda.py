# Importar clase Queue de libreria queue
from queue import Queue

# Declarar clase Grafo
class Grafo:
    """
    Clase para representar un grafo

    ...

    Attributos
    ----------
    m_num_de_nodos : int
        numero de nodos de grafo
    m_nodos : range
        rango de nodos
    m_dirigido : bool
        Estado de dirigido
    m_lista_adyacencia : Array
        Lista de ayacencia

    Metodos
    -------
    agregar_borde(nodo1, nodo2, peso=1):
         Agregar borde al gráfico.
    
    imprimir_lista_adyacente():
        Imprimir la representación gráfica

    bfs_transversal(nodo_inicial):
         Imprimir el recorrido BFS de un vértice fuente dado.
    
    """

    def __init__(self, num_de_nodos, dirigido=True):
        """
        Construye todo los atributos necesarios para el objeto Grafo.

        Parametros
        ----------
            num_de_nodos : int
                Numero de nodos de grafo
            dirigido : bool
                Estado de dirigido
        """

        self.m_num_de_nodos = num_de_nodos
        self.m_nodos = range(self.m_num_de_nodos) #Rango con numero de nodos
        self.m_dirigido = dirigido
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}# Usamos un diccionario para implementar una lista de adyacencia      
	
    def agregar_borde(self, nodo1, nodo2, peso=1):
        """
        Agrega un borde al Grafo

        Si el argumento peso no es pasado, then toma como valor por defecto 1

        Parametros
        ----------
        nodo1 : int
            Número de nodo1
        nodo2 : int
            Número de nodo2
        peso : int (opcional)
            Peso del borde. por defento 1.

        Retorna
        -------
        None
        """

        # Agregar nodo2 a lista en nodo1
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        # No Dirigido?
        if not self.m_dirigido:
            # Agregar nodo 1 a lista en nodo2
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
    
    def imprimir_lista_adyacente(self):
        """
        Imprime la representación gráfica

        Parametros
        ----------
        Ninguno

        Retorna
        -------
        nodo$(llave): {m_lista_adyacencia[llave]}
        """

        #Recorrer por la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # Imprimir nodo
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def bfs_transversal(self, nodo_inicial,objetivo):
        """
        Imprime el recorrido BFS de un vértice fuente dado y atraviesa vértices alcanzables desde s.

        Parametros
        ----------
        nodo_inicial : int
            Nodo inicial del Grafo a imprimir

        Retorna
        -------
        Recorrido de nodos ( 0 1 2 4 3 ...)
        """
        # Conjunto de nodos visitados para evitar bucles
        visitado = set()
        cola = Queue()
        # Agregue nodo_inicial a la cola
        cola.put(nodo_inicial)
        # Agregue a la lista visitada
        visitado.add(nodo_inicial)
        ruta=[]
        # Bucle de impresion de nodos
        while not cola.empty():
            # Quitar un vértice de la cola
            nodo_actual = cola.get()
            # Imprimirlo vertice
            print(nodo_actual, end = " ")
            ruta.append(nodo_actual)
            if nodo_actual == objetivo:
                print("encontrado")
                return ruta
            # Obtener todos los vértices adyacentes del vértice eliminado. 
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                # dyacente no ha sido visitado?
                if siguiente_nodo not in visitado:
                    #ponerlo en cola
                    cola.put(siguiente_nodo)
                    #marcarlo como visitado
                    visitado.add(siguiente_nodo)

