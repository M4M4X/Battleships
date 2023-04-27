# -*- coding: utf-8 -*-
#
# Fichier des fonctions du programme principale
# Mai 2021
# Auteurs : Maxime Innocenti & Antoine Henriet
# Version : 2.0
#
from random import *
from math import *
import PySimpleGUI as sg

#---Informations contenu jeu---#

armadaUt = {
    "pa" : {"Nom" : "Porte-avion (5 cases)", "Bateaux" : 1, "Place" : False, "Cases" : 5, "Coulé" : False, "Position" : [""]*5, "Position_fixe" : [""]*5},
    "c" : {"Nom" : "Croiseur (4 cases)", "Bateaux" : 1, "Place" : False, "Cases" : 4, "Coulé" : False, "Position" : [""]*4, "Position_fixe" : [""]*4},
    "ct1" : {"Nom" : "Contre-torpilleurs 1 (3 cases)", "Bateaux" : 1, "Place" : False, "Cases" : 3, "Coulé" : False,"Position" : [""]*3, "Position_fixe" : [""]*3},
    "ct2" : {"Nom" : "Contre-torpilleurs 2 (3 cases)", "Bateaux" : 1, "Place" : False, "Cases" : 3, "Coulé" : False,"Position" : [""]*3, "Position_fixe" : [""]*3},
    "sm" : {"Nom" : "Sous-marin (2 cases)", "Bateaux" : 1, "Place" : False, "Cases" : 2, "Coulé" : False, "Position" : [""]*2, "Position_fixe" : [""]*2}
    }

armadaOrd = {
    "pa" : {"Nom" : "Porte-avion", "Bateaux" : 1, "Cases" : 5, "Coulé" : False, "Position" : [""]*5, "Position_fixe" : [""]*5},
    "c" : {"Nom" : "Croiseur", "Bateaux" : 1, "Cases" : 4, "Coulé" : False, "Position" : [""]*4, "Position_fixe" : [""]*4},
    "ct1" : {"Nom" : "Contre-torpilleurs 1", "Bateaux" : 1, "Cases" : 3, "Coulé" : False,"Position" : [""]*3, "Position_fixe" : [""]*3},
    "ct2" : {"Nom" : "Contre-torpilleurs 2", "Bateaux" : 1, "Cases" : 3, "Coulé" : False,"Position" : [""]*3, "Position_fixe" : [""]*3},
    "sm" : {"Nom" : "Sous-marin", "Bateaux" : 1, "Cases" : 2, "Coulé" : False, "Position" : [""]*2, "Position_fixe" : [""]*2}
    }

colonnes = ["A","B","C","D","E","F","G","H","I","J"]
lignes = ["1","2","3","4","5","6","7","8","9","10"]
listeBateau = []

#---Fonctions Bataille Navale---#

def Appel (window,window1,armada):
    """
    Cette fonction permet à l'utilisateur de placer ses bateaux.
    Pour cela on lui demande de choisir le bateau à poser, 
    puis la case de départ et d'arrivée.

    Parameters
    ----------
    window : Fenêtre graphique principale
        Permet de récuperer le bouton sur lequel l'utilisateur clique.
    window1 : Fenêtre graphique choix des bateaux
        Permet de récuperer le bateau que l'utilisateur veut placer.
    armada : Dictionnaire
        Correspond à l'inventaire des bateaux de l'utilisateur.

    Returns
    -------
    armadaUt : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur.
    choix_bateau : Chaines de caractères
        Contient le nom du bateau choisi par l'utilisateur.
    case_depart : Tuple
        Contient les coordonnées de la case de départ.
    case_arrivee : Tuple
        Contient les coordonnées de la case d'arrivée.

    """
        #CHOIX BATEAU
    listeBateau.clear()
    for element in armadaUt.keys():
        if armadaUt[element]["Place"] == False: 
            listeBateau.append(armadaUt[element]["Nom"])
        
    window1["-LISTEBATEAU-"].Update(listeBateau)
    window1.un_hide()
    selectionne = True
    while selectionne == True:
        event1,values1 = window1.read()
        if event1 == "-LISTEBATEAU-":    
            bateauChoisi = window1["-LISTEBATEAU-"].get()[0]
            for element in armadaUt.keys():
                if armadaUt[element]["Nom"] == bateauChoisi :
                    armadaUt[element]["Place"] = True
                    choix_bateau = element
                    selectionne = False
    window1.hide()
    print("\nPlacez votre",bateauChoisi)
    
    #CHOIX PLACEMENT BATEAU
    print("Cliquer sur la case de départ.")
    
    case_depart,bin = window.read()
    while case_depart[0] != "utilisateur":
        case_depart,bin = window.read()
        
    if window[(case_depart)].get_text() == "__":
        window[(case_depart)].update(button_color="grey50")

    print("Cliquer sur la case d'arrivée.")
    case_arrivee,bin = window.read()
    while case_arrivee[0] != "utilisateur":
        case_arrivee,bin = window.read()
    
    if window[(case_depart)].get_text() == "__":    
        window[(case_depart)].update(button_color="grey70")
        
    return armadaUt,choix_bateau,case_depart,case_arrivee

#==========
        
