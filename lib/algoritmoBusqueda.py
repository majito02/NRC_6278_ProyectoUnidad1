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

    crear_arbol(self,bordes):
        Crea el arbol segun el Array de nodos ingresado llamando al metodo agregar_borde

    imprimir_lista_adyacente():
        Imprimir la representación gráfica
    
     buscar_dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        Retorna la ruta desde un nodo inicial al final
        usa busqueda en profundidad

    buscar_bfs(nodo_inicial):
        Retorna el recorrido BFS de un vértice fuente dado.
        Usa busqueda transversal

    def obtener_ruta(self,inicio, objetivo):
        Retorna ruta y distancia usando busqueda_bfs
    """

    def __init__(self, num_de_nodos, bordes, dirigido=True):
        """
        Construye todo los atributos necesarios para el objeto Grafo.

        Parametros
        ----------
            num_de_nodos : int
                Numero de nodos de grafo
            bordes: Array
                Array de tuplas con cada borde del arbol a contruir
                [(nodo1,nodo2,peso),(nodo2,nodo3,peso),(nodo1,nodo3,peso),...]
            dirigido : bool
                Estado de dirigido
        """
        #Creacion de variables de clase
        self.peso_total = 0 #peso total recorido
        self.m_num_de_nodos = num_de_nodos
        self.m_nodos = range(1,self.m_num_de_nodos+1) #Rango con numero de nodos
        self.m_dirigido = dirigido
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}# Usamos un diccionario para implementar una lista de adyacencia      
        # Creacion de Arbol
        self.crear_arbol(bordes)#primero en ejecutar
        self.imprimir_lista_adyacente()

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
    
    def crear_arbol(self,bordes):
        """
        Crea arbol del grafo
        Se ingresa un Array de Tuplas de cada borde a ingresar
        Se llama iterativamente agregar_borde(nodo1,nodo2,peso) para agregar todos lo bordes

        Parametros
        ----------
        bordes: Array
            Array de tuplas con cada borde del arbol a contruir
            [(nodo1,nodo2,peso),(nodo2,nodo3,peso),(nodo1,nodo3,peso),...]

        Retorna
        -------
        None
        """
        for borde in bordes:
            nodo1 = borde[0]
            nodo2 = borde[1]
            peso = borde[2]
            self.agregar_borde(nodo1,nodo2,peso)

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
            #se imprimo el resultaod 
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def buscar_dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        """
        Devuelve el recorrido DFS de un vérticedado y atraviesa vértices alcanzables.
        Se detiene al alcanzar su objetivo
        Parametros
        ----------
        inicio : int
            Nodo inicial del Grafo a imprimir
        objetivo: int
            Nodo final de busqueda
        ruta : array
            arreglo donde se guarda la ruta
        visitado : set()
            auxiliar para nodos visitados

        Retorna
        -------
        Recorrido de nodos  [0 1 2 4 3 ...]
        """
        ruta.append(inicio)#agregargar ruta 
        visitado.add(inicio)#agregamos visitado 
        if inicio == objetivo:
            return ruta#retorna la ruta si el objetivo inicio el igual al objetivo 
        for (vecino, peso) in self.m_lista_adyacencia[inicio]:#recuperamos el vecino 
            if vecino not in visitado:#si no fue visitado 
                resultado = self.buscar_dfs(vecino, objetivo, ruta, visitado)
                if resultado is not None:#En caos que el resultado sea null
                    print("Busqueda DFS resultado ",resultado) # [19, 17, 12, 11, 5, 3]
                    return resultado #retornamos el resultaod 
        ruta.pop()
        return None

    def obtener_ruta(self,inicio, objetivo):# inicio = 19 y objetivo 3
        
        """
        Devuelve la ruta y peso total de la busqueda
        Parametros
        ----------
        inicio : int
            Nodo inicial del Grafo a imprimir
        objetivo: int
            Nodo final de busqueda

        Retorna
        -------
        Recorrido de nodos y peso total  [0 1 2 4 3 ...], peso_total
        """ 
        peso_total =0#variable acumulador 
        ruta = self.buscar_dfs(inicio, objetivo,[],set())
        #Recuperamos la ruta # [19, 17, 12, 11, 5, 3]
        #len(ruta)-1 -> 6-1 = 5
        for i in  range(len(ruta)-1):#5 veces
            #19 - 
            for nodo_vecino in self.m_lista_adyacencia[ruta[i]]:
                print("peso_total 17", self.m_lista_adyacencia[ruta[1]])
                #nodo 19 :  {(21, 2.9), (17, 1.62), (18, 4.72)}
                #nodo 17 :  {(12, 1.5), (13, 4.49), (5, 2.06), (19, 1.62), (18, 3.88)}
                #nodo 12 :  {(11, 1), (17, 1.5), (5, 1.65)}
                #nodo 11 :  {(12, 1), (5, 1.02), (4, 1.96)}
                #nodo 5 :  {(11, 1.02), (3, 2.63), (12, 1.65), (13, 3.82), (6, 3.2), (17, 2.06)}
                #nodo 3 :  {(5, 2.63), (1, 3.64), (4, 2.57), (6, 2.39)}
                # print("self.m_lista_adyacencia[ruta[i]",self.m_lista_adyacencia[ruta[i]])
                if nodo_vecino[0] == ruta[i+1]:
                    peso_total += nodo_vecino[1]
        print("[ruta,peso_total]",[ruta,peso_total])# [[19, 17, 12, 11, 5, 3], 7.7700000000000005]
        return [ruta,peso_total]

    def buscar_bfs(self, nodo_inicial,objetivo):
        """
        Devuelve el recorrido BFS de un vértice fuente dado y atraviesa vértices alcanzables desde s.
        Se detiene al alcanzar su objetivo
        Parametros
        ----------
        nodo_inicial : int
            Nodo inicial del Grafo a imprimir
        objetivo: int
            Nodo final de busqueda

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
                return ruta
            # Obtener todos los vértices adyacentes del vértice eliminado. 
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                # dyacente no ha sido visitado?
                if siguiente_nodo not in visitado:
                    #ponerlo en cola
                    cola.put(siguiente_nodo)
                    #marcarlo como visitado
                    visitado.add(siguiente_nodo)
                    
                    
                    
if __name__ == "__main__":
    grafo = Grafo()
    grafo.imprimir_lista_adyacente()


