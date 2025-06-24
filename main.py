import minecraft_launcher_lib, os, subprocess, platform, datetime

# Detección del sistema operativo
system = platform.system()
user = os.environ.get('USER') or os.environ.get('USERNAME')

# Configurar directorio según SO
if system == "Windows":
    minecraft_dir = f"C:/Users/{user}/AppData/Roaming/.minecraftLauncher"
elif system == "Darwin":
    minecraft_dir = f"/Users/{user}/Library/Application Support/.minecraftLauncher"
elif system == "Linux":
    minecraft_dir = f"/home/{user}/.minecraftLauncher"
else:
    print("Sistema operativo no compatible")
    exit(1)

# Crear directorio si no existe
os.makedirs(minecraft_dir, exist_ok=True)

# Variables globales para el progreso
current_max = 0
last_status = ""

###################### MOSTRAR AVANCE DE DESCARGA
def set_status(status: str):
    global last_status
    last_status = status
    print(status)

def set_progress(progress: int):
    if current_max != 0:
        percent = int((progress / current_max) * 100)
        print(f"\rProgreso: {percent}% | {progress}/{current_max}", end='')

def set_max(new_max: int):
    global current_max
    current_max = new_max

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}
###############
############### INSTALAR VERSION
def instalar(version):
    try:
        print(f"\nInstalando {version}...")
        minecraft_launcher_lib.install.install_minecraft_version(
            version, 
            minecraft_dir,
            callback=callback
        )
        print(f"\n✅ Se ha instalado la versión {version}")
    except Exception as e:
        print(f"\n❌ Error durante la instalación: {str(e)}")

def listar_versiones_disponibles():
    try:
        versiones = minecraft_launcher_lib.utils.get_version_list()
        releases = [v for v in versiones if v["type"] == "release"]
        idreleases = [v["id"] for v in releases]     
        print(f"{idreleases}")
        return idreleases
    except Exception as e:
        print(f"Error al obtener versiones: {e}")
        return []

def ejecutar(nombre, version):
    try:
        options = {
            'username': nombre,
            'uuid': '',
            'token': '',
            'jvArguments': ["-Xmx4G", "-Xms2G"],
            'launcherVersion': "0.0.2"
        }
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
            version, 
            minecraft_dir, 
            options
        )
        print(f"\nIniciando Minecraft {version}...")
        subprocess.run(minecraft_command)
    except Exception as e:
        print(f"❌ Error al iniciar: {str(e)}")

def mostrar_versiones_instaladas():
    vers_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_dir)
    if not vers_instaladas:
        print("No tienes versiones instaladas")
        return []
    
    print("\nVersiones instaladas:")
    for i, ver in enumerate(vers_instaladas, 1):
        print(f"{i}. {ver['id']}")
    
    return [v['id'] for v in vers_instaladas]

def borrar_version():
    instaladas = mostrar_versiones_instaladas()
    if not instaladas:
        return
    
    try:
        opcion = input("\nIngresa el número de la versión a borrar (0 para cancelar): ")
        if opcion == "0":
            return
        
        index = int(opcion) - 1
        if 0 <= index < len(instaladas):
            version = instaladas[index]
            confirmar = input(f"¿Estás seguro de borrar {version}? (s/n): ").lower()
            
            if confirmar == "s":
                print(f"Borrando {version}...")
                minecraft_launcher_lib.install.uninstall_minecraft_version(version, minecraft_dir)
                print(f"✅ Versión {version} borrada exitosamente")
            else:
                print("Operación cancelada")
        else:
            print("❌ Número de versión inválido")
    except ValueError:
        print("❌ Ingresa un número válido")
    except Exception as e:
        print(f"❌ Error al borrar: {str(e)}")

def menu():
    while True:
        print("\n" + "="*50)
        print("MINECRAFT LAUNCHER".center(50))
        print("="*50)
        print("1. Instalar una versión")
        print("2. Ejecutar Minecraft")
        print("3. Borrar versión")
        print("4. Salir")
        print("="*50)
        
        try:
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                print("\n" + "-"*50)
                disponibles = listar_versiones_disponibles()
                if disponibles:
                    version = input("\nEscribe el número de la versión: ")
                    instalar(version)
            
            elif opcion == "2":
                print("\n" + "-"*50)
                nombre = input("Tu nombre de usuario: ")
                instaladas = mostrar_versiones_instaladas()
                
                if instaladas:
                    version = input("\nEscribe la versión a ejecutar: ")
                    if version in instaladas:
                        ejecutar(nombre, version)
                    else:
                        print(f"❌ La versión {version} no está instalada")
            
            elif opcion == "3":
                print("\n" + "-"*50)
                borrar_version()
            
            
            elif opcion == "4":
                print("¡Hasta pronto!")
                break
            
            else:
                print("Opción inválida. Intenta de nuevo.")
                
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    menu()