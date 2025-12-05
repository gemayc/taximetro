import tkinter as tk               # Librería estándar de Python para crear interfaces gráficas
from tkinter import messagebox     # Para mostrar mensajes tipo popup
from pricing import load_prices    # Cargar tarifas desde el json
from oop_taximeter import Taximeter  # Importamos la clase

# Creamos la ventana principal
root = tk.Tk()
#si se ponen los titulos
root.title("🚕 Taxímetro - GUI")
# tamaño inicial de la ventana
root.geometry("400x400")


# CARGAMOS LOS PRECIOS
prices = load_prices() #cargamos los precios con mi funcion de princing.py
taximeter = Taximeter(prices) # cargamos mi funcion de taximetro y le metemos los precios

#  ETIQUETAS (LABELS) - SE CREAN ANTES DE LAS FUNCIONES
title = tk.Label(root, text="🚕 TAXÍMETRO", font=("Arial", 16, "bold"))
title.pack(pady=10)

label_state = tk.Label(root, text="Estado: SIN VIAJE", font=("Arial", 12))
label_state.pack(pady=5)

label_info = tk.Label(root, text="", font=("Arial", 10))
label_info.pack(pady=5)


# FUNCIONES QUE VAN A LOS BOTONES
def start_trip():
    try:
        taximeter.start_trip()
        label_state.config(text="Estado: STOPPED")
        label_info.config(text="Viaje iniciado")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        
def stop_trip():
    """Cambia el estado a parado."""
    try:
        taximeter.change_state("stopped")
        label_state.config(text="Estado: STOPPED")
        label_info.config(text="Taxi Parado")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        
def move_trip():
    """Cambia el estado a parado."""
    try:
        taximeter.change_state("moving")
        label_state.config(text= "Estado: MOVING")
        label_info.config(text= "Taxi en Movimiento")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        
def finish_trip():
    """Termina el viaje y muestra un resumen."""
    try:
        summary= taximeter.finish_trip()
        
        stopped = summary["stopped_time"]
        moving = summary["moving_time"]
        total = summary["total_fare"]
        
    
    
            
        
