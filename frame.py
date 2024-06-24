import minecraft_launcher_lib, os, subprocess
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

user_wind = os.environ["USERNAME"]
minecraft_dir = f"C:/Users/{user_wind}/AppData/Roaming/.minecraftLauncher"

ventana = ctk.CTk()
ventana.geometry('400x400')
ventana.title('MineBr_Launcher')
ventana.resizable(False,False)

bt_ejecutar = ctk.CTkButton(ventana,text='Iniciar',text_color='white', fg_color='#3b82f6')
bt_instalar = ctk.CTkButton(ventana,text='Instalar version',text_color='white', fg_color='#10b981')
bt_instalar_forge = ctk.CTkButton(ventana,text='Instalar version Forge',text_color='white', fg_color='#ef4444')

lb_APP = ctk.CTkLabel(ventana,text='MineBr_Launcher ',text_color='white', font=('Arial',48))
lb_nombre = ctk.CTkLabel(ventana,text='Ingresa tu nombre: ',text_color='white', font=('Arial',12))
lb_ver = ctk.CTkLabel(ventana,text='Selecciona la version: ',text_color='white', font=('Arial',12))
lb_ram = ctk.CTkLabel(ventana,text='RAM a usar (en GB): ',text_color='white', font=('Arial',12))

entry_nombre = ctk.CTkEntry(ventana, placeholder_text='nombre...')
entry_ram = ctk.CTkEntry(ventana, placeholder_text='ram...')


vers_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_dir)
lista = [version['id'] for version in vers_instaladas]
    
if len(lista) != 0:
    res = ctk.StringVar(value=lista[0])
else:
    res = ctk.StringVar(value="No tiene ninguna version instalada")
    lista.append('sin versiones instaladas')

versiones_optMenu = ctk.CTkOptionMenu(ventana,variable=res, values=lista)
versiones_optMenu.configure()


def instalar():
    version = entry_versiones.get()
    if version:
        minecraft_launcher_lib.install.install_minecraft_version(version,minecraft_dir)
        print(f"se ha instalado la version {version}")
        messagebox.showinfo("Exito", f'Se ha instalado la version {version}')
    else:
        messagebox.showerror('Error','Intentelo de nuevo')
    
def instalar_forge():
    version = entry_versiones.get()
    forge = minecraft_launcher_lib.forge.find_forge_version(version)
    if forge:
        minecraft_launcher_lib.forge.install_forge_version(forge,minecraft_dir)
        print('Forge instalado')
        messagebox.showinfo("Exito", 'Forge instalado')
    else:
        messagebox.showerror('Error','Intentelo de nuevo')
    
    
def ejecutar():
    nombre = entry_nombre.get()
    vers = versiones_optMenu._current_value
    ram = entry_ram.get()
    if not nombre:
        messagebox.showerror("Error","Introduce tu nombre!")
        print("Introduce tu nombre!")
        return
    if not ram:
        messagebox.showerror("Error","Introduce la cantidad de memoria ram!")
        print("Introduce la cantidad de memoria ram!")
        return
    
    options = {
        'username' : nombre,
        'uuid' : '',
        'token' : '',
        
        'jvArguments' : [f"-Xmx{ram}G","-Xmx{ram}G"], 
        'launcherVersion' : "0.0.2"
    }
    ventana.destroy()
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(vers,minecraft_dir,options)
    subprocess.run(minecraft_command)
    

def instalar_version_normal():
    ventana_vers = ctk.CTkToplevel(ventana)
    ventana_vers.geometry('300x150')
    ventana_vers.title('Instalar version')
    ventana_vers.grab_set()
    
    global entry_versiones
    entry_versiones = ctk.CTkEntry(ventana_vers,placeholder_text="Introduce la version")
    entry_versiones.place(x=80,y=20)
    
    bt_instalar_vers = ctk.CTkButton(ventana_vers, command=instalar, text='instalar')
    bt_instalar_vers.place(x=80,y=60)

def instalar_version_forge():
    ventana_vers = ctk.CTkToplevel(ventana)
    ventana_vers.geometry('300x150')
    ventana_vers.title('Instalar version forge')
    ventana_vers.grab_set()
    
    global entry_versiones
    entry_versiones = ctk.CTkEntry(ventana_vers,placeholder_text="Introduce la version")
    entry_versiones.place(x=80,y=20)
    
    bt_instalar_vers = ctk.CTkButton(ventana_vers, command=instalar_forge, text='instalar')
    bt_instalar_vers.place(x=80,y=60)
    

def menu():
    lb_APP.place(x=10,y=20)
    
    lb_nombre.place(x=20,y=120)
    entry_nombre.place(x=150,y=120)

    lb_ver.place(x=20, y=160)
    versiones_optMenu.place(x=150,y=160)
    
    lb_ram.place(x=20,y=200)
    entry_ram.place(x=150,y=200)

    bt_ejecutar.configure(command=ejecutar)
    bt_ejecutar.place(x=133,y=250)
    
    bt_instalar.configure(command=instalar_version_normal)
    bt_instalar.place(x=133,y=300)
    
    bt_instalar_forge.configure(command=instalar_version_forge)
    bt_instalar_forge.place(x=133,y=350)
    
    
    
    ventana.mainloop()

menu()


