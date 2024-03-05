from tkinter import ttk
import tkinter as tk
import os
from tkinter.messagebox import showerror, showinfo, showwarning
import sys
import wget
from bs4 import BeautifulSoup
from colorama import init, Fore, Back
import getpass
import webbrowser as web
import requests
import json
import zipfile
from time import *
import PIL.Image
import shutil
from pypresence import Presence
import time

init(autoreset=True)

print(Fore.BLUE + r"""
  __  __       _ _   _ __  __           _ 
 |  \/  |_   _| | |_(_)  \/  | ___   __| |
 | |\/| | | | | | __| | |\/| |/ _ \ / _` |
 | |  | | |_| | | |_| | |  | | (_) | (_| |
 |_|  |_|\__,_|_|\__|_|_|  |_|\___/ \__,_|
                                                                                                             
""")



window = tk.Tk()
loading_window = tk.Tk()
path = os.getcwd()
version = 1.0

actual_game = ""

print(Fore.BLACK + Back.WHITE + " OS " + Fore.RESET + Back.RED + f" {os.name} " + Back.RESET + "  " + Fore.BLACK + Back.WHITE + " Version " + Fore.RESET + Back.GREEN + f" {version} " + Back.RESET + "\n")

def download_latest_firmware():
    if os.path.exists(yuzupath+"/nand/system/Contents/registered"):
        showinfo("Information", "Téléchargement du dernier firmware. Cette opération peut prendre jusqu'à 3 minutes.")
        with requests.get("https://api.github.com/repos/THZoria/NX_Firmware/releases") as r:
            releases = json.loads(r.text)
            r.close()
        for file in os.listdir(yuzupath+"/nand/system/Contents/registered"):
            os.remove(yuzupath+f"/nand/system/Contents/registered/{file}")
        wget.download(releases[0]["assets"][0]["browser_download_url"], yuzupath+"/nand/system/Contents/registered/firmware.zip")
        with zipfile.ZipFile(yuzupath+"/nand/system/Contents/registered/firmware.zip", 'r') as zip_ref:
            zip_ref.extractall(yuzupath+"/nand/system/Contents/registered/")
        os.remove(yuzupath+"/nand/system/Contents/registered/firmware.zip")
        showinfo("Information", "Le dernier firmware a bien été installé")
    else:
        showerror("Erreur", "Vous ne possédez pas le dossier nécessaire.")

def select_game(id: str = None):
    global pochette, actual_game
    game_name.config(text=f"\nNom du jeu : {games_db_yuzu_format[id]['name']}\nEditeur : {games_db_yuzu_format[id]['publisher']}\nIdentifiant : {id}\nTaille du jeu : {round(int(games_db_yuzu_format[id]['size'])*(1/1000000000), ndigits=2)} Go\nNombre de cheats : {len(games_db_yuzu_format[id]['cheats'].keys())}\nNombre de mods : {len(games_db_yuzu_format[id]['mods'].keys())}")
    game_name1.config(text=f"\nNom du jeu : {games_db_yuzu_format[id]['name']}\nEditeur : {games_db_yuzu_format[id]['publisher']}\nIdentifiant : {id}\nTaille du jeu : {round(int(games_db_yuzu_format[id]['size'])*(1/1000000000), ndigits=2)} Go\nNombre de cheats : {len(games_db_yuzu_format[id]['cheats'].keys())}\nNombre de mods : {len(games_db_yuzu_format[id]['mods'].keys())}")

    del pochette

    pochette = tk.PhotoImage(file=path+"/cache/Icons/"+id+".png", master=games_infos_frame)
    game_logo.config(image=pochette)
    game_logo1.config(image=pochette)

    cheats_list_viewer.delete(*cheats_list_viewer.get_children())
    mods_list_viewer.delete(*mods_list_viewer.get_children())

    if not os.path.exists(f"{yuzupath}/load/{id}/cheats"):
        os.mkdir(f"{yuzupath}/load/{id}/cheats")

    if not os.path.exists(f"{yuzupath}/load/{id}/cheats/cheats.txt"):
        with open(f"{yuzupath}/load/{id}/cheats/cheats.txt", "w") as f:
            f.write("")
            f.close()

    if len(list(games_db_yuzu_format[id]["cheats"].keys())) == 0:
        showwarning("Information", "Aucun cheat trouvé pour ce jeu.")
    else:
            for cheat in list(games_db_yuzu_format[id]["cheats"].keys()):
                with open(f"{yuzupath}/load/{id}/cheats/cheats.txt", "r") as f:
                    if cheat in f.read():
                        cheats_list_viewer.insert(parent='', text='', index="end", values=(cheat, games_db_yuzu_format[id]["cheats"][cheat], "✅"))
                    else:
                        cheats_list_viewer.insert(parent='', text='', index="end", values=(cheat, games_db_yuzu_format[id]["cheats"][cheat], "❌"))
                    f.close()

    if len(list(games_db_yuzu_format[id]["mods"].keys())) == 0:
        showwarning("Information", "Aucun mod trouvé pour ce jeu.")
    else:
        for mod in games_db_yuzu_format[id]["mods"].keys():
            if mod.replace(".rar", "").replace(".zip", "") in os.listdir(f"{yuzupath}/load/{id}/"):
                mods_list_viewer.insert(parent='', text='', index="end", values=(mod.replace(".rar", "").replace(".zip", ""), games_db_yuzu_format[id]["mods"][mod]["host"], games_db_yuzu_format[id]["mods"][mod]["game_version"], "✅"))
            else:
                mods_list_viewer.insert(parent='', text='', index="end", values=(mod.replace(".rar", "").replace(".zip", ""), games_db_yuzu_format[id]["mods"][mod]["host"], games_db_yuzu_format[id]["mods"][mod]["game_version"], "❌"))
    

    actual_game = id

