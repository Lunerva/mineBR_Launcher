# Requisitos
- Python 3.8 o superior
- Acceso a internet

# Instalación
1. Crear y activar entorno virtual
Windows:
    python -m venv venv
    venv\Scripts\activate

macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate

2. Instalar dependencias
    pip install minecraft-launcher-lib

# Uso
Ejecuta el archivo principal desde la terminal:
    python launcher.py

# Notas
- Las versiones se almacenan en un directorio personalizado (.minecraftLauncher) dependiendo del sistema operativo.
- Este launcher no incluye autenticación, solo simula un usuario offline.
- Requiere al menos Java instalado en tu sistema y accesible desde la terminal (Java 8+).