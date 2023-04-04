import traitement_liste as tl
from os import system

choix =0
notes=[]
while choix !=7:
    system("cls")
    choix=int(input("\n1. Saisir\n2. Afficher\n3. Somme\n"
    + "4. Tri Croissant\n5. Inverser\n6. Max\n7. Quitter\nTapez votre choix ? "))
    if choix==1:
        n=int(input("Combien de notes voulez vous saisir ? "))
        tl.saisir(notes,n)
        
    elif choix==2:
        tl.afficherVertical(notes)
        system("pause")
        
    elif choix==3:
        print("La somme est :",tl.somme(notes))
        system("pause")
        
    elif choix==4:
       #tl.triCroissant(notes)
       notes.sort()
       tl.afficherVertical(notes)
       system("pause")
       
    elif choix==5:
       #tl.inverser(notes)
       notes=notes[::-1]
       tl.afficherVertical(notes)
       system("pause")
          
    elif choix==6:
        print("La plus grande note de la liste est :",tl.getMax(notes))
        system("pause")


    