def toogle_cheat():
    if actual_game != "":
        cheats_selected = cheats_list_viewer.item(cheats_list_viewer.focus())["values"]
        if cheats_selected != "":
            with open(f"{yuzupath}/load/{actual_game}/cheats/cheats.txt", "r") as f:
                tmp = f.read()
                f.close()
            if not cheats_selected[0] in tmp:
                with open(f"{yuzupath}/load/{actual_game}/cheats/cheats.txt", "a") as f:
                    f.write(f"\n[{cheats_selected[0]}]\n")
                    for ccode in games_db_yuzu_format[actual_game]["cheats"][cheats_selected[0]]:
                        f.write(f"{ccode}\n")
                    f.close()
                settings_variables["cheats_status"][actual_game][cheats_selected[0]] = True
            else:
                for ccode in games_db_yuzu_format[actual_game]["cheats"][cheats_selected[0]]:
                    tmp = tmp.replace(ccode, "")
                tmp = tmp.replace(f"\n[{cheats_selected[0]}]", "")
                with open(f"{yuzupath}/load/{actual_game}/cheats/cheats.txt", "w") as f:
                    f.write(tmp)
                    f.close()
                settings_variables["cheats_status"][actual_game][cheats_selected[0]] = False
            print(settings_variables["cheats_status"][actual_game])
            apply_settings()
        select_game(actual_game)
    
def disable_all_cheats():
    if actual_game != "":
        with open(f"{yuzupath}/load/{actual_game}/cheats/cheats.txt", "w") as f:
            f.write("")
            f.close()
        for cheat in settings_variables["cheats_status"][actual_game].keys():
            settings_variables["cheats_status"][actual_game][cheat] = False
        apply_settings()
        select_game(actual_game)
        
def toogle_mod():
    if actual_game != "":
        mod_selected = mods_list_viewer.item(mods_list_viewer.focus())["values"]
        if mod_selected != "":
            if not settings_variables["mods_status"][actual_game][mod_selected[0]+".rar"]:
                # patoolib.extract_archive(f"{yuzupath}/load/{actual_game}/{mod_selected[0]}.rar", outdir=f"{yuzupath}/load/{actual_game}/")
                settings_variables["mods_status"][actual_game][mod_selected[0]+".rar"] = True
            else:
                shutil.rmtree(f"{yuzupath}/load/{actual_game}/{mod_selected[0]}")
                settings_variables["mods_status"][actual_game][mod_selected[0]+".rar"] = False
            apply_settings()
        select_game(actual_game)


def cheat_editor():
    if "txt_editor.py" in extensions:
        if os.name == "nt":
            os.system(f"python -u {path}/extensions/txt_editor.py")
        else:
            os.system(f"python3 -u {path}/extensions/txt_editor.py")
    else:
        showerror("Erreur", "L'extension \"Editeur de cheats (Simple Text Editor)\" n'est pas installée. Veuillez télécharger et installer cette extension pour pouvoir utiliser cet outil.")
    


