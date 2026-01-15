# PDF Metadata Extractor

Esta aplicación permite leer metadatos de archivos PDF ubicados en carpetas locales o compartidas en red (SMB) y guardarlos en una base de datos MySQL/PostgreSQL. La aplicación también permite categorizar los PDFs según su tema.

## ⚙️ Requisitos

- Python 3.8+
- MySQL/PostgreSQL Server
- Dependencias de Python (`pip install -r requirements.txt`)
- Montar la carpeta SMB como unidad de red en el sistema operativo

## 🚀 Uso

1. Configura tu conexión en el archivo `.env`.
2. Ejecuta `main.py`.
3. Usa la interfaz gráfica para seleccionar la carpeta y definir la categoría.
4. ¡Listo! Los datos se guardarán en tu base MySQL/PostgreSQL.

## 🛠️ Estructura

- `main.py` - Interfaz gráfica principal.
- `db.py` - Conexión y gestión de base de datos.
- `pdf_utils.py` - Extracción de metadatos.
- `.env` - Configuración segura.
- `requirements.txt` - Dependencias.

## 📱 Futuro

Este proyecto está listo para escalar hacia:

- API REST con FastAPI o Flask
- Aplicación móvil Android (Kivy o usando una API externa)

## 🔒 Seguridad

No subas el archivo `.env` a repositorios públicos.
