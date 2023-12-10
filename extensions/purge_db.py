#Supprimer la base de données
#1.0
#Luckyluka17
#-- ^ INFORMATIONS SUR L'EXTENSION ^ --
import os
from tkinter.messagebox import showinfo

os.remove(os.getcwd()+"/cache/yuzu_db.json")

showinfo("Information", "La base de données a été supprimée. Vous pouvez la mettre à jour en redémarrant le logiciel.")