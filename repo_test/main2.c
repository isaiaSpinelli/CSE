
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	/* prend une photo avec la Pi Cam */
	printf("Prend une photo...\n");
	system("python takePhoto.py");
	printf("Photo ok !\n");  

	/* Execute le script python afin d’appliquer l'algorithme OCR 
	    et stocker le texte lu dans un fichier (res.txt) */
	printf("\nLecture des caracteres...\n"); 
	system("python ocr_arg.py picture.jpg");

	/* Parse le texte lu avec l'algo ocr (res.txt) dans un fichier res.xml */  
	printf("\nParsing... \n");
	system("python parse_res.py");
	printf("Fichier res.xml OK\n");


	printf("\nFin\n");

	return 0;
}
