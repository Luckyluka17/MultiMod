# Téléchargement des mods, dans le dossier db
# Organisation des dossiers et tri
import os
import requests
import json
import shutil
import wget
import zipfile

if os.path.exists(os.getcwd()+"/mods/"):
    shutil.rmtree("mods")

os.mkdir("mods")

path = os.getcwd()+"/mods/"
os.chdir(path)


wget.download("https://github.com/theboy181/switch-ptchtxt-mods/archive/refs/heads/main.zip", "mods.zip")

with zipfile.ZipFile("mods.zip", 'r') as zip_ref:
    zip_ref.extractall(path)
os.remove("mods.zip")
os.remove(path+"switch-ptchtxt-mods-main/README.md")

for game in os.listdir(path+"switch-ptchtxt-mods-main/"):
    shutil.move(path+"switch-ptchtxt-mods-main/"+game, path)

shutil.rmtree("switch-ptchtxt-mods-main")

for folder in os.listdir(path):
    os.rename(folder, folder.lower())

with requests.get("https://raw.githubusercontent.com/blawar/titledb/master/FR.fr.json") as r:
    data = json.loads(r.text)
    r.close()

db = {}

for game in data.keys():
    print(game)
    try:
        db[data[game]["name"].lower()] = data[game]["id"]
    except:
        pass

for folder in os.listdir(path):
    try:
        os.rename(folder, db[folder])
    except KeyError:
        shutil.rmtree(folder)