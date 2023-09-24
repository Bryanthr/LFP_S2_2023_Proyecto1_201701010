from Expresiones.expresion import *
from Graficas.Arbol import *
import math 


class ExpresionAritmetica(Expresion):
    def __init__(self, tipo, valor1, valor2, line, col):
        self.tipo = tipo 
        self.valor1 = valor1
        self.valor2 = valor2
        self.linea = line
        self.columna = col

    def interpretar(self):
        valor1 = self.valor1
        valor2 = self.valor2 

        if isinstance(valor1, Expresion):
            valor1 = valor1.interpretar()
            nodo1 = arbol.obtenerUltimoNodo()
            print("Resultado momentaneo", valor1)
        else:
            nodo1 = arbol.agregarNodo(str(valor1))


        if isinstance(valor2, Expresion):
            valor2 = valor2.interpretar()
            nodo2 = arbol.obtenerUltimoNodo()
            print("Resultado momentaneo", valor2)
        else:
            valor2 = self.valor2
            nodo2 = arbol.agregarNodo(str(valor2))



        resultado = None

        if self.tipo == "suma":
            resultado = valor1 + valor2
        elif self.tipo == "resta":
            resultado = valor1 - valor2
        elif self.tipo == "multiplicacion":
            resultado = valor1 * valor2
        elif self.tipo == "division":
            resultado = valor1 / valor2
        elif self.tipo == "mod":
            resultado = valor1 % valor2
        elif self.tipo == "potencia":
            resultado = math.pow(valor1, valor2)
        elif self.tipo == "raiz":
            resultado =  math.pow(valor1, 1/ valor2)

        raiz = arbol.agregarNodo(f"{self.tipo}\\n{resultado}")

        arbol.agregarArista(raiz, nodo1)
        arbol.agregarArista(raiz, nodo2)

        return resultado 