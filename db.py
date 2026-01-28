import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Función para conectar a PostgreSQL
def conectar_postgresql():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),  # Asegúrate de que el puerto es un entero
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME")
    )

# Función para crear la tabla
def crear_tabla():
    conn = conectar_postgresql()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pdf_metadatos (
            id SERIAL PRIMARY KEY,
            ruta TEXT UNIQUE,
            titulo TEXT,
            autor TEXT,
            asunto TEXT,
            productor TEXT,
            creador TEXT,
            numero_paginas INT,
            categoria TEXT,
            tamano_arch TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Función para guardar los metadatos en PostgreSQL
def guardar_en_postgresql(metadatos):
    conn = conectar_postgresql()
    cursor = conn.cursor()
    try:
        # Usamos ON CONFLICT para ignorar duplicados en la columna 'ruta'
        cursor.execute("""
            INSERT INTO pdf_metadatos
            (ruta, titulo, autor, asunto, productor, creador, numero_paginas, categoria, tamano_arch)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (ruta) DO NOTHING
        """, (
            metadatos["ruta"], metadatos["titulo"], metadatos["autor"],
            metadatos["asunto"], metadatos["productor"], metadatos["creador"],
            metadatos["numero_paginas"], metadatos["categoria"], metadatos["tamano_arch"]
        ))
        conn.commit()
    except Exception as e:
        print(f"Error al guardar {metadatos['ruta']}: {e}")
    finally:
        cursor.close()
        conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear la tabla si no existe
    crear_tabla()
    
    # Ejemplo de metadatos
    ejemplo_metadatos = {
        "ruta": "/libros/ejemplo.pdf",
        "titulo": "Ejemplo de Título",
        "autor": "Autor Ejemplo",
        "asunto": "Asunto Ejemplo",
        "productor": "Productor Ejemplo",
        "creador": "Creador Ejemplo",
        "numero_paginas": 120,
        "categoria": "Novela",
        "tamano_arch": "8773772"
    }

    # Guardar los metadatos en la base de datos
    guardar_en_postgresql(ejemplo_metadatos)