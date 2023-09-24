from Expresiones.expresion import *
from Graficas.Arbol import *
import math

class ExpresionTrigonometrica(Expresion):
    def __init__(self, tipo, valor1, line, col):
        self.tipo = tipo
        self.valor1 = valor1
        self.linea = line
        self.columna = col 

    def interpretar(self):
        valor = self.valor1
        nodo = None 

        if isinstance(self.valor1, Expresion):
            valor = round(self.valor1.interpretar(), 2)
            nodo = arbol.obtenerUltimoNodo()
        else:
            nodo = arbol.agregarNodo(str(valor))

        resultado = None


        if self.tipo == "seno":
            resultado = math.sin(self.valor1)
        elif self.tipo == "coseno":
            resultado = math.cos(self.valor1)
        elif self.tipo == "tangente":
            resultado = math.tan(self.valor1)
        elif self.tipo == "inverso":
            resultado = (1 / self.valor1)

        raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(round(resultado,2))}")
        arbol.agregarArista(raiz, nodo)

        return resultado