def Bateau(armada,choix_bateau,player):
    """
    Cette fonction permet de vérifier que le bateau choisi par l'utilisateur n'est pas déjà placé.

    Parameters
    ----------
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.
    choix_bateau : Chaines de caractères
        Contient le nom du bateau choisi par l'utilisateur.
    player : Chaines de caractères
        Cette variable permet de savoir si l'on doit afficher ou non des messages d'erreurs pour aider.
        Exemple si c'est au tour de l'ordinateur nous n'allons pas lui afficher de message d'erreur,
        contrairement au joueur.

    Returns
    -------
    bool
        Prends la valeur True si le bateau n'a pas déjà été placé, sinon il prend la valeur False.
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.

    """
    nb_bateau = armada[choix_bateau]["Bateaux"]
    if nb_bateau == 0 :
        return False, armada
    else :
        armada[choix_bateau]["Bateaux"]-=1
        return True, armada

#==========

def Simulation (window,armada,choix_bateau,case_depart,case_arrivee,player):
    """
    Cette fonction permet de vérifier le placement du bateau
    (la taille est respectée, direction possible, grille selctionnée est bonne).
    Si ce n'est pas le cas, alors la fonction renvoie False.

    Parameters
    ----------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique.
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.
    choix_bateau : Chaines de caractères
        Contient le nom du bateau choisi par l'utilisateur.
    case_depart : Tuple
        Contient les coordonnées de la case de départ.
    case_arrivee : Tuple
        Contient les coordonnées de la case d'arrivée.
    player : Chaines de caractères
        Cette variable permet de savoir si l'on doit afficher ou non des messages d'erreurs pour aider.
        Exemple si c'est au tour de l'ordinateur nous n'allons pas lui afficher de message d'erreur,
        contrairement au joueur.

    Returns
    -------
    bool
        Prends la valeur True si l'utilisateur a bien respecté le placement du bateau (nombre de case,direction,grille),
        sinon il prends la valeur False.

    """
    taille_b = armada[choix_bateau]["Cases"]-1 #On enlève 1 car la première case est déjà comptée
    grille_depart = case_depart[0]
    grille_arrivee = case_arrivee[0]
    
    if player == "utilisateur":
        if grille_depart == grille_arrivee == "utilisateur": #Verifie le placement dans la bonne grille
            if (case_depart[1] == case_arrivee[1]) or (case_depart[2] == case_arrivee[2]): #Verifie que le bateau n'est pas en diagonale
                if (abs(int(case_depart[1])-int(case_arrivee[1]))==taille_b) or (abs(int(case_depart[2])-int(case_arrivee[2]))==taille_b): #Verifie que le nombre de case pour la taille du bateau est respecté
                    return True
                else:
                    print("Vous n'avez pas choisis le bon nombre de case pour votre bateau.")
                    return False
            else:
                print("Votre bateau ne peut pas être placé en diagonale!")
                return False
        else:
            print("Votre bateau doit être placé dans la grille de gauche!")
            return False
    else:
        if (case_depart[1] == case_arrivee[1]) or (case_depart[2] == case_arrivee[2]): #Verifie que le bateau n'est pas en diagonale
            if (abs(int(case_depart[1])-int(case_arrivee[1]))==taille_b) or (abs(int(case_depart[2])-int(case_arrivee[2]))==taille_b): #Verifie que le nombre de case pour la taille du bateau est respecté
                return True
            else:
                return False
        else :
            return False

#==========

def Occupation(window,armada,choix_bateau,case_depart,case_arrivee,player):
    """
    Cette fonction permet de vérifier que le bateau placé ne chevauche ni ne touche un autre bateau.

    Parameters
    ----------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique.
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.
    choix_bateau : Chaines de caractères
        Contient le nom du bateau choisi par l'utilisateur.
    case_depart : Tuple
        Contient les coordonnées de la case de départ.
    case_arrivee : Tuple
        Contient les coordonnées de la case d'arrivée.
    player : Chaines de caractères
        Cette variable permet de savoir si l'on doit afficher ou non des messages d'erreurs pour aider.
        Exemple si c'est au tour de l'ordinateur nous n'allons pas lui afficher de message d'erreur,
        contrairement au joueur.

    Returns
    -------
    bool
        Prends la valeur False si la bateau touche/ est posé sur un autre bateau, sinon prends la valeur True.
    armada : Dictionnaire
        Contient maintenant les coordonnées du bateau en plus.

    """
    nb_case = armada[choix_bateau]["Cases"]-1        
            
    #Recupere les coordonnées dans des variables
    ligne_dep = int(case_depart[1])
    ligne_arr = int(case_arrivee[1])
    colonne_dep = int(case_depart[2])
    colonne_arr = int(case_arrivee[2])
    
    if ligne_dep == ligne_arr: #Pour savoir le bateau est horizontal (même ligne)
        #Mettre la plus petite coordonnee en premier pour faciliter l'utilisation du for 
        if colonne_dep>colonne_arr: #On ne change pas les lignes car elles sont égales
            switch = colonne_dep
            colonne_dep = colonne_arr
            colonne_arr = switch
        
        for i in range (ligne_dep-1, ligne_dep+2): 
            for j in range(colonne_dep-1, colonne_arr+2):
                if i<1 or i>10 or j<1 or j>10:
                    continue
                if  window[(player,i,j)].get_text() != "__":
                    if player == "utilisateur":
                        print("\nVotre bateau croise/touche un autre bateau!\nVeuillez recommencer :\n")
                    return False, armada
        return True, armada
                
    if colonne_dep == colonne_arr: #Pour savoir le bateau est vertical (même colonne)
        #Mettre la plus petite coordonnee en premier pour faciliter l'utilisation du for
        if ligne_dep>ligne_arr: #On ne change pas les colonnes car elles sont égales
            switch = ligne_dep
            ligne_dep = ligne_arr
            ligne_arr = switch
        
        for j in range (colonne_dep-1, colonne_dep+2): 
            for i in range(ligne_dep-1, ligne_arr+2):
                if i<1 or i>10 or j<1 or j>10:
                    continue
                if window[(player,i,j)].get_text() != "__":
                    if player == "utilisateur":
                        print("\nVotre bateau croise/touche un autre bateau!\nVeuillez recommencer :\n")
                    return False, armada
        return True, armada


