# mercredi 11/02/2017  21:35
"""
    une version textuelle du jeu de démineur
    la taille de grille est 8x8
    nombre de mines est 10
"""
from random import randint

#défintion de la grille
grilleJoueur=['0' for x in range(64)] #grille à afficher au joueur
grilleCachee=['0' for x in range(64)] #grille réelle contenant les mines

#affichage de grille
def afficherGrille(l):
    s=''
    for i in range(64):
        s+=str(l[i])+'  '
        if (i+1)%8==0:
            s+='\n'
    print (s)
#générer aléatoirement les mines placées  la grille caché :
for x in range(11):
    grilleCachee[randint(0,63)]='¤'
#placés les nombres des mines dans la grille caché :
for i in range(64):
    if grilleCachee[i]!='¤' and i>7 and i<56 and i%8!=0 and (i+1)%8!=0 :
        c=0
        if 0<=i+1 and i+1<=63 :
            if grilleCachee[i+1]=='¤': c=c+1
        if 0<=i-1 and i-1<=63 :
            if grilleCachee[i-1]=='¤': c=c+1
        if 0<=i+7 and i+7<=63 :
            if grilleCachee[i+7]=='¤': c=c+1
        if 0<=i+8 and i+8<=63 :
            if grilleCachee[i+8]=='¤': c=c+1
        if 0<=i+9 and i+9<=63 :
            if grilleCachee[i+9]=='¤': c=c+1
        if 0<=i-7 and i-7<=63 :
            if grilleCachee[i-7]=='¤': c=c+1
        if 0<=i-8 and i-8<=63 :
            if grilleCachee[i-8]=='¤': c=c+1
        if 0<=i-9 and i-9<=63 :
            if grilleCachee[i-9]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and (i+1)%8==0 and i>7 and i<56 :
        c=0
        if 0<=i-1 and i-1<=63 :
            if grilleCachee[i-1]=='¤': c=c+1
        if 0<=i+7 and i+7<=63 :
            if grilleCachee[i+7]=='¤': c=c+1
        if 0<=i+8 and i+8<=63 :
            if grilleCachee[i+8]=='¤': c=c+1
        if 0<=i-7 and i-7<=63 :
            if grilleCachee[i-8]=='¤': c=c+1
        if 0<=i-9 and i-9<=63 :
            if grilleCachee[i-9]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and i%8==0  and i>7 and i<56 :
        c=0
        if 0<=i+1 and i+1<=63 :
            if grilleCachee[i+1]=='¤': c=c+1
        if 0<=i+8 and i+8<=63 :
            if grilleCachee[i+8]=='¤': c=c+1
        if 0<=i+9 and i+9<=63 :
            if grilleCachee[i+9]=='¤': c=c+1
        if 0<=i-7 and i-7<=63 :
            if grilleCachee[i-7]=='¤': c=c+1
        if 0<=i-8 and i-8<=63 :
            if grilleCachee[i-8]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and i in[57,58,59,60,61,62]:
        c=0
        if 0<=i+1 and i+1<=63 :
            if grilleCachee[i+1]=='¤': c=c+1
        if 0<=i-1 and i-1<=63 :
            if grilleCachee[i-1]=='¤': c=c+1
        if 0<=i-7 and i-7<=63 :
            if grilleCachee[i-7]=='¤': c=c+1
        if 0<=i-8 and i-8<=63 :
            if grilleCachee[i-8]=='¤': c=c+1
        if 0<=i-9 and i-9<=63 :
            if grilleCachee[i-9]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and i in[1,2,3,4,5,6]:
        c=0
        if 0<=i+1 and i+1<=63 :
            if grilleCachee[i+1]=='¤': c=c+1
        if 0<=i-1 and i-1<=63 :
            if grilleCachee[i-1]=='¤': c=c+1
        if 0<=i+7 and i+7<=63 :
            if grilleCachee[i+7]=='¤': c=c+1
        if 0<=i+8 and i+8<=63 :
            if grilleCachee[i+8]=='¤': c=c+1
        if 0<=i+9 and i+9<=63 :
            if grilleCachee[i+9]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and i==0:
        c=0
        if 0<=i+1 and i+1<=63 :
            if grilleCachee[i+1]=='¤': c=c+1
        if 0<=i+8 and i+8<=63 :
            if grilleCachee[i+8]=='¤': c=c+1
        if 0<=i+9 and i+9<=63 :
            if grilleCachee[i+9]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and i==7:
        c=0
        if 0<=i-1 and i-1<=63 :
            if grilleCachee[i-1]=='¤': c=c+1
        if 0<=i+8 and i+8<=63 :
            if grilleCachee[i+8]=='¤': c=c+1
        if 0<=i+7 and i+7<=63 :
            if grilleCachee[i+7]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and i==56:
        c=0
        if 0<=i+1 and i+1<=63 :
            if grilleCachee[i+1]=='¤': c=c+1
        if 0<=i-8 and i-8<=63 :
            if grilleCachee[i-8]=='¤': c=c+1
        if 0<=i-7 and i-7<=63 :
            if grilleCachee[i-7]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
    if grilleCachee[i]!='¤' and i==63:
        c=0
        if 0<=i-1 and i-1<=63 :
            if grilleCachee[i-1]=='¤': c=c+1
        if 0<=i-8 and i-8<=63 :
            if grilleCachee[i-8]=='¤': c=c+1
        if 0<=i-9 and i-9<=63 :
            if grilleCachee[i-9]=='¤': c=c+1
        if c!=0: grilleCachee[i]=str(c)
