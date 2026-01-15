import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from db import crear_tabla, guardar_en_postgresql
from pdf_utils import extraer_metadatos

def procesar_carpeta():
    carpeta = filedialog.askdirectory(title="Selecciona la carpeta con PDFs")
    if not carpeta:
        return

    categoria = simpledialog.askstring("Categoría", "Ingresa una categoría para estos PDFs:", initialvalue="General")
    if not categoria:
        categoria = "General"

    archivos_pdf = []
    for raiz, _, archivos in os.walk(carpeta):
        for archivo in archivos:
            if archivo.lower().endswith(".pdf"):
                archivos_pdf.append(os.path.join(raiz, archivo))

    if not archivos_pdf:
        messagebox.showinfo("Sin archivos", "No se encontraron archivos PDF.")
        return

    procesados = 0
    for pdf in archivos_pdf:
        meta = extraer_metadatos(pdf, categoria)
        if meta:
            guardar_en_postgresql(meta)
            procesados += 1

    messagebox.showinfo("Proceso finalizado", f"{procesados} archivos procesados correctamente.")

def iniciar_gui():
    crear_tabla()

    ventana = tk.Tk()
    ventana.title("PDF Metadata Extractor")
    ventana.geometry("400x200")

    label = tk.Label(ventana, text="Selecciona una carpeta con archivos PDF", font=("Arial", 12))
    label.pack(pady=20)

    boton = tk.Button(ventana, text="Seleccionar carpeta y procesar", command=procesar_carpeta, bg="#4CAF50", fg="white", padx=10, pady=5)
    boton.pack()

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_gui()
