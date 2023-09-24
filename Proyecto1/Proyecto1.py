import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox 
from Analizador import analizar as analizar_json  # Renombramos la función local
from Analizador import errores
from Analizador import handle_error
from Analizador import reset_errors, get_error_count

# Funciones para los comandos del menú
def analizar():
    print("Comando 'Analizar'")

def ver_errores():
    print("Comando 'Errores'")

def ver_reporte():
    print("Comando 'Reporte'")

# Ventana principal
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto 1")
        self.geometry("800x500")
        self.configure(bg="blue4")
        
        # Espacio en blanco en la parte superior
        self.espacio_superior = Label(self, text="", height=1, bg="blue4")
        self.espacio_superior.pack()

        # Tamaño del cuadro de texto
        self.text = Text(
            self,
            width=80,
            height=24,
            font=("comicsans", 13)
        )
        self.text.pack()

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.filemenu)
        self.filemenu.add_command(label="Abrir", command=self.open_file)
        self.filemenu.add_command(label="Guardar", command=self.save_filesg)
        self.filemenu.add_command(label="Guardar Como", command=self.save_files)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Salir", command=self.quit)
        
        # Agregar comandos al menú principal
        self.menu.add_command(label="Analizar", command=self.analizar_texto)
        self.menu.add_command(label="Comprobar Errores", command=self.ver_errores)
        self.menu.add_command(label="Reporte", command=self.generar_reporte)
        
    #Abrir archivo
    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.text.delete(1.0, tk.END)
        with open(filepath, "r" ) as input_file:
            text = input_file.read()
            self.text.insert(tk.END, text)
        self.title(f"Proyecto 1 - {filepath}")

    #Guardar Archivo
    def save_filesg(self):
        current_title = self.title()
        current_file_path = current_title.split(" - ")[-1]
        if current_file_path:
            with open(current_file_path, "w") as output_file:
                text = self.text.get(1.0, tk.END)
                output_file.write(text)

    #Guardar Archivo pero permite cambiar el nombre
    def save_files(self):
        filepath = asksaveasfilename(
            defaultextension="json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open (filepath, "w") as output_file:
            text =  self.text.get(1.0, tk.END)
            output_file.write(text)
        self.title(f"Proyecto 1 - {filepath}")

    def analizar_texto(self):
        text = self.text.get(1.0, tk.END)
        if not text.strip():  # Verificar si el texto está vacío o solo contiene espacios en blanco
            messagebox.showwarning("Texto vacío", "No hay texto para analizar.")
            return  # Salir de la función si no hay texto

        print("analizando...")
        # Reiniciar errores antes de realizar una nueva comprobación
        reset_errors()
        arbol = analizar_json(text)
        print("Análisis completado.")
        # Luego, aquí puedes generar la gráfica o reporte con la información de 'arbol'

    def generar_reporte(self):
        text = self.text.get(1.0, tk.END)
        arbol = analizar_json(text)
        arbol.dot.view()
        # Utilizando la información de 'arbol' o de donde sea que provenga.
        print("Generando reporte...")

    def ver_errores(self):
        text = app.text.get(1.0, tk.END)
        if not text.strip():
            messagebox.showinfo("Resultado de Comprobación", "No hay errores.")
            return

        # Reiniciar errores antes de realizar una nueva comprobación
        reset_errors()

        # Ejecutar la comprobación de errores
        analizar_json(text)

        # Verificar si no hay errores antes de mostrar el mensaje "No hay errores"
        if get_error_count() == 0:
            messagebox.showinfo("Resultado de Comprobación", "No hay errores.")
        else:
            # Mostrar ventana emergente de errores al final del análisis, si hay errores
            handle_error("", show_message=True)



app = VentanaPrincipal()
app.mainloop()
