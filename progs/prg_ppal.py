
if __name__=="__main__":

    from sys import path
    from os import system
    system('cls')
    path.append(".\\modules")    
    '''
    system('cls')
    for p in path:
        print(p)
    system('pause') 
    '''
    #path.append("D:\\Espegic\\Tsdi1\\groupe_c\\gestion_notes\\modules")

    import pack.traitement_liste as tl


    choix =0
    notes=[]
    while choix !=9:
        #system("cls")
        choix=int(input("\n1. Saisir\n2. Afficher\n3. Somme\n"
        + "4. Tri Croissant\n5. Inverser\n6. Max\n7. Admis\n8. NonAdmis\n9. Quitter\nTapez votre choix ? "))
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
            tl.triCroissant(notes)
            #notes.sort()
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
        elif choix==7:
            tl.afficherHoris(tl.getAdmis(notes))
            system("pause")
        elif choix==8:
            tl.afficherHoris(tl.getNonAdmis(notes))
            system("pause")

        
