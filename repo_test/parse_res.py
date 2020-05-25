# CSE Groupe 2 2020
# Permet de lire le fichier rex.txt et le transformer en fichier xml


import os
import sys

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree



# Fonction permettant d'ajouter des retour a la ligne 
# et des indentations
def indent(elem, level=0):
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# Fin de la fonction ----------------------------------------------


# Lecture du resultat de l'algo OCR
f_in = open("res.txt","r+")
texte = f_in.read();
# print(texte);


# Cree la base du fichier XML
root = ET.Element("sachet");

personne = ET.SubElement(root, 'personne');
nom = ET.SubElement(personne, 'nom');
#nom.text = "asterix";
prenom = ET.SubElement(personne, 'prenom');


adresse = ET.SubElement(root, 'adresse');
ville = ET.SubElement(adresse, 'ville');
npa = ET.SubElement(adresse, 'npa');
rue = ET.SubElement(adresse, 'rue');
numero = ET.SubElement(adresse, 'numero');

time = ET.SubElement(root, 'time');
heure = ET.SubElement(time, 'heure');
date = ET.SubElement(time, 'date');

heure_m = ET.SubElement(heure, 'heure');
minute_m = ET.SubElement(heure, 'minute');

jourstr = ET.SubElement(date, 'jourstr');
jour = ET.SubElement(date, 'jour');
mois = ET.SubElement(date, 'mois');
annee = ET.SubElement(date, 'annee');

total = ET.SubElement(root, 'total');


medocs = ET.SubElement(root, 'medocs');

# Parse le texte dans le fichier res.txt
listLine = texte.split('\n')
print (listLine)

listLine = [string for string in listLine if string != ""]
print (listLine)

# Parse le nom et prennom
listNomPrenom = listLine[0].split(' ', 1)
print (listNomPrenom)
nom.text = listNomPrenom[1]
prenom.text = listNomPrenom[0]

# Parse l'adresse
#adresse.text = listLine[1]
listAdresse = listLine[1].split(' ', 2)

npa.text  = listAdresse[1]
rue.text = listAdresse[2]

# Parse la date
#time.text = listLine[2]
listTime = listLine[2].split(' ', 3)

jourstr.text = listTime[0]
heure_m.text = listTime[1].split(':', 1)[0]
minute_m.text = listTime[1].split(':', 1)[1]

jour.text = listTime[2].split('.', 2)[0]
mois.text = listTime[2].split('.', 2)[1]
annee.text = listTime[2].split('.', 2)[2]

# Parse le nombre total de medicament

indexTotal = texte.find('Total:') + 7
print(indexTotal)
index_num_str = texte[indexTotal]
print(index_num_str)

total_index = index_num_str
total.text = total_index

index_num = int(index_num_str, base=10)


# Parse tous les medicaments

quantite = [None] * index_num
nom = [None] * index_num
description = [None] * index_num

# Pour chaque medoc
while index_num > 0 :
	# Cree les balises xml
	medoc1 = ET.SubElement(medocs, 'medoc');
	quantite1 = ET.SubElement(medoc1, 'quantite');
	nom1 = ET.SubElement(medoc1, 'nom');
	description1 = ET.SubElement(medoc1, 'description');

	# Parse le texte
	indexList = 3+((index_num-1) *2)
	listMedoc = listLine[indexList].split(' ', 1)
        #quantite[index_num-1] = listMedoc[0]
	quantite1.text = listMedoc[0]
	nom1.text = listMedoc[1]
	description1.text = listLine[indexList+1]
	#print(quantite[index_num-1])
	#nom[index_num-1] = listMedoc[1]
	#print(nom[index_num-1])
	#description[index_num-1] = listLine[indexList+1]
	#print(description[index_num-1])
	index_num = index_num-1


# Cree le fichier xml 
tree = ET.ElementTree(root);
indent(root)
# writing xml
tree.write("res.xml", encoding="utf-8", xml_declaration=True)

# ferme le fichier de resultat OCR
f_in.close();

#print type(mylist)
#print mylist
#Nom = "ok"

