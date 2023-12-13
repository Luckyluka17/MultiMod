<h1 align="center"><img src="assets/img/logo.png" width="160px"><br/>MultiMod - Mods manager for Yuzu</h1>

**Langue :** [🇫🇷 Français](https://github.com/Luckyluka17/MultiMod/blob/main/README.md) - [🇬🇧 English](https://github.com/Luckyluka17/MultiMod/blob/main/README_EN.md)


_Ce logiciel remplace [YuzuCheatsManager](https://github.com/Luckyluka17/YuzuCheatsManager), qui n'est plus mis à jour._

MultiMod est un outil permettant d'installer et de gérer des mods et des cheats. Il peut également intaller les derniers firmwares à jour.

> **ATTENTION : Le logiciel n'est pas fait pour supporter trop de jeux installés sur Yuzu. Pour un bon fonctionnement, nous vous recommandons d'avoir au maximum 20 à 25 jeux, vous pouvez bien évidemment dépasser cette limite, mais cela risque de causer quelques problèmes.**

<a href=""><img src="https://www.allkpop.com/upload/2021/01/content/262046/1611711962-discord-button.png" width="105px"></a>
<a href="https://www.buymeacoffee.com/luckyluka17" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="120px"></a>

## Installation

>  **👉 Aide complémentaire :** Consultez le [wiki](https://github.com/Luckyluka17/MultiMod/wiki) si vous souhaitez un tutoriel complet sur l'installation de l'outil, ou si vous recontrez des difficultés.

### Windows

- Pack de fichiers (contient au moins un thème, et des extensions indispensables)
    - Fichier compressé **zip** (recommandé) :
[Télécharger](https://github.com/Luckyluka17/MultiMod/releases/latest/download/multimod.zip)
    - Fichier compressé **rar** :
[Télécharger](https://github.com/Luckyluka17/MultiMod/releases/latest/download/multimod.rar)
- Exécutable :
[Télécharger](https://github.com/Luckyluka17/MultiMod/releases/latest/download/multimod.exe)

> **👉 Bon à savoir :** Si vous téléchargez le fichier .exe, vous ne pourrez pas le lancer en l'état. Il faudra installer au minimum un thème, pour cela, [suivez ces instructions](https://github.com/Luckyluka17/MultiMod#installer-un-th%C3%A8me).

### Linux

> **👉 Prérequis :** Vous devez posséder python3 (généralement préinstallé) et git sur votre machine. 

```sh
sudo apt install python3-pip
sudo apt install python3-tk

git clone https://github.com/Luckyluka17/MultiMod.git
cd MultiMod
python3 -m pip install -r requirements.txt

python3 -u theme_installer.py native
```

> Utilisez la commande `python3 -u multimod.py` pour lancer le logiciel

## Sources

- Cheats
    - [switch-cheat](https://github.com/ibnux/switch-cheat) ([@ibnux](https://github.com/ibnux))
- Mods
    - [Switch Mods](https://github.com/yuzu-emu/yuzu/wiki/Switch-Mods) ([@yuzu-emu](https://github.com/yuzu-emu))
    - [switch-ptchtxt-mods](https://github.com/theboy181/switch-ptchtxt-mods) ([@theboy181](https://github.com/theboy181))
- Firmwares/keys
    - [NX_Firmware](https://github.com/THZoria/NX_Firmware) ([@THZoria](https://github.com/THZoria))
- Métadonnées des jeux
    - [titledb](https://github.com/blawar/titledb) ([@blawar](https://github.com/blawar))


## Thèmes

> **👉 Important :** Python 3 est nécessaire pour l'exécution du script.

### Thèmes disponibles
- native (Thème par défaut)

### Installer un thème
```sh
# Commande pour Linux
python3 -u theme_installer.py [nom du thème]

# Commande pour Windows
python -u theme_installer.py [nom du thème]
```
> Remplacez **[nom du thème]** par le nom du thème que le script doit installer.

## License (MIT)
```
Copyright (c) 2023 Luckyluka17

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```