#==========
        
def Placement(window,armada,choix_bateau,case_depart,case_arrivee,player):
    """
    Cette fonction permet de placer le bateau sur la grille.

    Parameters
    ----------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique.
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.
    choix_bateau : Chaines de caractères
        Contient le nom du bateau choisi par l'utilisateur.
    case_depart : Tuple
        Contient les coordonnées de la case de départ.
    case_arrivee : Tuple
        Contient les coordonnées de la case d'arrivée.
    player : Chaines de caractères
        Cette variable permet de savoir si l'on doit afficher ou non des messages d'erreurs pour aider.
        Exemple si c'est au tour de l'ordinateur nous n'allons pas lui afficher de message d'erreur,
        contrairement au joueur.

    Returns
    -------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique.
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.

    """
    nb_case = armada[choix_bateau]["Cases"]
    tab = armada[choix_bateau]["Position"]
    tab_fixe = armada[choix_bateau]["Position_fixe"]
    
    #Recupere les coordonnées dans des variables
    ligne_dep = int(case_depart[1])
    ligne_arr = int(case_arrivee[1])
    colonne_dep = int(case_depart[2])
    colonne_arr = int(case_arrivee[2])
    
    if ligne_dep == ligne_arr : #Bateau à l'horizontal
        if colonne_dep > colonne_arr:
            switch = colonne_dep
            colonne_dep = colonne_arr
            colonne_arr = switch
        for i in range(colonne_dep,colonne_arr+1):
            window[(player,int(ligne_dep),i)].update(text=(choix_bateau.upper()),button_color=("CadetBlue"))
            tab[i-colonne_dep]= [str(ligne_dep),str(i)]
            tab_fixe[i-colonne_dep]= [str(ligne_dep),str(i)]
            
    if colonne_dep == colonne_arr : #Bateau à la vertical
        if ligne_dep > ligne_arr:
            switch = ligne_dep
            ligne_dep = ligne_arr
            ligne_arr = switch
        for i in range(ligne_dep,ligne_arr+1):
            window[(player,i,int(colonne_dep))].update(text=(choix_bateau.upper()),button_color=("CadetBlue"))
            tab[i-ligne_dep]= [str(i),str(colonne_dep)]
            tab_fixe[i-ligne_dep]= [str(i),str(colonne_dep)]

    return window, armada
   
#---Fonctions Ordinateurs---#

def AppelOrdinateur(armada):
    """
    Cette fonction permet de donner un type de bateau, une case de départ et une case d'arrivée de manière automatique.
    La fonction est utilisée pour l'ordinateur.

    Parameters
    ----------
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.

    Returns
    -------
    armadaUt : Dictionnaire
        Contient toutes les informations sur l'armada de l'ordinateur.
    choix_bateau : Chaines de caractères
        Contient le nom du bateau choisi par l'ordinateur.
    case_depart : Tuple
        Contient les coordonnées de la case de départ.
    case_arrivee : Tuple
        Contient les coordonnées de la case d'arrivée.

    """
        #CHOIX BATEAU
    choix_bateau = ['pa', 'c', 'ct1', "ct2", 'sm'][randint(0,4)]
    
    if armada[choix_bateau]["Bateaux"] == 0 :
        return armada,choix_bateau,None,None
    else:
        #CHOIX PLACEMENT BATEAU
        case_depart1 = randint(1,10)
        case_depart2 = randint(1,10)
        case_depart = ["tirs",case_depart1,case_depart2] 
        
        case_arrivee1 = randint(1,10)
        case_arrivee2 = randint(1,10)
        case_arrivee = ["tirs",case_arrivee1,case_arrivee2] 
        
        return armada,choix_bateau,case_depart,case_arrivee
    
#---Fonctions Attaque---#

