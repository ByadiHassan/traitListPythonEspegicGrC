import pickle
def saisir(liste,nbr):
    for i in range(nbr):
        liste.append(float(input("Tapez la note numéro "+str(i+1)+" : ")))

def afficherHoris(liste):
    for i in range(len(liste)):
        print(liste[i],end= "  ")

def afficherVertical(liste):
    for i in range(len(liste)):
        print(liste[i])

def afficher(items):
    for item in items:
        print(item)

def somme(items):
    s=0
    for item in items:
        s+=item
    return s
 
def triCroissant(items):
    for _ in range(len(items)-1):
        for i in range(len(items)-1):
            if items[i]>items[i+1]:
                items[i],items[i+1]=items[i+1],items[i]

def triCroissantV1(items):
    sorted=False
    while not sorted:
        sorted =True
        for i in range(len(items)-1):
            if items[i]>items[i+1]:
                items[i],items[i+1]=items[i+1],items[i]
                sorted=False

def inverser(items):
    for i in range(len(items)//2):
         items[i],items[-i-1]=items[-i-1],items[i]
def inverserV1(items):
    return items[::-1]
def getMax(items):
    m=items[0]
    for item in items:
        if item>m:
            m=item
    return m
def getMaxV1(items):
    m=items[0]
    for i in range(1,len(items)):
        if items[i]>m:
            m=items[i]
    return m
def getMin(items):
    m=items[0]
    for i in range(1,len(items)):
        if items[i]<m:
            m=items[i]
    return m

def getAdmis(items):
    admis=[]
    for item in items:
        if item>=10:
            admis.append(item)
    return admis
def getNonAdmis(items):
    admis=[]
    for item in items:
        if item<10:
            admis.append(item)
    return admis
def enregistrer(liste):
    fichier= open("notes.bin","wb")
    pickle.dump(liste,fichier)
    fichier.close()
def charger():
    fichier= open("notes.bin","rb")
    liste=pickle.load(fichier)
    fichier.close()
    return liste


if __name__=="__main__":
    print("Test des fonctions du module TraitementListe")
    print('Test de la fonction getAdmis')
    print("les notes sont :[10,12,3,15,7,19]","Les admis sont :",getAdmis([10,12,3,15,7,19]))
    print('Test de la fonction getNonAdmis')
    print("les notes sont :[10,12,3,15,7,19]","Les non admis sont :",getNonAdmis([10,12,3,15,7,19]))

