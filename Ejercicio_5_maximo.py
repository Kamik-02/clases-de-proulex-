
from tkinter import END, messagebox, ttk
import tkinter as tk

ventana =tk.Tk()
ventana.config(width=350, height=320)
ventana.title ("Ejercicio5")

ttk.Label(ventana, text="Valor 1").place(x=20,y=30)
ttk.Label(ventana, text="Valor 2").place(x=20,y=100)
ttk.Label(ventana, text="Valor 3").place(x=20,y=170)

txValor1 = tk.Entry(ventana,width=10)
txValor1.place(x=20, y=50)

txValor2 = tk.Entry(ventana, width=10)
txValor2.place(x=20,y=120)

txValor3 = tk.Entry(ventana,width=10,)
txValor3.place(x=20,y=190)

def obtener_valores():
    try:
        v1 = int(txValor1.get())
        v2 = int(txValor2.get())
        v3 = int(txValor3.get())
        return [v1, v2, v3]
    except ValueError:
        messagebox.showerror("Error", "Ingresa números enteros válidos")
        return None

def mostrar_maximo():
    valores = obtener_valores()
    if valores:
        messagebox.showinfo("Máximo", f"El valor máximo es: {max(valores)}")

def mostrar_minimo():
    valores = obtener_valores()
    if valores:
        messagebox.showinfo("Mínimo", f"El valor mínimo es: {min(valores)}")

def mostrar_Nmedio():
    valores = obtener_valores()
    if valores:
        mediana = sorted(valores)[1]  # El número del medio
        messagebox.showinfo("Número del medio", f"El número de enmedio es: {mediana}")












btMaximo= tk.Button(ventana, text="Maximo",width=10, command=mostrar_maximo)
btMaximo.place(x=20, y=250)

btMinimo= tk.Button(ventana, text="Minimo",width=10,command=mostrar_minimo)
btMinimo.place(x=120, y=250)


btMedia= tk.Button(ventana, text="Nmedio",width=10,command=mostrar_Nmedio)
btMedia.place(x=220,y=250)





























ventana.mainloop()