def TirUt(window,window2,score):
    """
    Cette fonction permet à l'utilisateur de tirer sur la grille de l'ordinateur.
    Elle renvoie si le tir est 'Raté'/'Touché'/'Coulé', et modifie le score de l'utilisateur en fonction des cas.

    Parameters
    ----------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique dont la grille de tirs.
    window2 : Fenêtre graphique secondaire
        Permet de stocker et afficher les informations sur la position des bateaux de l'ordinateur.
    score : Entier
        Cette variable contient le score.

    Returns
    -------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique.
    window2 : Fenêtre graphique secondaire
        Permet de stocker et afficher les informations sur la position des bateaux de l'ordinateur.
    score : Entier
        Cette variable contient le score.
    str
        Renvoie une chaine de caractère qui indique qui doit être la prochaine personne à jouer.

    """     
    i=0    
    case_tir,bin = window.read()
    while case_tir[0] not in ["tirs"]:
        if case_tir in ["Afficher Bateaux Ennemis","Masquer Bateaux Ennemis","Règles du jeu","A propos","Exit",sg.WIN_CLOSED]:
            if case_tir == "A propos":
                sg.Popup("Version : 2.0 de Mai 2021","Auteurs : Maxime Innocenti - Antoine Henriet")
            if case_tir == "Règles du jeu":
                sg.Popup("Règle de la Bataille Navale :","- Début de la partie :","La bataille navale oppose deux joueurs qui s'affrontent.",
                     "Au début du jeu, chaque joueur place ses bateaux sur sa grille. Celle-ci est toujours numérotée de 1 à 10 verticalement et de A à J horizontalement."
                     "Chacun a une flotte composée de 5 bateaux, qui sont les suivants : 1 porte-avion (5 cases), 1 croiseur (4 cases), 2 contre-torpilleurs (3 cases), 1 sous-marin (2 cases).",
                     "Les bateaux ne doivent pas être collés entre eux.",
                     "","- Déroulement de la partie :","Un à un, les joueurs vont « tirer » sur une case de l'adversaire : par exemple, B3 ou encore H8.",
                     "","- But du jeu :","Le but du jeu est de couler tous les bateaux ennemis !",
                     "","- Fin de la partie :","La partie se termine quand un des deux joueurs n'a plus de bateaux, ou alors n'a plus de points pour tirer.")
            if case_tir == "Afficher Bateaux Ennemis":
                window2.un_hide()
            if case_tir == "Masquer Bateaux Ennemis":
                window2.hide()
            if case_tir in [sg.WIN_CLOSED,"Exit"]:
                window2.close()
                window.close()
                exit()
        else:
            if i<0:
                print("ERREUR !\nTirez sur la grille de tirs!")
                i+=1
        case_tir,bin = window.read()

    coordonnées = [str(case_tir[1]),str(case_tir[2])] 
    type_bateau = window2[("ordinateur",case_tir[1],case_tir[2])].get_text().lower()
       
    if window2[("ordinateur",case_tir[1],case_tir[2])].get_text() == "__":
        window[(case_tir)].update(text=("X"),button_color=("grey40"))
        score-=1
        return window,window2,score,"ordinateur"
    
    if window2[("ordinateur",case_tir[1],case_tir[2])].get_text() in ["X","PA.","C.","CT1.","CT2.","SM."]:
        print("\nVous avez déjà tiré ici!\nDommage,c'est au tour de l'ordinateur.")
        score-=1
        return window,window2,score,"ordinateur"
    
    if window2[("ordinateur",case_tir[1],case_tir[2])].get_text() in ["PA","C","CT1","CT2","SM"]:
        for i in range (len(armadaOrd[type_bateau]["Position"])):
            if armadaOrd[type_bateau]["Position"][i] == coordonnées:
                score+=1
                armadaOrd[type_bateau]["Position"][i] = ""

                window[(case_tir)].update(text=("!"),button_color=("orange red"))
                break
        
        if armadaOrd[type_bateau]["Position"] == [""]*armadaOrd[type_bateau]["Cases"]:
            sg.Popup("Coulé !")
            score+=armadaOrd[type_bateau]["Cases"]*2
            armadaOrd[type_bateau]["Coulé"] = True
        
        return window,window2,score,"utilisateur"

#==========

