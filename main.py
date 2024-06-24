import minecraft_launcher_lib, os, subprocess

user_wind = os.environ["USERNAME"]
minecraft_dir = f"C:/Users/{user_wind}/AppData/Roaming/.minecraftLauncher"


def instalar(version):
    minecraft_launcher_lib.install.install_minecraft_version(version,minecraft_dir)
    print(f"se ha instalado la version {version}")
    
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
    
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version,minecraft_dir,options)
    subprocess.run(minecraft_command)
    
def menu():
    while True:
        print("Bienvenido a mineBr_launcher")
        res = int(input("Para instalar una version (0) \nPara ejecutar minecraft (1) \nDetener launcher (3)\n"))
        
        match res:
            case 0:
                version = input('Cual version? ')
                instalar(version)
            case 1:
                nombre = input('Tu nombre: ')
                version = input('Cual version? ')
                ejecutar(nombre,version)
            case 3:
                break;
            
            
            
menu()