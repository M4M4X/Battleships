# -*- coding: utf-8 -*-
#
# Programme principal
# Mai 2021
# Auteurs : Maxime Innocenti & Antoine Henriet
# Version : 2.0
#
import PySimpleGUI as sg
from Fonctions_finales import *

#---Creation Fenetres Graphiques---#

#Creation fenetre principale
colonnes = lignes = 11

sg.theme("DarkBlue14")

menu = [
        ["Fichier", ["Exit"]],
        ["Triche",["Afficher Bateaux Ennemis", "Masquer Bateaux Ennemis"]],
        ["Aide", ["Règles du jeu","A propos"]]
       ]

layout = []

# Ajoute le menu
layout.append([sg.Menu(menu)])

# Définit le titre
titre = [[sg.Text("Bataille Navale", font=("Arial",50), justification = "center")]]

# Ajoute le titre
layout.append([sg.Frame("", titre, border_width = 0, vertical_alignment = "center", element_justification="center")])

# Définit la grille de gauche + ajout du statuts des bateaux en dessous
grille_gauche = []
for i in range(lignes):
    grille_ligne = []
    for j in range(colonnes):
        if (i == 0):
            if (j == 0):
                grille_ligne.append(sg.Button(("\\"),size=(4,2),key=("utilisateur",i,j),pad=(0,0),button_color=("black"),disabled = True))
            else:
                grille_ligne.append(sg.Button(str(chr(ord("A")+j-1)),size=(4,2),key=("utilisateur",i,j),pad=(0,0),button_color=("black"),disabled = True))
        else:
            if (j == 0):
                grille_ligne.append(sg.Button((str(i)),size=(4,2),key=("utilisateur",i,j),pad=(0,0),button_color=("black"),disabled = True))
            else:
                grille_ligne.append(sg.Button("__",size=(4,2),key=("utilisateur",i,j),pad=(0,0),button_color=("grey70")))
    grille_gauche.append(grille_ligne) 

BAR_MAX = 1000
zone_statuts_joueur = [[sg.Text('Porte-Avion (5 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG1JOU-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Croiseur (4 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG2JOU-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Contre-Torpilleur 1 (3 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG3JOU-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Contre-Torpilleur 2 (3 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG4JOU-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Sous-Marin (2 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG5JOU-', bar_color =["orange red","light steel blue"])]
        ]

colonne_gauche = [[sg.Frame("Grille Joueur",grille_gauche,title_location="n",element_justification="center")],
                  [sg.Frame("Statuts Bateaux Joueur",zone_statuts_joueur,title_location="n",element_justification="left")]
                  ]

# Définit la zone d'information
zone_info = [[sg.Output(size=(30,15),key="console")],
             [sg.Text("")],
             [sg.Frame("",border_width = 0,layout=[[sg.Button("Touché",size=(12,8),pad=(20,20),button_color=("orange red")),sg.Button("Raté",size=(12,8),pad=(20,20),button_color=("grey40"))]])]
             ]

# Définit la grille de droite + ajout du statuts des bateaux en dessous
grille_droite = []
for i in range(lignes):
    grille_ligne = []
    for j in range(colonnes):
        if (i == 0):
            if (j == 0):
                grille_ligne.append(sg.Button("\\",size=(4,2),key=("tirs",i,j),pad=(0,0),button_color=("black"),disabled = True))
            else:
                grille_ligne.append(sg.Button(str(chr(ord("A")+j-1)),size=(4,2),key=("tirs",i,j),pad=(0,0),button_color=("black"),disabled = True))
        else:
            if (j == 0):
                grille_ligne.append(sg.Button((str(i)),size=(4,2),key=("tirs",i,j),pad=(0,0),button_color=("black"),disabled = True))
            else:
                grille_ligne.append(sg.Button("__",size=(4,2),key=("tirs",i,j),pad=(0,0),button_color=("grey70")))
    grille_droite.append(grille_ligne) 