def TirOrd(window,window2,score,scoreUt,tirs, case, chasse):
    """
    Cette fonction permet à l'ordinateur de tirer sur la grille de l'utilisateur en modifiant le score de l'utilisateur si il triche,
    et le score de l'ordinateur en fonction de si il 'Rate'/'Touche'/'Coule' les bateaux de l'utilisateur.

    Parameters
    ----------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique dont la grille de l'utilisateur.
    window2 : Fenêtre graphique secondaire
        Permet de stocker et afficher les informations sur la position des bateaux de l'ordinateur.
    score : Entier
        Cette variable contient le score de l'ordinateur.
    scoreUt : Entier
        Cette variable contient le score de l'utilisateur.
    tirs : Liste
        Cette liste contient l'historique des tirs de l'ordinateur pour qu'il ne tire pas deux fois au même endroit.
    case : Liste
        Contient les coordonnées du tr de l'ordinateur.
    chasse :Booleen
        Cette variable renvoie vrai si l'ordinateur a touché un bateau et il passe alors en mode chasse jusqu'à ce que le bateau soit coulé.
    
    Returns
    -------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique.
    score : Entier
        Cette variable contient le score de l'ordinateur.
    scoreUt : Entier
        Cette variable contient le score de l'utilisateur.
    str
        Renvoie une chaine de caractère qui indique qui doit être la prochaine personne à jouer.
    tirs : Liste
        Cette liste contient l'historique des tirs de l'ordinateur pour qu'il ne tire pas deux fois au même endroit.
    Touche : Booleen
        Cette variable renvoie vrai si l'ordinateur a touché un bateau ou renvoie faux sinon.
    Coule : Booleen
        Cette variable renvoie vrai si l'ordinateur a coulé un bateau ou renvoie faux sinon.
    chasse : Booleen
        Cette variable renvoie vrai si l'ordinateur a touché un bateau et il passe alors en mode chasse jusqu'à ce que le bateau soit coulé.
    """
    Touche = False
    Coule = False
    tirs.append(case)
    coordonnees = [str(case[0]),str(case[1])]
    print("\nL'ordinateur tire en",chr(ord('A')+int(case[1])-1)+str(case[0]),"\nIndiquez si c'est touché ou non ?")
    
    case_tirs = ("utilisateur",int(case[0]),int(case[1]))
    type_bateau = window[(case_tirs)].get_text().lower()
    window[(case_tirs)].update(button_color=("gold"))
    
    #Verifie que l'utilisateur appuie sur un des deux boutons
    i=0
    reponse,bin = window.read()
    while reponse not in ["Touché","Raté"]:
        if reponse in ["Afficher Bateaux Ennemis","Masquer Bateaux Ennemis","Règles du jeu","A propos","Exit",sg.WIN_CLOSED]:
            if reponse == "A propos":
                sg.Popup("Version : 2.0 de Mai 2021","Auteurs : Maxime Innocenti - Antoine Henriet")
            if reponse == "Règles du jeu":
                sg.Popup("Règle de la Bataille Navale :","- Début de la partie :","La bataille navale oppose deux joueurs qui s'affrontent.",
                     "Au début du jeu, chaque joueur place ses bateaux sur sa grille. Celle-ci est toujours numérotée de 1 à 10 verticalement et de A à J horizontalement."
                     "Chacun a une flotte composée de 5 bateaux, qui sont les suivants : 1 porte-avion (5 cases), 1 croiseur (4 cases), 2 contre-torpilleurs (3 cases), 1 sous-marin (2 cases).",
                     "Les bateaux ne doivent pas être collés entre eux.",
                     "","- Déroulement de la partie :","Un à un, les joueurs vont « tirer » sur une case de l'adversaire : par exemple, B3 ou encore H8.",
                     "","- But du jeu :","Le but du jeu est de couler tous les bateaux ennemis !",
                     "","- Fin de la partie :","La partie se termine quand un des deux joueurs n'a plus de bateaux, ou alors n'a plus de points pour tirer.")
            if reponse == "Afficher Bateaux Ennemis":
                window2.un_hide()
            if reponse == "Masquer Bateaux Ennemis":
                window2.hide()
            if reponse in [sg.WIN_CLOSED,"Exit"]:
                window2.close()
                window.close()
                exit()
        else:
            if i<0:
                print("\nCliquez uniqument sur soit 'Touché', soit 'Raté'!\n")
                i+=1
        reponse,bin = window.read()
    
    if window[(case_tirs)].get_text() == "__":
        if reponse == "Touché": #Verifie si l'utilisateur ne triche pas
            sg.Popup("Vous avez triché ! Il n'y a pas de bateau sur cette case.\nVous perdez 10 points.")
            scoreUt-=10
        
        window[(case_tirs)].update(text=("X"),button_color=("grey40"))
        score-=1
        return window,score,scoreUt,"utilisateur",tirs, Touche, Coule, chasse
    
    if window[(case_tirs)].get_text() in ["PA","C","CT1","CT2","SM"]:
        if reponse == "Raté": #Verifie si l'utilisateur ne triche pas
            sg.Popup("Vous avez triché ! Il a un bateau sur cette case.\nVous perdez 10 points.")
            scoreUt-=10
            
        for i in range (len(armadaUt[type_bateau]["Position"])):
            if armadaUt[type_bateau]["Position"][i] == coordonnees:
                score+=1
                armadaUt[type_bateau]["Position"][i] = ""
                window[(case_tirs)].update(text=(window[(case_tirs)].get_text()),button_color=("orange red"))
                Touche = True
                chasse = True
        if armadaUt[type_bateau]["Position"] == [""]*armadaUt[type_bateau]["Cases"]:
            score+=armadaUt[type_bateau]["Cases"]*2
            armadaUt[type_bateau]["Coulé"] = True
            Touche = True
            Coule = True
        return window,score,scoreUt,"ordinateur",tirs, Touche, Coule, chasse
    
#==========

def Tir_Opti ():
    """
    Cette fonction permet de créer une liste contenant une case sur deux de la grille tel un damier, cette liste est ensuite séparée en 5.
    Il y a 4 listes contenant les quatre parties de la grille (Haut Gauche, Haut Droit, Bas Droit, Bas Gauche)
    et la denière liste contenant les cases du centre de la gille.

    Returns
    -------
    Liste_CaseOpti : Liste
        Contient le coordonnées d'une case sur deux de la grille tel un damier.
    plateau : Liste
        Cette liste contient 4 listes associées au quatres parties contenant une case sur deux de la grille tel un damier.
    Liste_Centre : Liste
         Contient le coordonnées du centre d'une case sur deux de la grille tel un damier.

    """
    Liste_CaseOpti = []
    Liste_HautDroit = []
    Liste_HautGauche = []
    Liste_BasDroit = []
    Liste_BasGauche = []
    Liste_Centre = []
    for i in range(len(lignes)):                                                 #Creation d'une liste contenant une case sur 2
        for j in range(len(colonnes)):
            if (i % 2 == 1) and (j % 2 == 1):
                Liste_CaseOpti.append([str(i+1),str(j+1)])
                
            if (i % 2 == 0) and (j % 2 == 0):
                Liste_CaseOpti.append([str(i+1),str(j+1)])
                     
    for i in range (len(Liste_CaseOpti)):                                         #separation de cette nouvelle grille en 4
        if Liste_CaseOpti[i][0] in [str(j) for j in range (1,6)]:
            if Liste_CaseOpti[i][1] in [str(k) for k in range (1,6)]:
                Liste_HautGauche.append(Liste_CaseOpti[i])
        if Liste_CaseOpti[i][0] in [str(j) for j in range (1,6)]:
            if Liste_CaseOpti[i][1] in [str(k) for k in range (6,11)]:
                Liste_HautDroit.append(Liste_CaseOpti[i])
        if Liste_CaseOpti[i][0] in [str(j) for j in range (6,11)]:
            if Liste_CaseOpti[i][1] in [str(k) for k in range (1,6)]:
                Liste_BasGauche.append(Liste_CaseOpti[i])
        if Liste_CaseOpti[i][0] in [str(j) for j in range (6,11)]:
            if Liste_CaseOpti[i][1] in [str(k) for k in range (6,11)]:
                Liste_BasDroit.append(Liste_CaseOpti[i])
        if Liste_CaseOpti[i][0] in [str(j) for j in range (3,9)]:
            if Liste_CaseOpti[i][1] in [str(k) for k in range (3,9)]:
                Liste_Centre.append(Liste_CaseOpti[i])
                
    plateau = [Liste_HautGauche, Liste_HautDroit, Liste_BasDroit, Liste_BasGauche] #repertorit la 4 parties de la grille
    
    return plateau, Liste_Centre