def apply_settings():
    with open(path+"/cache/settings.json", "w") as f:
        json.dump({
        "rpc": settings_variables["rpc"].get(),
        "check_repo": settings_variables["check_repo"].get(),
        "disable_updates": settings_variables["disable_updates"].get(),
        "games": settings_variables["games"],
        "theme": settings_variables["theme"].get(),
        "mods_status": settings_variables["mods_status"],
        "cheats_status": settings_variables["cheats_status"]
    }, f, indent=4)
        f.close()


if not os.path.exists(path+"/cache"):
    os.mkdir(path+"/cache")

if os.name == "nt":
   yuzupath = f"C:\\Users\\{getpass.getuser()}\\AppData\Roaming\\yuzu"
else:
    yuzupath = f"/home/{getpass.getuser()}/.local/share/yuzu"

if os.path.exists(yuzupath):
    if not os.path.exists(yuzupath+"/load"):
        showerror("Erreur", "Yuzu n'est pas détecté")
        sys.exit()
else:
    showerror("Erreur", "Yuzu n'est pas détecté")
    sys.exit()

if len(os.listdir(yuzupath+"/load")) == 0:
    showerror("Erreur", "Aucun jeu n'est installé sur l'émulateur")
    sys.exit()

# Initilisation des paramètres
settings_variables = {
    "rpc": tk.BooleanVar(value=True),
    "check_repo": tk.BooleanVar(value=True),
    "disable_updates": tk.BooleanVar(value=False),
    "games": [],
    "theme": tk.IntVar(value=0),
    "mods_status": {},
    "cheats_status": {}
}

if not os.path.exists(path+"/cache/settings.json"):
    apply_settings()
else:
    with open(path+"/cache/settings.json", "r") as f:
        data1 = json.loads(f.read())
        f.close()

    for setting in list(data1.keys()):
        if setting in ["games", "mods_status", "cheats_status"]:
            settings_variables[setting] = data1[setting]
        else:
            settings_variables[setting].set(data1[setting])

themes = os.listdir(f"{path}/themes/")
for theme in themes:
    if "." in themes:
        themes.remove(theme)

theme_used = themes[settings_variables["theme"].get()]

if os.path.exists(path+"/themes"):
    if not os.path.exists(path+"/themes/"+theme_used):
        showerror("Erreur", "Une erreur c'est produite lors de la vérification du thème actuel.")
        sys.exit()
else:
    showerror("Erreur", "Une erreur c'est produite lors de la vérification du thème actuel.")


# Cacher la fenêtre principale
window.withdraw()


# Activer la RPC Discord
if settings_variables["rpc"] == True:
    try:
        RPC = Presence(1022537407448490125)
        RPC.connect()
        RPC.update(
            details=f"Application: MultiMod",
            state=f"MultiMod est un outil permettant d'installer et de gérer des mods et des cheats.",
            large_image="logomm",
            large_text="MultiMod - Team EmuKit",
            buttons=[{"label": "En savoir plus", "url": "https://luckyluka17.github.io/MultiMod/"}, {"label": "Rejoindre le Discord", "url": "https://discord.gg/HmN6pyFU5B"}],
            start=int(time.time())
        )
    except:
        pass


# Vérifier les extenions
if os.path.exists(path+"/extensions/"):
    extensions = {}

    for extension in os.listdir(path+"/extensions"):
        if extension.endswith(".py"):
            with open(path+"/extensions/"+extension, "r") as f:
                data_extension = f.read()
                f.close()
            # Séparation des informations et du code
            data_extension = data_extension.split("#-- ^ INFORMATIONS SUR L'EXTENSION ^ --")[0].split("\n")

            del data_extension[3]

            if data_extension[0].startswith("#") and data_extension[1].startswith("#") and data_extension[2].startswith("#") and len(data_extension) == 3:
                extensions[extension] = {
                    "name": data_extension[0].replace("#", ""),
                    "version": float(data_extension[1].replace("#", "")),
                    "developer": data_extension[2].replace("#", "")
                }
    
    print(extensions)


# Tester l'api de Github
print(Fore.YELLOW + "Vérification des rate limits de l'api Github...")

with requests.get("https://api.github.com/") as r:
    api_data = json.loads(r.text)
    r.close()

if "message" in api_data:
    if "rate limit" in api_data["message"]:
        print(Fore.RED + "Impossible d'accéder à l'api de Github. Cela est dû à un envoi de requetes fréquentes par le logiciel. Veuillez réessayer plus tard.")
        showerror("Erreur", "Impossible d'accéder à l'api de Github. Cela est dû à un envoi de requetes fréquentes par le logiciel. Veuillez réessayer plus tard.\nError: "+api_data["message"])
        sys.exit()
