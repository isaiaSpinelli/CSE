import cv2 
import pytesseract

import os
import sys

# Chemin de l'image de base
fn = "image_sans_bord_grayscale.PNG"

# Recupere le chemin de l'image en argument
if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    print("Warning ! : need arg (par defaut take : image_sans_bord_grayscale.PNG\r\n")
	
# recupere l'image
img_cv = cv2.imread(fn)

# transforme l'image en image rgb
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

# Lis les caracteres
texte = pytesseract.image_to_string(img_rgb)
# Affiche le resutlat
print("ALGO OCR RESULTAT :\n")
print("--------------------------\n");
print(texte)
print("--------------------------\n");

# Ouvre et ecris le resultat dans le fichier res.txt
f = open("res.txt","w+")
texte2 = texte.encode('utf-8').strip()
f.write(texte2);
f.close();