#==========

def Tirs_Recherche(tirs, plateau, Centre, Statuts_Tirs):
    """
    Cette fonction va choisir la case où l'ordinateur va tirer. En tirant une case sur deux tel un damier, au debut de la partie, l'ordinateur
    va avoir un plus grande chance de choisir une case au centre de la grille a l'aide de pourcentage. Ensuite la fonction va determiner
    le nombre de tirs dans chaque parties de la grille et si une partie à moins de tire que les autres alors la fonction va choisir un case
    de cette partie.

    Parameters
    ----------
    tirs : Liste
        Cette liste contient l'historique des tirs de l'ordinateur pour qu'il ne tire pas deux fois au même endroit.
    Case_Opti : Liste
        Contient le coordonnées d'une case sur deux de la grille tel un damier.
    plateau : Liste
        Cette liste contient 4 listes associées au quatres parties contenant une case sur deux de la grille tel un damier.
    Centre : Liste
         Contient le coordonnées du centre d'une case sur deux de la grille tel un damier.
    Statuts_Tirs : Liste
        Contient le nombre de tir effectuer dans les 4 partie de la grille.

    Returns
    -------
    case : Liste
        Contient les coordonnées du tr de l'ordinateur.
    Statuts_Tirs : Liste
        Contient le nombre de tir effectuer dans les 4 partie de la grille.
    plateau : Liste
        Cette liste contient 4 listes associées au quatres parties contenant une case sur deux de la grille tel un damier.

    """
    pourcent = randint(0,10)                                     #tirage d'un nombre
    case = []                                                    #pour stocker la future case
    Statuts_Max = Statuts_Tirs[0]                                #Nombre max de tirs une case
    Statuts_Min = Statuts_Tirs[0]                                #Nombre min de tirs une case
    Repartition_Tirs = True                                      
    indice_min = 0
    End_Game = []

    for i in range (len(plateau)):
        for j in range (len(plateau[i])):
            if plateau[i][j] not in tirs:
                End_Game.append(plateau[i][j])
    
    for i in range (len(Statuts_Tirs)):                        
        if Statuts_Max < Statuts_Tirs[i]:                        #trouve la partie de la grille avec le plus de tirs
            Statuts_Max = Statuts_Tirs[i]                        #recupere le nombre de tirs dans cette partie
        if Statuts_Min > Statuts_Tirs[i]:                        #trouve la partie de la grille avec le plus de tirs
            Statuts_Min = Statuts_Tirs[i]                        #recupere le nombre de tirs dans cette partie
            indice_min = i                                       #recupere l'indice de cette partie
    
    if (Statuts_Max - Statuts_Min) >= 2:                         #Si une partie à 3 tirs de plus qu'une autre alors
        Repartition_Tirs = False                                 #Repartition pas equitables de tirs
            
    if len(tirs) < 5:          # selectionne un pourcentage en fonction du nombre de tirs
        proba = 10
    if 5 <= len(tirs) < 10:    # selectionne un pourcentage en fonction du nombre de tirs
        proba = 8
    if 10 <= len(tirs) < 15:   # selectionne un pourcentage en fonction du nombre de tirs
        proba = 6
    if len(tirs) >= 15:        #permet de désactiver la plus forte proba de tirer au centre
        pourcent = -1
        proba = 0
    
    if Repartition_Tirs == True:                                  #si les tirs sont bien repartis alors:
        if (pourcent < proba) and (pourcent != -1):               #augmente la proba de tirer au centre
            while case in tirs or case == []:                     #evite que l'ordi tire au meme endroit
                case = Centre[randint(0,len(Centre)-1)]           #choisit une case parmi le centre
        else:
            while case in tirs or case == []:                     #evite que l'ordi tire au meme endroit
                Grille_Tirs = plateau[randint(0,len(plateau)-1)]  #choisit une section du plateau
                while len(Grille_Tirs) == 0:
                    Grille_Tirs = plateau[randint(0,len(plateau)-1)]#choisit une section du plateau
                case = Grille_Tirs[randint(0,len(Grille_Tirs)-1)] #choisit une case parmi cette partie
                    
    elif Repartition_Tirs == False:                               #si les tirs ne sont pas bien repartis alors
        while case in tirs or case == []:  
            Grille_Tirs = plateau[indice_min]                     #recupere la partie avec le moins de tirs
            while len(Grille_Tirs) == 0:
                Grille_Tirs = plateau[randint(0,len(plateau)-1)]  #choisit une section du plateau
                print("\npb solve")
            case = Grille_Tirs[randint(0,len(Grille_Tirs)-1)]     #choisit une case parmi cette partie

    return case, Statuts_Tirs, plateau


