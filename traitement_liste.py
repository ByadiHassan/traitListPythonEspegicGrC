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