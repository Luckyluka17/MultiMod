<h1 align="center"><img src="assets/img/logo.png" width="160px"><br/>MultiMod - Mod manager for Yuzu</h1>

**Langue :** [🇫🇷 Français](https://github.com/Luckyluka17/MultiMod/blob/main/README.md) - [🇬🇧 English](https://github.com/Luckyluka17/MultiMod/blob/main/README_EN.md)


MultiMod est un outil permettant d'installer et de gérer des mods et des cheats. Ce logiciel remplace [YuzuCheatsManager](https://github.com/Luckyluka17/YuzuCheatsManager), qui permet uniquement de télécharger et d'installer des cheats. Il fonctionne **uniquement avec des dépôts Github**. 

Pour apprendre à utiliser le logiciel, vous pouvez consulter le [wiki](https://github.com/Luckyluka17/MultiMod/wiki).

<a href=""><img src="https://www.allkpop.com/upload/2021/01/content/262046/1611711962-discord-button.png" width="105px"></a>
<a href="https://www.buymeacoffee.com/luckyluka17" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="120px"></a>

## Installation

> Consultez le [wiki](https://github.com/Luckyluka17/MultiMod/wiki) si vous souhaitez un tutoriel complet sur l'installation de l'outil, ou si vous recontrez des difficultés.

### Windows
[Cliquez ici](https://github.com/Luckyluka17/MultiMod/releases/latest/download/multimod.exe) pour télécharger la dernière version.

### Linux
```sh
# Télécharger les paquets prérequis
sudo apt install python3
sudo apt install python3-pip

# Si vous êtes sur ChromeOS, installez ce paquet
sudo apt install python3-tk

# Créer un dossier pour le logiciel
mkdir MultiMod
cd MultiMod

# Télécharger et installer les modules prérequis
wget https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/multimod.py
wget https://raw.githubusercontent.com/Luckyluka17/MultiMod/main/requirements.txt
python3 -m pip install -r requirements.txt
```

> Utilisez la commande `python3 -u multimod.py` pour lancer le logiciel

## Fonctionnalités disponibles

- Téléchargement des ~~clés/~~ firmwares
- Téléchargement de cheats et de mods
- Gestion des cheats et des mods

## MIT License
```
Copyright (c) 2023 Luckyluka17

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```