#==========

def Chasse_Bateaux(window, case, tirs, Choix_Cibles, Touche, Coule, Liste_Coule, chasse):
    """
    Cette fonction, une fois qu'un bateau est touché, va créer une liste des cases potentielles autour de cette dernière. Une fois la deuxième case
    du bateau touché, la fonction va définir la direction du bateau et actualiser les cases potentielles du bateau. Une fois le bateau coulé,
    la fonction va réinitialiser les informations concernant le bateau coulé (direction, les cases potentielles et Choix_Cibles).

    Parameters
    ----------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique dont la grille de l'utilisateur.
    case : Liste
        Contient les coordonnées du tr de l'ordinateur.
    tirs : Liste
        Cette liste contient l'historique des tirs de l'ordinateur pour qu'il ne tire pas deux fois au même endroit.
    Choix_Cibles : Liste
        Cette liste contient les coordonées des cases où il y a potentiellement le bateau ennemi.
    Touche : Booleen
        Cette variable renvoie vrai si l'ordinateur a touché un bateau ou renvoie faux sinon.
    Coule : Booleen
        Cette variable renvoie vrai si l'ordinateur a coulé un bateau ou renvoie faux sinon.
    Liste_Coule : Liste
        Cette liste va contenir les coordonnées des deux premières cases touchées par l'ordinateur pour ensuite definir la direction du bateau.
    chasse : Booleen
        Cette variable renvoie vrai si l'ordinateur a touché un bateau et il passe alors en mode chasse jusqu'à ce que le bateau soit coulé.

    Returns
    -------
    window : Fenêtre graphique principale
        Permet de récuperer les informations contenues dans la fenetre graphique dont la grille de l'utilisateur.
    case : Liste
        Contient les coordonnées du tr de l'ordinateur.
    tirs : Liste
        Cette liste contient l'historique des tirs de l'ordinateur pour qu'il ne tire pas deux fois au même endroit.
    Choix_Cibles : Liste
        Cette liste contient les coordonées des cases où il y a potentiellement le bateau ennemi.
    Touche : Booleen
        Cette variable renvoie vrai si l'ordinateur a touché un bateau ou renvoie faux sinon.
    Coule : Booleen
        Cette variable renvoie vrai si l'ordinateur a coulé un bateau ou renvoie faux sinon.
    Liste_Coule : Liste
        Cette liste va contenir les coordonnées des deux premières cases touchées par l'ordinateur pour ensuite definir la direction du bateau.
    chasse : Booleen
        Cette variable renvoie vrai si l'ordinateur a touché un bateau et il passe alors en mode chasse jusqu'à ce que le bateau soit coulé.

    """
    direction = ""
    if Choix_Cibles != []:                                           #determine et supprimer les case de choix cible deja tiré
        New_tab = []
        for i in range (0,len(Choix_Cibles)):                        #verifier si ca marche
            if Choix_Cibles[i] not in tirs:
                New_tab.append(Choix_Cibles[i])
        Choix_Cibles = New_tab

    if Touche == True:
        if Liste_Coule[0] == "":                               #affecte la premiere case 
            Liste_Coule[0] = case
        
        elif (Liste_Coule[0] != "") and (Liste_Coule[1] == ""):#affecte la 2 case 
            Liste_Coule[1] = case
        
        if Liste_Coule[0] != "" and Liste_Coule[1] != "":
            if Liste_Coule[0][0] == Liste_Coule[1][0]:         #determine la direction avec ces 2 cases et definie la ligne ou la colonne du bateau
                direction = "horizontale"
                Ligne_ref = Liste_Coule[0][0]
            elif Liste_Coule[0][1] == Liste_Coule[1][1]:
                direction = "verticale"
                Colonne_ref = Liste_Coule[0][1]
                
        if Coule == False:    
            if direction == "":                                     #determine la croix pour la premiere case touchee
                if [case[0],str(int(case[1])-1)] not in tirs:
                    if 0 < int(case[1])-1 < 11:
                        Choix_Cibles.append([case[0],str(int(case[1])-1)])        #case gauche
                if [case[0],str(int(case[1])+1)] not in tirs:
                    if 0 < int(case[1])+1 < 11:
                        Choix_Cibles.append([case[0],str(int(case[1])+1)])        #case droite
                if [str(int(case[0])+1),case[1]] not in tirs:
                    if 0 < int(case[0])+1 < 11:
                        Choix_Cibles.append([str(int(case[0])+1),case[1]])        #case bas
                if [str(int(case[0])-1),case[1]] not in tirs:
                    if 0 < int(case[0])-1 < 11:
                        Choix_Cibles.append([str(int(case[0])-1),case[1]])        #case haut
                    
            elif direction == "horizontale":                        #suppression des cases hors de la ligne du bateau
                New_tab = []
                for i in range (0,len(Choix_Cibles)):                      
                    if Choix_Cibles[i][0] == Ligne_ref:
                        New_tab.append(Choix_Cibles[i])
                Choix_Cibles = New_tab
                
                if [case[0],str(int(case[1])-1)] not in tirs:
                    if 0 < int(case[1])-1 < 11:
                        Choix_Cibles.append([case[0],str(int(case[1])-1)])        #case gauche
                if [case[0],str(int(case[1])+1)] not in tirs:
                    if 0 < int(case[1])+1 < 11:
                        Choix_Cibles.append([case[0],str(int(case[1])+1)])        #case droite
                    
            elif direction == "verticale":                                        #suppression des cases hors de la colonne du bateau
                New_tab = []
                for i in range (0,len(Choix_Cibles)):                      
                    if Choix_Cibles[i][1] == Colonne_ref:
                        New_tab.append(Choix_Cibles[i])
                Choix_Cibles = New_tab
                
                if [str(int(case[0])+1),case[1]] not in tirs:
                    if 0 < int(case[0])+1 < 11:
                        Choix_Cibles.append([str(int(case[0])+1),case[1]])         #case bas
                if [str(int(case[0])-1),case[1]] not in tirs:
                    if 0 < int(case[0])-1 < 11:
                        Choix_Cibles.append([str(int(case[0])-1),case[1]])         #case haut
                
        elif Coule == True:                                                            #si bateau coulé, reset des données
            Modele_Bateau = window[("utilisateur",int(case[0]),int(case[1]))].get_text()
            Modele_Bateau = Modele_Bateau.lower()
            Coord = armadaUt[Modele_Bateau]["Position_fixe"]
            if direction == "horizontale":
                for i in range (int(Coord[0][0])-1, int(Coord[0][0])+2): 
                    for j in range(int(Coord[0][1])-1, int(Coord[-1][1])+2):
                        if i<1 or i>10 or j<1 or j>10:
                            continue
                        if [str(i),str(j)] not in tirs:
                            tirs.append([str(i),str(j)])
            if direction == "verticale":
                for j in range (int(Coord[0][1])-1, int(Coord[0][1])+2): 
                    for i in range(int(Coord[0][0])-1, int(Coord[-1][0])+2):
                        if i<1 or i>10 or j<1 or j>10:
                            continue
                        if [str(i),str(j)] not in tirs:
                            tirs.append([str(i),str(j)])
                            
            chasse = False
            direction = ""
            Choix_Cibles = []
            Liste_Coule = ["",""]                        
    return window, case, tirs, Choix_Cibles, Touche, Coule, Liste_Coule, chasse

