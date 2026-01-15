import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar_mysql():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def crear_tabla():
    conn = conectar_mysql()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pdf_metadatos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ruta TEXT UNIQUE,
            titulo TEXT,
            autor TEXT,
            asunto TEXT,
            productor TEXT,
            creador TEXT,
            numero_paginas INT,
            categoria TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_en_mysql(metadatos):
    conn = conectar_mysql()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT IGNORE INTO pdf_metadatos
            (ruta, titulo, autor, asunto, productor, creador, numero_paginas, categoria)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            metadatos["ruta"], metadatos["titulo"], metadatos["autor"],
            metadatos["asunto"], metadatos["productor"], metadatos["creador"],
            metadatos["numero_paginas"], metadatos["categoria"]
        ))
        conn.commit()
    except Exception as e:
        print(f"Error al guardar {metadatos['ruta']}: {e}")
    finally:
        conn.close()