else:
    print(Fore.GREEN + "L'api Github connectée.")


# Afficher la fenêtre de chargement
loading_window.title("Chargement de MultiMod")
if os.name == "nt":
    window.iconbitmap(path+"/themes/"+theme_used+"/images/logo.ico")
loading_window.geometry("300x100")
loading_window.resizable(False, False)

loading_label = ttk.Label(
    loading_window,
    text="\nTéléchargement de la base de données\n",
    font=("Calibri", 10)
)
loading_label.pack()

loading_bar = ttk.Progressbar(
    loading_window,
    value=0,
    orient="horizontal",
    mode="determinate",
    length=155
)
loading_bar.pack()

loading_window.update()

games_db_yuzu_format = {}

if not os.listdir(yuzupath+"/load") == settings_variables["games"] or not os.path.exists(path+"/cache/yuzu_db.json"):
    with requests.get("https://raw.githubusercontent.com/blawar/titledb/master/FR.fr.json") as r:
        games_db = json.loads(r.text)
        r.close()

    loading_window.update()
    loading_label.config(text="\nTraitement de la base de données\n0% (0/0)\n")
    loading_window.update()
    settings_variables["games"] = os.listdir(yuzupath+"/load")
    status = 0
    for game in list(games_db.keys()):
        st_time = time.time()
        if games_db[game]["id"] != None:
            if games_db[game]["id"] in os.listdir(yuzupath+"/load/"):
                games_db_yuzu_format[games_db[game]["id"]] = {
                    "name": games_db[game]["name"],
                    "db_id": game,
                    "icon": games_db[game]["iconUrl"],
                    "publisher": games_db[game]["publisher"],
                    "size": games_db[game]["size"],
                    "screenshots": games_db[game]["screenshots"],
                    "cheats": {},
                    "mods": {},
                }
                print(Fore.GREEN + f"Jeu ajouté [{games_db[game]['id']}]" + str(games_db_yuzu_format[games_db[game]["id"]]))

                with requests.get(f"https://api.github.com/repos/ibnux/switch-cheat/contents/atmosphere/titles/{games_db[game]['id']}/cheats") as r:
                    data1 = json.loads(r.text)
                    r.close()

                with requests.get(f"https://api.github.com/repositories/701704734/contents/mods/{games_db[game]['id']}/[{games_db[game]['id']}]") as r:
                    data2 = json.loads(r.text)
                    r.close()

                if not "message" in data1:
                    for cheat in data1:
                        with requests.get(f"https://raw.githubusercontent.com/ibnux/switch-cheat/master/atmosphere/titles/{games_db[game]['id']}/cheats/{cheat['name']}") as r:
                            content = r.text
                            r.close()
                        content = content.split("\n\n")
                        for c in content:
                            c1 = c.split("\n")
                            games_db_yuzu_format[games_db[game]['id']]["cheats"][c1[0].replace("[", "").replace("]", "")] = c1[1:len(c1)]
                    del c1, content
                    print(Fore.GREEN + f"Nombre de cheats trouvés : {len(list(games_db_yuzu_format[games_db[game]['id']]['cheats'].keys()))}")

                if not "message" in data2:
                    for mod in data2:
                        with requests.get(f"https://api.github.com/repositories/701704734/contents/mods/{games_db[game]['id']}/[{games_db[game]['id']}]/{mod['name']}/") as r:
                            for file in json.loads(r.text):
                                if not file["name"] == "...":
                                    games_db_yuzu_format[games_db[game]['id']]["mods"][file["name"]] = {
                                        "url": file["download_url"],
                                        "size": file["size"],
                                        "author": "?",
                                        "host": file["download_url"].split("/")[2],
                                        "game_version": mod['name'].replace("v", "")
                                    }
                    print(Fore.GREEN + f"Nombre de mods trouvés : {len(list(games_db_yuzu_format[games_db[game]['id']]['mods'].keys()))}")

            else:
                print(Fore.YELLOW + f"Jeu ignoré [{games_db[game]['id']}] : Pas installé sur Yuzu.")
        status += 1
        loading_bar.config(value=int(status/len(games_db)*100))
        loading_label.config(text=f"\nTraitement de la base de données\n{str(int(status/len(games_db)*100))}% ({status}/{len(games_db)})\n")
        loading_window.update()

    with open(path+"/cache/yuzu_db.json", "w") as f:
        json.dump(games_db_yuzu_format, f, indent=4)
        f.close()
