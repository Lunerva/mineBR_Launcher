import minecraft_launcher_lib, os, subprocess

user_wind = os.environ["USERNAME"]
minecraft_dir = f"C:/Users/{user_wind}/AppData/Roaming/.minecraftLauncher"

def versiones_instaladas():
    print("Versiones instaladas: ")
    vers_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_dir)
    if len(vers_instaladas) == 0:
        print("No tiene ninguna version instalada")
    else:
        for ver in vers_instaladas:
            print(ver['id'])
    print('\n')
    

def instalar(version):
    
    versiones_instaladas()
    
    minecraft_launcher_lib.install.install_minecraft_version(version,minecraft_dir)
    print(f"se ha instalado la version {version}")
    
def instalar_forge(version):
    versiones_instaladas()
    
    forge = minecraft_launcher_lib.forge.find_forge_version(version)
    minecraft_launcher_lib.forge.install_forge_version(forge,minecraft_dir)
    print('Forge instalado')
    
    
def ejecutar(nombre,vers,ram):
    options = {
        'username' : nombre,
        'uuid' : '',
        'token' : '',
        
        'jvArguments' : [f"-Xmx{ram}G","-Xmx{ram}G"], 
        'launcherVersion' : "0.0.2"
    }
    
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(vers,minecraft_dir,options)
    subprocess.run(minecraft_command)
    
def menu():
    while True:
        print("Bienvenido a mineBr_launcher")
        print("1. Para instalar una version\n2. Para instalar una version forge\n3. Para ejecutar minecraft\n4. Salir\n")
        res = int(input("Selecciona una opcion: "))
        
        match res:
            case 1:
                version = input('Ingresa el numero de version a instalar: ')
                instalar(version)
            case 2:
                version = input('Ingresa el numero de version a instalar (Forge): ')
                instalar_forge(version)
            case 3:
                nombre = input('Ingresa tu nombre de usuario: ')
                versiones_instaladas()
                version = input('Selecciona la version: ')
                ram = input('Ingresa la cantidad de memoria ram (en Gb): ')
                ejecutar(nombre,version,ram)
            case 4:
                break;
            
            
            
            
menu()