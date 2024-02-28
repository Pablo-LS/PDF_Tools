import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog
import fitz


# FUNCIONES
def NombreDoc():
    return input("Escribe el nombre final: ") + ".pdf"

def seleccionar_archivos_pdf():
    archivos_seleccionados = filedialog.askopenfilenames(
        title="Selecciona archivos PDF",
        filetypes=[("Archivos PDF", "*.pdf")],
        initialdir=os.getcwd()
    )

    return archivos_seleccionados

def seleccionar_carpeta():
    carpeta_guardar = filedialog.askdirectory(
        title="Selecciona la carpeta de destino"
    )
    
    os.chdir(carpeta_guardar)
    return carpeta_guardar

def fusionarPdf(archivos_seleccionados, nombreDocumento):
    merger = PyPDF2.PdfMerger()

    for file in archivos_seleccionados:
        if file.endswith(".pdf"):
            merger.append(file)

    merger.write(nombreDocumento)
    print(f"Tus PDFs se han fusionado en {nombreDocumento}")

def comprimirPdf(archivos_seleccionados, nombreDocumento):
    for file in archivos_seleccionados:
        if file.endswith(".pdf"):
            input_pdf = fitz.open(file)
            output_pdf = fitz.open()

            for page_number in range(input_pdf.page_count):
                page = input_pdf[page_number]
                pix = page.get_pixmap()
                img = output_pdf.new_page(width=page.rect.width, height=page.rect.height)
                img.insert_image(page.rect, pixmap=pix)

            output_pdf.save(nombreDocumento)
            input_pdf.close()
            print(f"Tus PDFs se han comprimido en {nombreDocumento}")


# PROGRAMA
bucle = True

print("Bienvenido a PDF Tools")
print()

while bucle == True:
    root = tk.Tk()
    root.withdraw()

    print("1. Fusionar PDFs")
    print("2. Comprimir PDF")
    print()
    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":
        print()
        print("Seleccione sus PDFs y la carpeta destino:")
        ruta_archivos = seleccionar_archivos_pdf()
        seleccionar_carpeta()
        nombreDocumento = NombreDoc()
        if ruta_archivos:
            fusionarPdf (ruta_archivos, nombreDocumento)

    elif opcion == "2":
        print()
        print("Seleccione un PDF y la carpeta destino:")
        ruta_archivos = seleccionar_archivos_pdf()
        seleccionar_carpeta()
        nombreDocumento = NombreDoc()
        if ruta_archivos:
            comprimirPdf(ruta_archivos, nombreDocumento)

    else:
        print("Opción no válida, introduce 1 o 2")

    root.destroy()

    respuesta = input("¿Desea realizar otra operación? (Si/No): ")
    if respuesta.lower() != "si":
        bucle = False