#==========

def Info_Case(tirs, plateau, Statuts_Tirs, case):
    """
    Cette fonction va actualiser le nombre de tirs dans chaque parties de la grille. Elle va ensuite supprimer du plateau la case sur laquelle
    l'ordinateur à déjà tirer.

    Parameters
    ----------
    tirs : Liste
        Cette liste contient l'historique des tirs de l'ordinateur pour qu'il ne tire pas deux fois au même endroit.
    plateau : Liste
        Cette liste contient 4 listes associées au quatres parties contenant une case sur deux de la grille tel un damier.
    Statuts_Tirs : Liste
        Contient le nombre de tir effectuer dans les 4 partie de la grille.
    case : Liste
        Contient les coordonnées du tr de l'ordinateur.

    Returns
    -------
    plateau : Liste
        Cette liste contient 4 listes associées au quatres parties contenant une case sur deux de la grille tel un damier.
    Statuts_Tirs : Liste
        Contient le nombre de tir effectuer dans les 4 partie de la grille.

    """
    
    if (int(case[0]) in [1,2,3,4,5]) and (int(case[1]) in [1,2,3,4,5]) and (case in plateau[0]):
        Statuts_Tirs[0] += 1
    if (int(case[0]) in [1,2,3,4,5]) and (int(case[1]) in [6,7,8,9,10]) and (case in plateau[1]):
        Statuts_Tirs[1] += 1
    if (int(case[0]) in [6,7,8,9,10]) and (int(case[1]) in [6,7,8,9,10]) and (case in plateau[2]):
        Statuts_Tirs[2] += 1
    if (int(case[0]) in [6,7,8,9,10]) and (int(case[1]) in [1,2,3,4,5]) and (case in plateau[3]):
        Statuts_Tirs[3] += 1
        
    for i in range (len(plateau)):
        New_Tab=[]
        for j in range (len(plateau[i])):
            if plateau[i][j] not in tirs:
                New_Tab.append(plateau[i][j])
        plateau[i] = New_Tab
    return plateau, Statuts_Tirs

#==========

def Statuts_Coule(armada):
    """
    Cette fonction permet de savoir si tous les bateaux de l'utilisateur ou de l'ordinateur sont coulés.

    Parameters
    ----------
    armada : Dictionnaire
        Contient toutes les informations sur l'armada de l'utilisateur ou de l'ordinateur.

    Returns
    -------
    bool
        Prends la valeur True si tous les bateaux d'un des deux joueurs sont coulés, sinon prends la valeur False.

    """
    tab=["sm","ct1","ct2","c","pa"]
    for i in range(5):
        if armada[tab[i]]["Coulé"] == True:
            tab[i] = True
    if tab == [True,True,True,True,True]:
        return True 
    else:
        return False