else:
    with open(path+"/cache/yuzu_db.json", "r") as f:
        games_db_yuzu_format = json.loads(f.read())
        f.close()

apply_settings()

loading_window.update()
loading_label.config(text=f"\nRécupération des icones\n0% (0/{len(os.listdir(yuzupath+'/load'))})\n")
loading_window.update()

if not os.path.exists(path+"/cache/Icons"):
    os.mkdir(path+"/cache/Icons")
else:
    for icon in os.listdir(path+"/cache/Icons"):
        os.remove(path+"/cache/Icons/"+icon)

status = 0
loading_bar.config(value=0)
loading_window.update()

# Charger les icones des thèmes
icons = {}
for icon in os.listdir(f"{path}/themes/{theme_used}/icons/"):
    icons[icon.replace(".png", "")] = tk.PhotoImage(file=path+"/themes/"+theme_used+"/icons/"+icon)

for game in os.listdir(yuzupath+"/load"):
    try:
        wget.download(games_db_yuzu_format[game]["icon"], path+"/cache/Icons/"+game+".jpg")
        wget.download(games_db_yuzu_format[game]["icon"], path+"/cache/Icons/"+game+"40.jpg")

        image_r = PIL.Image.open(path+"/cache/Icons/"+game+".jpg")
        image_r1 = PIL.Image.open(path+"/cache/Icons/"+game+"40.jpg")
        image_r.thumbnail((130, 130), PIL.Image.Resampling.LANCZOS)
        image_r1.thumbnail((40, 40), PIL.Image.Resampling.LANCZOS)
        image_r.save(path+"/cache/Icons/"+game+".png", 'PNG', quality=88)
        image_r1.save(path+"/cache/Icons/"+game+"40.png", 'PNG', quality=88)

        os.remove(path+"/cache/Icons/"+game+"40.jpg")
        os.remove(path+"/cache/Icons/"+game+".jpg")
    except:
        print(Fore.RED + "Icone ignoré : jeu invalide")

    status += 1
    loading_bar.config(value=int(status/len(os.listdir(yuzupath+"/load"))*100))
    loading_label.config(text=f"\nRécupération des icones\n{str(int(status/len(os.listdir(yuzupath+'/load'))*100))}% ({status}/{len(os.listdir(yuzupath+'/load'))})\n")
    loading_window.update()

del image_r

loading_window.update()
loading_label.config(text=f"\nCopie des mods\n0% (0/{len(os.listdir(yuzupath+'/load'))})\n")
loading_window.update()

status = 0
loading_bar.config(value=0)
loading_window.update()

for game in os.listdir(yuzupath+"/load"):
    if game in games_db_yuzu_format:
        if not len(games_db_yuzu_format[game]["mods"].keys()) == 0:
            for mod in games_db_yuzu_format[game]["mods"].keys():
                if os.path.exists(f"{yuzupath}/load/{game}/{mod}.zip"):
                    os.remove(f"{yuzupath}/load/{game}/{mod}.zip")
                wget.download(games_db_yuzu_format[game]["mods"][mod]["url"].replace("%5B", "[").replace("%5D", "]").replace("%20", " "), f"{yuzupath}/load/{game}/{mod}")

    status += 1
    loading_bar.config(value=int(status/len(os.listdir(yuzupath+"/load"))*100))
    loading_label.config(text=f"\nCopie des mods\n{str(int(status/len(os.listdir(yuzupath+'/load'))*100))}% ({status}/{len(os.listdir(yuzupath+'/load'))})\n")
    loading_window.update()

loading_window.update()
loading_label.config(text=f"\nChargement des cheats et des mods\n0% (0/{len(os.listdir(yuzupath+'/load'))})\n")
loading_window.update()

status = 0
loading_bar.config(value=0)
loading_window.update()

for game in os.listdir(yuzupath+"/load"):
    if game in games_db_yuzu_format:
        settings_variables["cheats_status"][game] = {}
        settings_variables["mods_status"][game] = {}

        for cheat in games_db_yuzu_format[game]["cheats"].keys():
            settings_variables["cheats_status"][game][cheat] = False

        for mod in games_db_yuzu_format[game]["mods"].keys():
            settings_variables["mods_status"][game][mod] = False
            
    apply_settings()

    status += 1
    loading_bar.config(value=int(status/len(os.listdir(yuzupath+"/load"))*100))
    loading_label.config(text=f"\nChargement des cheats et des mods\n{str(int(status/len(os.listdir(yuzupath+'/load'))*100))}% ({status}/{len(os.listdir(yuzupath+'/load'))})\n")
    loading_window.update()

