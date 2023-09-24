from collections import namedtuple
from Expresiones.aritmeticas import ExpresionAritmetica
from Expresiones.trigonometricas import ExpresionTrigonometrica
from Graficas.Arbol import *
from tkinter import messagebox


Token = namedtuple("Token", ["value", "line", "col"])

line = 1
col = 1

error_messages = ""

global errores
errores = 0

tokens = []

configuracion = {
    "texto": None,
    "fondo":None,
    "fuente":None,
    "forma":None
}

def string_To_Token(input_str, i):
    token = ""
    for char in input_str:
        if char == '"':
            return [token, i]
        token += char
        i += 1

def number_To_Token(input_str, i):
    token = ""
    is_decimal = False
    for char in input_str:
        if char.isdigit():
            token += char
            i += 1
        elif char == ".":
            token += char
            i += 1
            is_decimal = True
        else:
            break
    if is_decimal:
        return [float(token), i]
    return [int(token), i]

def token_input(input_str):
    global line, col, tokens, errores

    errores = 0 
    

    i = 0
    while i < len(input_str):
        char = input_str[i]

        if char.isspace():
            if char == "\n":
                line += 1
                col = 1
            elif char == "\t":
                col += 4
            i += 1

        elif char == '"':
            string, pos = string_To_Token(input_str[i + 1:], i)
            col += len(string) + 2
            i = pos + 2
            token = Token(string, line, col)
            tokens.append(token)

        elif char in ["{", "}", "[", "]", ",", ":"]:
            col += 1
            i += 1
            token = Token(char, line, col)
            tokens.append(token)

        elif char.isdigit():
            number, pos = number_To_Token(input_str[i:], i)
            col += pos - i
            i = pos
            token = Token(number, line, col)
            tokens.append(token)
        else:
            handle_error(char)
            i += 1
            col += 1

#entrada = open(r"C:\Users\Bryant Herrera\Documents\Lenguajes formales\EjemploEntrada.json", "r").read()
#token_input(entrada)

#Esta parte es complicada IMPORTANTE
#
def get_instruction():
    global tokens
    operacion = None
    value1 = None
    value2 = None
    while tokens:
        token = tokens.pop(0)
        if token.value == "operacion":
            tokens.pop(0)
            operacion = tokens.pop(0).value

        elif token.value == "valor1":
            #eliminar el ":"
            tokens.pop(0)
            value1 = tokens.pop(0).value
            if value1 == "[":
                value1 = get_instruction()

        elif token.value == "valor2":
            #eliminar el ":"
            tokens.pop(0)
            value2 = tokens.pop(0).value
            if value2 == "[":
                value2 = get_instruction()
        
        #configuraciones
        elif token.value in ["texto", "fondo", "fuente", "forma"]:
            tokens.pop(0)
            configuracion[token.value] = tokens.pop(0).value

        #Si hay errores
        else:
            pass

        if operacion and value1 and value2:
            return ExpresionAritmetica(operacion, value1, value2, 0, 0)
        elif operacion and operacion in ["seno","coseno","tangente","inverso"] and value1:
            return ExpresionTrigonometrica(operacion, value1, 0, 0)
    return None


#crear las instrucciones para cuando encuentre una función
def create_instructions():
    global tokens
    instrucciones = []
    while tokens:
        instruccion = get_instruction()
        if instruccion:
            instrucciones.append(instruccion)
    return instrucciones


def analizar(entrada):
    global line, col, tokens, errores

    # Restablecer variables al inicio de cada análisis
    line = 1
    col = 1
    errores = 0 
    token_input(entrada)
    #limpiar arbol
    arbol.dot.clear()
    arbol.agregarConfiguracion(configuracion)
    instrucciones = create_instructions()
    for i in instrucciones:
        print("Resultado FINAL de la instruccion: ",  i.interpretar())

    error_count = get_error_count()
    print("Número total de errores encontrados: ", error_count)

    return arbol

def handle_error(char, show_message=True):
    global errores, error_messages
    if char:
        errores += 1
        mensaje_error = (
            f"Error: caracter desconocido: {char} "
            f"En fila: {line} columna: {col}\n"
        )
        # Verificar si el mensaje de error ya está en error_messages antes de agregarlo
        if mensaje_error not in error_messages:
            error_messages += mensaje_error

    # Mostrar mensaje de error en una ventana emergente al final del análisis
    if show_message and not tokens and error_messages:
        messagebox.showerror("Resultado de Comprobación", "Se encontraron errores:\n" + error_messages)

def get_error_count():
    global errores
    return errores

def get_errores():
    global errores
    return errores

def reset_errors():
    global errores, error_messages
    errores = 0
    error_messages = ""

#print("INSTRUCCIONES: ", instrucciones)
#print("Configuraciones: ", configuracion)

#print("\n"*3)
#print(arbol.dot.source)