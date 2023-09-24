import graphviz 

class Arbol:
    def __init__(self):
        self.dot = graphviz.Digraph(comment= "Diagrama")
        self.counter = 0

    def agregarConfiguracion(self, conf):
        self.dot.attr('node', style="filled", fillcolor=conf["fondo"], fontcolor=conf["fuente"], shape=conf["forma"])
    


    def agregarNodo(self, valor):
        nombre = f"nodo{self.counter}"
        self.dot.node(nombre, valor)
        self.counter += 1
        #retornar el nombre para unir las dos aristas
        return nombre

    def agregarArista(self, nodo1, nodo2):
        self.dot.edge(nodo1, nodo2)

    def generarGrafica(self):
        pass

    def obtenerUltimoNodo(self):
        return f"nodo{self.counter - 1}"
    
arbol = Arbol()