loading_window.destroy()

window.deiconify()

window.title("MultiMod")
if os.name == "nt":
    window.iconbitmap(path+"/themes/"+theme_used+"/images/logo.png")
window.resizable(False, False)
window.geometry("1090x550")

menubar = tk.Menu()

file_menu = tk.Menu(tearoff=0)
games_menu = tk.Menu(tearoff=0)
settings_menu = tk.Menu(tearoff=0)
tools_menu = tk.Menu(tearoff=0)
dfirmware_menu = tk.Menu(tearoff=0)
firmware_menu = tk.Menu(tearoff=0)
os_menu = tk.Menu(tearoff=0)
help_menu = tk.Menu(tearoff=0)
exp_menu = tk.Menu(tearoff=0)
ext_menu = tk.Menu(tearoff=0)
account_menu = tk.Menu(tearoff=0)
theme_menu = tk.Menu(tearoff=0)

menubar.add_cascade(menu=file_menu, label="Fichier")
menubar.add_cascade(menu=tools_menu, label="Outils & extensions")
# if "connect.py" in extensions:
#     menubar.add_cascade(menu=account_menu, label="Compte (expérimental)")
menubar.add_cascade(menu=dfirmware_menu, label="Firmwares")
menubar.add_cascade(menu=help_menu, label="?")

file_menu.add_cascade(label="Sélectionner un jeu", menu=games_menu, image=icons["select_game"], compound="left")
file_menu.add_separator()
file_menu.add_cascade(label="Paramètres", menu=settings_menu, image=icons["settings"], compound="left")
file_menu.add_command(label="Quitter", command=lambda: sys.exit(), image=icons["close"], compound="left")

with open(path+"/cache/tmp.py", "a") as f:
    for game in os.listdir(yuzupath+"/load"):
        if game in list(games_db_yuzu_format.keys()):
            f.write(f'temp_icon_{game}=tk.PhotoImage(file="{path}/cache/Icons/{game}40.png")\ngames_menu.add_command(label="{games_db_yuzu_format[game]["name"].replace("™", "")}", command=lambda: select_game(id="{game}"), compound="left", image=temp_icon_{game})\n')
    f.close()

with open(path+"/cache/tmp.py", "r") as f:
    exec(f.read())
    f.close()

os.remove(path+"/cache/tmp.py")

games_menu.add_separator()
games_menu.add_command(label="Aide : Mon/mes jeu(x) ne s'affichent pas", command=lambda: showinfo("Aide", "Si un ou plusieurs jeux ne s'affichent pas dans ce menu, quittez le logiciel puis ouvrez Yuzu. Vérifiez que vos jeux sont bien visibles sur Yuzu, et si c'est le cas, ouvrez le jeu au moins une fois."))

settings_menu.add_checkbutton(label="Rich Presence Discord (redémarrage requis de l'app)", variable=settings_variables["rpc"], command=apply_settings)
settings_menu.add_checkbutton(label="Vérification des dépôts Github avant installation", variable=settings_variables["check_repo"], command=apply_settings)
settings_menu.add_checkbutton(label="Ne pas mettre à jour (déconseillé)", variable=settings_variables["disable_updates"], command=apply_settings)
settings_menu.add_cascade(menu=theme_menu, label="Thèmes")

tvalue = 0
for theme in os.listdir(f"{path}/themes/"):
    if not "." in theme:
        theme_menu.add_radiobutton(label=theme, variable=settings_variables["theme"], value=tvalue, command=apply_settings)
        tvalue += 1
del tvalue

if "txt_editor.py" in extensions:
    tools_menu.add_command(label="Editeur de cheats", image=icons["cheats_editor"], compound="left", command=cheat_editor)
else:
    tools_menu.add_command(label="Editeur de cheats", image=icons["cheats_editor"], compound="left", state="disabled")
tools_menu.add_command(label="Catalogue d'extensions", image=icons["extensions"], compound="left")
tools_menu.add_separator()
tools_menu.add_cascade(label="Extensions", image=icons["extensions_menu"], compound="left", menu=ext_menu)

