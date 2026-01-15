from pypdf import PdfReader

def extraer_metadatos(ruta_pdf, categoria="General"):
    try:
        reader = PdfReader(ruta_pdf)
        info = reader.metadata
        return {
            "ruta": ruta_pdf,
            "titulo": info.get("/Title"),
            "autor": info.get("/Author"),
            "asunto": info.get("/Subject"),
            "productor": info.get("/Producer"),
            "creador": info.get("/Creator"),
            "numero_paginas": len(reader.pages),
            "categoria": categoria
        }
    except Exception as e:
        print(f"Error leyendo {ruta_pdf}: {e}")
        return None