afficherGrille(grilleJoueur)      
variable=True
m=64
while variable==True and m>1  :
    lin = int(input("entrez le numéro de ligne: "))
    col = int(input("entrez le numéro de colonne : "))
    indice=8*(lin-1)+col-1
    if grilleCachee[indice]=='0':
        grilleJoueur[indice]='.'
        par=1
        while par<8: #8 parcours est suffisant pour 8x8
            for i in range(64):
                if grilleJoueur[i]=='.'and i%8!=0 and (i+1)%8!=0  and i>7 and i<56 :
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]=='0': grilleJoueur[i+1]='.'
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]=='0': grilleJoueur[i-1]='.'
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]=='0': grilleJoueur[i+7]='.'
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]=='0': grilleJoueur[i+8]='.'
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]=='0': grilleJoueur[i+9]='.'
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]=='0': grilleJoueur[i-7]='.'
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]=='0': grilleJoueur[i-8]='.'
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]=='0': grilleJoueur[i-9]='.'
                            
                elif grilleJoueur[i]=='.' and (i+1)%8==0 and i>7 and i<56 :
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]=='0': grilleJoueur[i-1]='.'
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]=='0': grilleJoueur[i+7]='.'
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]=='0': grilleJoueur[i+8]='.'
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]=='0': grilleJoueur[i-8]='.'
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]=='0': grilleJoueur[i-9]='.'

                elif grilleJoueur[i]=='.' and i%8==0  and i>7 and i<56 :
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]=='0': grilleJoueur[i+1]='.'
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]=='0': grilleJoueur[i+8]='.'
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]=='0': grilleJoueur[i+9]='.'
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]=='0': grilleJoueur[i-7]='.'
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]=='0': grilleJoueur[i-8]='.'

                elif grilleJoueur[i]=='.' and  i in[57,58,59,60,61,62] :
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]=='0': grilleJoueur[i+1]='.'
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]=='0': grilleJoueur[i-1]='.'
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]=='0': grilleJoueur[i-7]='.'
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]=='0': grilleJoueur[i-8]='.'
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]=='0': grilleJoueur[i-9]='.'
                elif grilleJoueur[i]=='.' and  i in[1,2,3,4,5,6]:
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]=='0': grilleJoueur[i+1]='.'
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]=='0': grilleJoueur[i-1]='.'
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]=='0': grilleJoueur[i+7]='.'
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]=='0': grilleJoueur[i+8]='.'
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]=='0': grilleJoueur[i+9]='.'                        
                elif grilleJoueur[i]=='.' and i==0:
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]=='0': grilleJoueur[i+1]='.'
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]=='0': grilleJoueur[i+8]='.'
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]=='0': grilleJoueur[i+9]='.'
                elif grilleJoueur[i]=='.' and i==7:
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]=='0': grilleJoueur[i-1]='.'
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]=='0': grilleJoueur[i+7]='.'
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]=='0': grilleJoueur[i+8]='.'
                elif grilleJoueur[i]=='.' and i==56:
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]=='0': grilleJoueur[i+1]='.'
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]=='0': grilleJoueur[i-7]='.'
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]=='0': grilleJoueur[i-8]='.'
                elif grilleJoueur[i]=='.' and i==63:
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]=='0': grilleJoueur[i-1]='.'
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]=='0': grilleJoueur[i-8]='.'
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]=='0': grilleJoueur[i-9]='.'
            par=par+1
        par2=0
        while par2<8:
            for i in range(64):
                if grilleJoueur[i]=='.'and i%8!=0 and (i+1)%8!=0  and i>7 and i<56 :
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]!='¤'and grilleCachee[i+1]!='0': grilleJoueur[i+1]=grilleCachee[i+1]
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]!='¤'and grilleCachee[i-1]!='0': grilleJoueur[i-1]=grilleCachee[i-1]
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]!='¤'and grilleCachee[i+7]!='0': grilleJoueur[i+7]=grilleCachee[i+7]
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]!='¤'and grilleCachee[i+8]!='0': grilleJoueur[i+8]=grilleCachee[i+8]
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]!='¤'and grilleCachee[i+9]!='0': grilleJoueur[i+9]=grilleCachee[i+9]
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]!='¤'and grilleCachee[i-7]!='0': grilleJoueur[i-7]=grilleCachee[i-7]
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]!='¤'and grilleCachee[i-8]!='0': grilleJoueur[i-8]=grilleCachee[i-8]
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]!='¤'and grilleCachee[i-9]!='0': grilleJoueur[i-9]=grilleCachee[i-9]
                            
                elif grilleJoueur[i]=='.' and (i+1)%8==0 and i>7 and i<56 :
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]!='¤'and grilleCachee[i-1]!='0': grilleJoueur[i-1]=grilleCachee[i-1]
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]!='¤'and grilleCachee[i+7]!='0': grilleJoueur[i+7]=grilleCachee[i+7]
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]!='¤'and grilleCachee[i+8]!='0': grilleJoueur[i+8]=grilleCachee[i+8]
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]!='¤'and grilleCachee[i-8]!='0': grilleJoueur[i-8]=grilleCachee[i-8]
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]!='¤'and grilleCachee[i-9]!='0': grilleJoueur[i-9]=grilleCachee[i-9]

                elif grilleJoueur[i]=='.' and i%8==0  and i>7 and i<56 :
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]!='¤'and grilleCachee[i+1]!='0': grilleJoueur[i+1]=grilleCachee[i+1]
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]!='¤'and grilleCachee[i+8]!='0': grilleJoueur[i+8]=grilleCachee[i+8]
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]!='¤'and grilleCachee[i+9]!='0': grilleJoueur[i+9]=grilleCachee[i+9]
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]!='¤'and grilleCachee[i-7]!='0': grilleJoueur[i-7]=grilleCachee[i-7]
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]!='¤'and grilleCachee[i-8]!='0': grilleJoueur[i-8]=grilleCachee[i-8]

                elif grilleJoueur[i]=='.' and  i in[57,58,59,60,61,62] :
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]!='¤'and grilleCachee[i+1]!='0': grilleJoueur[i+1]=grilleCachee[i+1]
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]!='¤'and grilleCachee[i-1]!='0': grilleJoueur[i-1]=grilleCachee[i-1]
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]!='¤'and grilleCachee[i-7]!='0': grilleJoueur[i-7]=grilleCachee[i-7]
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]!='¤'and grilleCachee[i-8]!='0': grilleJoueur[i-8]=grilleCachee[i-8]
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]!='¤'and grilleCachee[i-9]!='0': grilleJoueur[i-9]=grilleCachee[i-9]
                elif grilleJoueur[i]=='.' and  i in[1,2,3,4,5,6]:
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]!='¤'and grilleCachee[i+1]!='0': grilleJoueur[i+1]=grilleCachee[i+1]
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]!='¤'and grilleCachee[i-1]!='0': grilleJoueur[i-1]=grilleCachee[i-1]
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]!='¤'and grilleCachee[i+7]!='0': grilleJoueur[i+7]=grilleCachee[i+7]
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]!='¤'and grilleCachee[i+8]!='0': grilleJoueur[i+8]=grilleCachee[i+8]
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]!='0'and grilleCachee[i+9]!='0': grilleJoueur[i+9]=grilleCachee[i+9]                     
                elif grilleJoueur[i]=='.' and i==0:
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]!='¤'and grilleCachee[i+1]!='0': grilleJoueur[i+1]=grilleCachee[i+1]
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]!='¤'and grilleCachee[i+8]!='0': grilleJoueur[i+8]=grilleCachee[i+8]
                    if 0<=i+9 and i+9<=63 :
                        if grilleCachee[i+9]!='¤'and grilleCachee[i+9]!='0': grilleJoueur[i+9]=grilleCachee[i+9]
                elif grilleJoueur[i]=='.' and i==7:
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]!='¤'and grilleCachee[i-1]!='0': grilleJoueur[i-1]=grilleCachee[i-1]
                    if 0<=i+7 and i+7<=63 :
                        if grilleCachee[i+7]!='¤'and grilleCachee[i+7]!='0': grilleJoueur[i+7]=grilleCachee[i+7]
                    if 0<=i+8 and i+8<=63 :
                        if grilleCachee[i+8]!='¤'and grilleCachee[i+8]!='0': grilleJoueur[i+8]=grilleCachee[i+8]
                elif grilleJoueur[i]=='.' and i==56:
                    if 0<=i+1 and i+1<=63 :
                        if grilleCachee[i+1]!='¤'and grilleCachee[i+1]!='0': grilleJoueur[i+1]=grilleCachee[i+1]
                    if 0<=i-7 and i-7<=63 :
                        if grilleCachee[i-7]!='¤'and grilleCachee[i-7]!='0': grilleJoueur[i-7]=grilleCachee[i-7]
                    if 0<=i-8 and i-8<=63 : 
                        if grilleCachee[i-8]!='¤'and grilleCachee[i-8]!='0': grilleJoueur[i-8]=grilleCachee[i-8]
                elif grilleJoueur[i]=='.' and i==63:
                    if 0<=i-1 and i-1<=63 :
                        if grilleCachee[i-1]!='¤'and grilleCachee[i-1]!='0': grilleJoueur[i-1]=grilleCachee[i-1]
                    if 0<=i-8 and i-8<=63 :
                        if grilleCachee[i-8]!='¤'and grilleCachee[i-8]!='0': grilleJoueur[i-8]=grilleCachee[i-8]
                    if 0<=i-9 and i-9<=63 :
                        if grilleCachee[i-9]!='¤'and grilleCachee[i-9]!='0': grilleJoueur[i-9]=grilleCachee[i-9]
            par2=par2+1                    
    if grilleCachee[indice]!='¤' and grilleCachee[indice]!='0':
        grilleJoueur[indice]=grilleCachee[indice]
    if grilleCachee[indice]=='¤':
        variable=False
        grilleJoueur[indice]=grilleCachee[indice]
    m=grilleJoueur.count('0')
    afficherGrille(grilleJoueur)
if variable==False :
    print("vous avez perdu ....... :(")
if variable==True :
    print("bravoooooo,vous avez gagné")
a=input("appuyer sur une touche pour terminer :)")
# mercredi 11/02/2017  1:35

























                 



