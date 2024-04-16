import shutil
import os
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading

class FileMoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Mover App FISERV")
        self.master.resizable(False, False)  # Desactivar la posibilidad de cambiar el tamaño de la ventana
        
        self.directorio_origen = tk.StringVar(value="")
        self.directorio_destino = tk.StringVar(value="")
        self.tiempo_espera = tk.StringVar(value="60")
        self.unidad_tiempo = tk.StringVar(value="segundos")
        
        # Crear el fondo
        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()
        self.load_background("C:/todo/Script_python/logo_fiserv.png")  # Reemplaza con la ruta de tu imagen
        
        # Crear los widgets
        tk.Label(master, text="Directorio de origen:").place(x=20, y=50)
        self.entry_origen = tk.Entry(master, textvariable=self.directorio_origen, width=50)
        self.entry_origen.place(x=180, y=50)
        tk.Button(master, text="Seleccionar", command=self.select_origen).place(x=500, y=45)
        
        tk.Label(master, text="Directorio de destino:").place(x=20, y=80)
        self.entry_destino = tk.Entry(master, textvariable=self.directorio_destino, width=50)
        self.entry_destino.place(x=180, y=80)
        tk.Button(master, text="Seleccionar", command=self.select_destino).place(x=500, y=75)
        
        tk.Label(master, text="Tiempo de espera:").place(x=20, y=110)
        self.entry_tiempo = tk.Entry(master, textvariable=self.tiempo_espera, width=10)
        self.entry_tiempo.place(x=180, y=110)
        
        # Unidad de tiempo
        self.unit_label = tk.Label(master, text="Unidad de tiempo:")
        self.unit_label.place(x=250, y=110)
        self.unit_combobox = ttk.Combobox(master, textvariable=self.unidad_tiempo, values=["segundos", "minutos", "horas"])
        self.unit_combobox.place(x=350, y=110)
        self.unit_combobox.bind("<<ComboboxSelected>>", self.on_unit_selected)
        
        self.start_button = tk.Button(master, text="Iniciar", command=self.start)
        self.start_button.place(x=20, y=150)
        
        self.lock_button = tk.Button(master, text="Bloquear rutas", command=self.lock_paths)
        self.lock_button.place(x=120, y=150)
        
        self.reset_button = tk.Button(master, text="Limpiar rutas", command=self.reset_paths)
        self.reset_button.place(x=240, y=150)
        
        # Inicializar las variables de estado
        self.running = False
        self.paths_locked = False
        
    def select_origen(self):
        if not self.paths_locked:
            directorio_origen = filedialog.askdirectory()
            if directorio_origen:
                self.directorio_origen.set(directorio_origen)
    
    def select_destino(self):
        if not self.paths_locked:
            directorio_destino = filedialog.askdirectory()
            if directorio_destino:
                self.directorio_destino.set(directorio_destino)
    
    def start(self):
        if self.directorio_origen.get() and self.directorio_destino.get():
            self.running = True
            self.start_button.config(state="disabled")
            self.lock_button.config(state="disabled")
            self.reset_button.config(state="normal")
            self.move_files_threaded()
        else:
            tk.messagebox.showwarning("Advertencia", "Por favor, seleccione los directorios de origen y destino.")
    
    def lock_paths(self):
        self.paths_locked = True
        self.entry_origen.config(state="readonly")
        self.entry_destino.config(state="readonly")
        self.lock_button.config(text="Rutas bloqueadas")
    
    def reset_paths(self):
        self.directorio_origen.set("")
        self.directorio_destino.set("")
        self.paths_locked = False
        self.entry_origen.config(state="normal")
        self.entry_destino.config(state="normal")
        self.lock_button.config(text="Bloquear rutas")
        self.start_button.config(state="normal")
        self.lock_button.config(state="normal")
        self.reset_button.config(state="disabled")
    
    def move_files_threaded(self):
        thread = threading.Thread(target=self.move_files)
        thread.start()
    
    def move_files(self):
        while self.running:
            archivos = os.listdir(self.directorio_origen.get())
            for archivo in archivos:
                ruta_archivo_origen = os.path.join(self.directorio_origen.get(), archivo)
                if archivo.endswith(".txt") and os.path.isfile(ruta_archivo_origen):
                    try:
                        shutil.copy2(ruta_archivo_origen, self.directorio_destino.get())
                        print(f"El archivo '{archivo}' se ha copiado correctamente.")
                    except Exception as e:
                        print(f"Error al copiar el archivo '{archivo}': {str(e)}")
            tiempo_espera = int(self.tiempo_espera.get())
            if self.unidad_tiempo.get() == "minutos":
                tiempo_espera *= 60
            elif self.unidad_tiempo.get() == "horas":
                tiempo_espera *= 3600
            time.sleep(tiempo_espera)
            self.master.update()  # Actualizar la interfaz para que sea sensible a los eventos de la GUI
    
    def on_unit_selected(self, event):
        # Deshabilitar la selección de la unidad de tiempo después de que el usuario la haya seleccionado
        self.unit_combobox.config(state="disabled")
    
    def load_background(self, image_path):
        if os.path.isfile(image_path):
            self.background_image = tk.PhotoImage(file=image_path)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        else:
            self.master.config(bg="white")

def main():
    root = tk.Tk()
    root.geometry("600x400")  # Tamaño de la ventana
    app = FileMoverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
