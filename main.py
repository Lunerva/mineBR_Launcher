import minecraft_launcher_lib, os, subprocess

#user_wind = os.environ["USERNAME"]
user_mac = os.environ["USER"]

user_wind = user_mac
try:
    minecraft_dir = f"C:/Users/{user_wind}/AppData/Roaming/.minecraftLauncher"
except:
    print("windows no detectado")

try:
    minecraft_dir = f"/Users/{user_mac}/Library/Application Support/.minecraftLauncher"
except:
    print("macOS no detectado")


if not os.path.exists(minecraft_dir):
    os.makedirs(minecraft_dir,exist_ok=True)

###################### MOSTRAR AVANCE DE DESCARGA
current_max =0

def set_status(status: str):
    print(status)

def set_progress(progress:int):
    if current_max != 0:
        print(f"{progress}/{current_max}")

def set_max(new_max:int):
    global current_max
    current_max = new_max

callback = {
    "setStatus":set_status,
    "setProgress": set_progress,
    "setMax":set_max
}
###############
############### INSTALAR VERSION
def instalar(version):
    try:
        minecraft_launcher_lib.install.install_minecraft_version(version,minecraft_dir,callback=callback)
        print(f"se ha instalado la version {version}")
    except:
        print("ha ocurrido un error inesperado")
    
def ejecutar(nombre,vers):
    
    vers_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_dir)
    if len(vers_instaladas) == 0:
        print("No tiene ninguna version instalada")
    else:
        for ver in vers_instaladas:
            print(ver['id'])
    
    
    mine_user = nombre
    version = vers
    
    options = {
        'username' : mine_user,
        'uuid' : '',
        'token' : '',
        
        'jvArguments' : ["-Xmx4G","-Xmx4G"], 
        'launcherVersion' : "0.0.2"
    }
    try:
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version,minecraft_dir,options)
        subprocess.run(minecraft_command)
    except:
        print("ha ocurrido un error inesperado")
    
def menu():
    while True:
        print("                                           |||||//////     ||||||||")
        print("                                           |||||   ///     |||    ///")
        print("|||            |||  |||          ///////   |||||////       |||/////")
        print("|||//|||//|||       |||/////   ||_____||   |||||//////     |||/////")
        print("|||  |||  |||  |||  |||   ///  ||          |||||   ///     |||   ///")
        print("|||  |||  |||  |||  |||   ///    /////     |||||////       |||    ///")
        print("\nBienvenido a mineBr_launcher")
        res = int(input("Para instalar una version (0) \nPara ejecutar minecraft (1) \nDetener launcher (3)\n"))
        
        match res:
            case 0:
                print('_______________________________')
                version = input('Cual version? ')
                instalar(version)
                print('_______________________________')
            case 1:
                print('_______________________________')
                nombre = input('Tu nombre: ')
                
                print("versiones instaladas: ")
                vers_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_dir)
                
                if len(vers_instaladas) == 0:
                    print("No tiene ninguna version instalada")
                else:
                    for ver in vers_instaladas:
                        print(ver['id'])
                try:
                    version = input('Cual version? ')
                    ejecutar(nombre,version)
                except:
                    print("ingrese el numero de la version")
                print('_______________________________')
            case 3:
                break;
            
            
            
menu()