for ext in extensions.keys():
    ext_menu.add_command(label=extensions[ext]["name"]+" | Par "+extensions[ext]["developer"])

dfirmware_menu.add_command(label="Télécharger le dernier firmware", command=download_latest_firmware, image=icons["download"], compound="left")
dfirmware_menu.add_separator()
dfirmware_menu.add_cascade(label="Liste des firmwares pris en charge", menu=firmware_menu, image=icons["firmwares"], compound="left")

# Récupérer la liste des firmwares
with requests.get("https://api.github.com/repos/THZoria/NX_Firmware/releases") as r:
    firmwares = json.loads(r.text)
    r.close()

    for firmware in firmwares:
        firmware_menu.add_command(label=f"{firmware['name']} - {firmware['published_at'].split('T')[0].replace('-', '/')}")

# account_menu.add_command(label="Connexion à un compte MultiMod", image=icons["login"], compound="left")
# account_menu.add_command(label="Déconnexion", state="disabled", image=icons["logout"], compound="left")
# account_menu.add_separator()
# account_menu.add_command(label="Informations sur votre compte", image=icons["informations"], compound="left", command=lambda:(showinfo("Information", "Stockage utilisé: 0/20Mo\nType de compte: gratuit\nClé de license: aucune")))
# account_menu.add_separator()
# account_menu.add_command(label="Synchroniser maintenant (paramètres et bdd)", image=icons["sync_now"], compound="left")

help_menu.add_command(label="Serveur Discord", command=lambda: web.open('https://discord.gg/SGHtzYbvRx'), image=icons["discord"], compound="left")
help_menu.add_command(label="Wiki", command=lambda: web.open('https://github.com/Luckyluka17/MultiMod/wiki'), image=icons["documentation"], compound="left")
help_menu.add_command(label="Dépot Github", command=lambda: web.open('https://github.com/Luckyluka17/MultiMod'), image=icons["repo"], compound="left")
help_menu.add_command(label="Crédits", command=lambda: showinfo("Information", "Les crédits ont été déplacés dans le README.md du dépôt MultiMod, sous le titre \"Sources\"."), image=icons["informations"], compound="left")
help_menu.add_separator()
help_menu.add_command(label="Vérifier les mises à jour", image=icons["check_update"], compound="left", state="disabled")
help_menu.add_command(label="Envoyer un rapport d'erreur", image=icons["bug"], compound="left", state="disabled")

tabs = ttk.Notebook(window)

tab1 = tk.Frame(tabs)
tab2 = tk.Frame(tabs)
tab3 = tk.Frame(tabs)

tabs.add(tab1, text='Gestionnaire de cheats')
tabs.add(tab2, text='Gestionnaire de mods')
tabs.add(tab3, text='A propos du logiciel')
tabs.pack(expand=1, fill="both")

# Onglet cheats
cheats_tree_frame = ttk.LabelFrame(
    tab1,
    text="Liste des cheats disponibles"
)
cheats_tree_frame.grid(column=0, row=0, padx=5, pady=10)

games_infos_frame = ttk.LabelFrame(
    tab1,
    text="Informations sur le jeu"
)
games_infos_frame.grid(column=1, row=0, padx=5, pady=10)

cheats_list_viewer = ttk.Treeview(
    cheats_tree_frame,
    columns=("Nom du cheat", "Code", "Status")
)
cheats_list_viewer.pack(side="left")

scrollbar1 = ttk.Scrollbar(
    cheats_tree_frame,
    orient="vertical"
)
scrollbar1.pack(side="right", fill='y')
cheats_list_viewer.configure(yscrollcommand=scrollbar1.set)

cheats_list_viewer.column('#0', width=0, stretch=False)
cheats_list_viewer.column("Nom du cheat", anchor='center', width=270)
cheats_list_viewer.column("Code", anchor='center', width=240)
cheats_list_viewer.column("Status", anchor='center', width=75)

cheats_list_viewer.heading('#0', text='', anchor='center')
cheats_list_viewer.heading("Nom du cheat", text="Nom du cheat", anchor='center')
cheats_list_viewer.heading("Code", text="Code", anchor='center')
cheats_list_viewer.heading("Status", text="Status", anchor='center')

pochette = tk.PhotoImage(file=f'{path}/cache/Icons/{os.listdir(path+"/cache/Icons/")[0]}')

game_logo = ttk.Label(
    games_infos_frame,
    image=pochette
)
game_logo.pack()

