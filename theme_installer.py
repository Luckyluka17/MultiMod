#
# Script d'installation de thèmes pour MultiMod
# Réalisé par Luckyluka17 - Version 1.0
#
import sys
import os
from colorama import Fore, init
import wget
import requests
import json

init(autoreset=True)

theme = sys.argv[1]
a_path = os.getcwd()


with requests.get("https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/themes/list.json") as r:
    informations = json.loads(r.text)
    r.close()

if not theme in informations["themes"]:
    print(Fore.RED + "Le thème n'existe pas !")
    sys.exit()

if not os.path.exists(a_path+"/themes"):
    print(Fore.YELLOW + "Création d'un dossier themes")
    os.mkdir(a_path+"/themes")
else:
    print(Fore.GREEN + "Dossier themes déjà présent")


if not os.path.exists(f"{a_path}/themes/{theme}"):
    os.mkdir(f"{a_path}/themes/{theme}")
    print(Fore.YELLOW + "Téléchargement des fichiers...")

    wget.download(f"https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/themes/{theme}/theme.json", f"{a_path}/themes/{theme}/theme.json")

    os.mkdir(f"{a_path}/themes/{theme}/icons")
    os.mkdir(f"{a_path}/themes/{theme}/images")

    for icon in informations["icons"]:
        wget.download(f"https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/themes/{theme}/icons/{icon}", f"{a_path}/themes/{theme}/icons/{icon}")

    wget.download(f"https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/themes/{theme}/images/banner.png", f"{a_path}/themes/{theme}/images/banner.png")
    wget.download(f"https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/themes/{theme}/images/logo.ico", f"{a_path}/themes/{theme}/images/logo.ico")
    wget.download(f"https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/themes/{theme}/images/logo.png", f"{a_path}/themes/{theme}/images/logo.png")
    print(Fore.GREEN + "\nThème installé")
    sys.exit()
else:
    print(Fore.RED + "Thème déjà installé !")
    sys.exit()