BAR_MAX = 1000
zone_statuts_ord = [[sg.Text('Porte-Avion (5 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG1ORD-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Croiseur (4 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG2ORD-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Contre-Torpilleur 1 (3 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG3ORD-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Contre-Torpilleur 2 (3 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG4ORD-', bar_color =["orange red","light steel blue"])],
          [sg.Text('Sous-Marin (2 cases)',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG5ORD-', bar_color =["orange red","light steel blue"])]
               ]
colonne_droite = [[sg.Frame("Grille Tirs",grille_droite,title_location="n",element_justification="center")],
                  [sg.Frame("Statuts Bateaux Ordinateur",zone_statuts_ord,title_location="n",element_justification="left")]
                  ]

# Ajoute les 3 zones
layout.append([
     sg.Frame("", colonne_gauche, title_location="n", vertical_alignment = "top", element_justification="center", border_width = 0),
     sg.Frame("Logs", zone_info, title_location="n", vertical_alignment = "top",element_justification="center", border_width = 0),
     sg.Frame("", colonne_droite, title_location="n", vertical_alignment = "top", element_justification="center", border_width = 0),
    ])

#Creation fenetre choix bateaux
layout1=[[sg.Text("Choisissez un bateau :")],
         [sg.Listbox(values=listeBateau,size=(30,5),key="-LISTEBATEAU-",enable_events=True)]]

#Creation fenetre triche
layout2=[]

#Ajout de la grille
grille_ord=[]

for i in range(lignes):
    grille_ligne = []
    for j in range(colonnes):
        if (i == 0):
            if (j == 0):
                grille_ligne.append(sg.Button("\\",size=(4,2),key=("ordinateur",i,j),pad=(0,0),button_color=("black"),disabled = True))
            else:
                grille_ligne.append(sg.Button(str(chr(ord("A")+j-1)),size=(4,2),key=("ordinateur",i,j),pad=(0,0),button_color=("black"),disabled = True))
        else:
            if (j == 0):
                grille_ligne.append(sg.Button((str(i)),size=(4,2),key=("ordinateur",i,j),pad=(0,0),button_color=("black"),disabled = True))
            else:
                grille_ligne.append(sg.Button("__",size=(4,2),key=("ordinateur",i,j),pad=(0,0),button_color=("grey70"),disabled = True))
    grille_ord.append(grille_ligne) 

#Ajout de la grille au layout
layout2.append([sg.Frame("", grille_ord, border_width = 0)])

#Declaration des fenetres
window2 = sg.Window("Grille Bateaux Ordinateur", layout2, grab_anywhere=False, finalize=True, disable_close=True)
window2.hide()
window1 = sg.Window("Liste des bateaux à placer", layout1, disable_close=True, finalize=True)
window1.hide()
window = sg.Window("Bataille Navale", layout, grab_anywhere=False)


#---Programme Principal---#

compte=["1er","2e","3e","4e","5e"]
scoreUt , scoreOrd = 25, 25
tour = "utilisateur"
gagnant = ""
Bateau_Coule = False
tirs=[]
compteur_tour=1
deroulement = "placement"
Statuts_Tirs = [0,0,0,0]                                     #Nombre de tirs dans les != parties du platau
chasse = False                                               #Statuts de chasse de bateaux
Touche = False
Coule = False
Liste_Coule = ["",""]
Choix_Cibles = []
plateau, Centre = Tir_Opti()

event, values = window.read()

while (0<scoreUt) and (0<scoreOrd) and Bateau_Coule == False :
    if deroulement == "":
        compteur_tour+=1
        print("\n\nTour numéro",compteur_tour)
        print("Score joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))
        if tour == "utilisateur":
            print("Sur quelle case voulez-vous tirer?")

    # Partie gestion des boutons de la fenetre
    if event in [sg.WIN_CLOSED,"Exit"]:
        window2.close()
        window.close()
        exit()
    if event == "A propos":
        sg.Popup("Version : 2.0 de Mai 2021","Auteurs : Maxime Innocenti - Antoine Henriet")
    if event == "Règles du jeu":
        sg.Popup("Règle de la Bataille Navale :","- Début de la partie :","La bataille navale oppose deux joueurs qui s'affrontent.",
                 "Au début du jeu, chaque joueur place ses bateaux sur sa grille. Celle-ci est toujours numérotée de 1 à 10 verticalement et de A à J horizontalement."
                 "Chacun a une flotte composée de 5 bateaux, qui sont les suivants : 1 porte-avion (5 cases), 1 croiseur (4 cases), 2 contre-torpilleurs (3 cases), 1 sous-marin (2 cases).",
                 "Les bateaux ne doivent pas être collés entre eux.",
                 "","- Déroulement de la partie :","Un à un, les joueurs vont « tirer » sur une case de l'adversaire : par exemple, B3 ou encore H8.",
                 "","- But du jeu :","Le but du jeu est de couler tous les bateaux ennemis !",
                 "","- Fin de la partie :","La partie se termine quand un des deux joueurs n'a plus de bateaux, ou alors n'a plus de points pour tirer.")
    if event == "Afficher Bateaux Ennemis":
        window2.un_hide()
    if event == "Masquer Bateaux Ennemis":
        window2.hide()

    # Partie jeu
    if deroulement == "placement":
        
        # Placement bateaux joueur
        for i in range (5):        
            ok = False
            place = False
            player = "utilisateur"
            while (ok != True) or (place != True):
                armadaUt,bateau,case_depart,case_arrivee = Appel(window,window1,armadaUt)
                ok = Simulation(window,armadaUt,bateau,case_depart,case_arrivee,player) #verifier si les cases choisis peuvent permettre la pose d'un bateau
                if ok == True :
                    place, armadaUt= Occupation(window,armadaUt,bateau,case_depart,case_arrivee,player) #Verifie si le bateau de chevauche pas d'autres bateaux
                    if place == True :
                        Placement(window,armadaUt, bateau,case_depart,case_arrivee,player)
                    else:
                        armadaUt[bateau]["Place"] = False
                else:
                    armadaUt[bateau]["Place"] = False        
        print("\nVous avez placé tous vos bateaux")
        
        # Placement bateaux ordinateur       
        for i in range (5):       
            ok = False
            place = False
            player = "ordinateur"
            while (ok != True) or (place != True):
                armadaOrd,bateau,case_depart,case_arrivee = AppelOrdinateur(armadaOrd)
                pose, armadaOrd= Bateau(armadaOrd,bateau,player) #Vérifie si le bateau n'est pas déjà placé
                if pose == True: 
                    ok = Simulation(window2, armadaOrd, bateau, case_depart, case_arrivee, player) #verifier si les cases choisis peuvent permettre la pose d'un bateau
                    if ok == True :
                        place, armadaOrd= Occupation(window2, armadaOrd, bateau, case_depart, case_arrivee, player) #Verifie si le bateau de chevauche pas d'autres bateaux
                        if place == True : 
                            Placement(window2, armadaOrd, bateau, case_depart, case_arrivee, player)
                        else:
                            armadaOrd[bateau]["Bateaux"]+=1
                    else:
                        armadaOrd[bateau]["Bateaux"]+=1
        deroulement = ""
        print("\n\nTour numéro",compteur_tour)
        print("Sur quelle case voulez-vous tirer?")

    if tour == "utilisateur" and Bateau_Coule == False:
        window, window2, scoreUt, tour = TirUt(window, window2, scoreUt)
        if Statuts_Coule(armadaOrd) == True:
            Bateau_Coule = True
            gagnant = "Utilisateur"
            
        #Actualisation des Statuts Bateaux de l'ordinateur
        if armadaOrd["pa"]["Coulé"] == True:
            window['-PROG1ORD-'].update(1000)
        if armadaOrd["c"]["Coulé"] == True:
            window['-PROG2ORD-'].update(1000)
        if armadaOrd["ct1"]["Coulé"] == True:
            window['-PROG3ORD-'].update(1000)
        if armadaOrd["ct2"]["Coulé"] == True:
            window['-PROG4ORD-'].update(1000)
        if armadaOrd["sm"]["Coulé"] == True:
            window['-PROG5ORD-'].update(1000)
            
        
    if tour == "ordinateur" and Bateau_Coule == False:
        if chasse == False:                                     #Passe en mode recherche
            case, Statuts_Tirs, plateau = Tirs_Recherche(tirs, plateau, Centre, Statuts_Tirs)

        elif chasse == True:                                    #Passe en mode chasse
            case = Choix_Cibles[randint(0,len(Choix_Cibles)-1)] #tirage dans les cibles potentielles
        
        plateau, Statuts_Tirs = Info_Case(tirs, plateau, Statuts_Tirs, case) #supprime du plateau la case selectionnée par la fontion Tirs_Recherche et actualise la repartition des tirs sur le plateau
        window, scoreOrd, scoreUt, tour, tirs, Touche, Coule, chasse = TirOrd(window, window2, scoreOrd, scoreUt, tirs, case, chasse)
        
        if chasse == True:
            window, case, tirs, Choix_Cibles, Touche, Coule, Liste_Coule, chasse = Chasse_Bateaux(window, case, tirs, Choix_Cibles, Touche, Coule, Liste_Coule, chasse)

        if Statuts_Coule(armadaUt) == True:
            Bateau_Coule = True
            gagnant = "Ordi"
            
        #Actualisation des Statuts Bateaux du joueur
        if armadaUt["pa"]["Coulé"] == True:
            window['-PROG1JOU-'].update(1000)
        if armadaUt["c"]["Coulé"] == True:
            window['-PROG2JOU-'].update(1000)
        if armadaUt["ct1"]["Coulé"] == True:
            window['-PROG3JOU-'].update(1000)
        if armadaUt["ct2"]["Coulé"] == True:
            window['-PROG4JOU-'].update(1000)
        if armadaUt["sm"]["Coulé"] == True:
            window['-PROG5JOU-'].update(1000)
        
    if gagnant == "Utilisateur":
        print("Score joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))
        sg.Popup("\nFélicitations vous avez gagné !\nScore joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))
        
    if gagnant == "Ordi":
        print("Score joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))
        sg.Popup("\nL'ordinateur a gagné\nDommage vous avez perdu !\nScore joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))

    if scoreUt <= 0:
        print("Score joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))
        sg.Popup("\nDommage, vous n'avez plus de point pour jouer.\nL'ordinateur est déclaré comme gagnant\nScore joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))
    
    if scoreOrd <= 0:
        print("Score joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))
        sg.Popup("\nL'ordinateur n'a plus de points.\nFélicitations,vous êtes déclaré comme gagnant\nScore joueur: %i\nScore ordinateur : %i\n" %(scoreUt,scoreOrd))    

#Fermeture de toutes les fenêtres    
window2.close()
window1.close()
window.close()