game_name = ttk.Label(
    games_infos_frame,
    text="\nAucun jeu sélectionné",
    font=("Calibri", 13)
)
game_name.pack(padx=5)

actions_frame1 = ttk.LabelFrame(
    tab1,
    text="Actions"
)
actions_frame1.grid(column=0, row=1, padx=2, pady=1)

ttk.Button(
    actions_frame1,
    text="Activer/désactiver le cheat séléctionné",
    cursor="hand2",
    command=lambda:toogle_cheat()
).grid(padx=5, pady=2, column=0, row=0)

ttk.Button(
    actions_frame1,
    text="Désactiver tous les cheats",
    cursor="hand2",
    command=lambda:disable_all_cheats()
).grid(padx=5, pady=2, column=1, row=0)

ttk.Button(
    actions_frame1,
    text="Rafraichir la liste",
    cursor="hand2",
    command=lambda:(select_game(actual_game),showinfo("Information", "La liste a été actualisée."))
).grid(padx=5, pady=2, column=2, row=0)


# Onglet mods
mods_tree_frame = ttk.LabelFrame(
    tab2,
    text="Liste des mods disponibles"
)
mods_tree_frame.grid(column=0, row=0, padx=5, pady=10)

games_infos_frame1 = ttk.LabelFrame(
    tab2,
    text="Informations sur le jeu"
)
games_infos_frame1.grid(column=1, row=0, padx=5, pady=10)

mods_list_viewer = ttk.Treeview(
    mods_tree_frame,
    columns=("Nom du mod", "Hébergeur", "Version jeu", "Status")
)
mods_list_viewer.pack(side="left")

scrollbar2 = ttk.Scrollbar(
    mods_tree_frame,
    orient="vertical"
)
scrollbar2.pack(side="right", fill="y")
mods_list_viewer.configure(yscrollcommand=scrollbar2.set)

mods_list_viewer.column('#0', width=0, stretch=False)
mods_list_viewer.column("Nom du mod", anchor='center', width=240)
mods_list_viewer.column("Hébergeur", anchor='center', width=110)
mods_list_viewer.column("Version jeu", anchor='center', width=110)
mods_list_viewer.column("Status", anchor='center', width=75)

mods_list_viewer.heading('#0', text='', anchor='center')
mods_list_viewer.heading("Nom du mod", text="Nom du mod", anchor='center')
mods_list_viewer.heading("Hébergeur", text="Hébergeur", anchor='center')
mods_list_viewer.heading("Version jeu", text="Version du jeu", anchor='center')
mods_list_viewer.heading("Status", text="Status", anchor='center')

game_logo1 = ttk.Label(
    games_infos_frame1,
    image=pochette
)
game_logo1.pack()

game_name1 = ttk.Label(
    games_infos_frame1,
    text="\nAucun jeu sélectionné",
    font=("Calibri", 13)
)
game_name1.pack(padx=5)

actions_frame2 = ttk.LabelFrame(
    tab2,
    text="Actions"
)
actions_frame2.grid(column=0, row=1, padx=2, pady=1)

ttk.Button(
    actions_frame2,
    text="Activer/désactiver le mod sélectionné",
    cursor="hand2",
    command=lambda:toogle_mod()
).grid(padx=5, pady=2, column=0, row=0)

ttk.Button(
    actions_frame2,
    text="Désactiver tous les mods",
    cursor="hand2",
).grid(padx=5, pady=2, column=1, row=0)

ttk.Button(
    actions_frame2,
    text="Rafraichir la liste",
    cursor="hand2",
    command=lambda:(select_game(actual_game),showinfo("Information", "La liste a été actualisée."))
).grid(padx=5, pady=2, column=2, row=0)

# Onglet a propos (tab3)
ttk.Label(
    tab3,
    text=f"\n\nVersion {version} - Développé par Team EmuKit",
    font=("Calibri", 18)
).pack()

buttons_about = ttk.Frame(
    tab3
)
buttons_about.pack()

ttk.Button(
    buttons_about,
    text="Serveur Discord",
    cursor="hand2",
    command=lambda:(web.open("https://discord.gg/GHETzETTtY"))
).grid(row=0, column=0, padx=5, pady=5)

ttk.Button(
    buttons_about,
    text="Dépôt Github",
    cursor="hand2",
    command=lambda:(web.open("https://github.com/Luckyluka17/MultiMod"))
).grid(row=0, column=1, padx=5, pady=5)

window.config(menu=menubar)
window.mainloop()