import random
def erstelle_computer_wahl():
     n = random.randint(1,3)
     if n == 1:
         return "Schere"
     elif n == 2:
         return "Stein"
     else:
         return "Papier"

benutzer_treffer = 0
computer_treffer = 0

"""
Wenn man Schummeln will, 
kann er die Funktion schummeln() verwenden.
"""
"""
def schummeln(benutzer_wahl):
    if benutzer_wahl == "Schere":
        return "Stein"
    elif benutzer_wahl == "Stein":
        return "Papier"
    else:
        return "Schere"
"""
while True:
    benutzer_wahl = input("Schere? Stein? Papier?")
    computer_wahl = erstelle_computer_wahl()
    """
    wenn schummeln() Funktion verwendet wird, 
    untenstehende kommentar
    entfernen.
    """
    #computer_wahl = schummeln(benutzer_wahl)
    print("Computer wählte: ", computer_wahl)

    if(benutzer_wahl == computer_wahl):
     print("Unentschieden")
    elif computer_wahl== "Stein" and benutzer_wahl =="Papier" :
     benutzer_treffer +=1
    elif computer_wahl == "Papier" and benutzer_wahl == "Schere":
     benutzer_treffer +=1
    elif computer_wahl== "Schere" and benutzer_wahl == "Stein":
     benutzer_treffer +=1
    else:
     computer_treffer +=1

    print("Sie:", benutzer_treffer, " VS  Computer:", computer_treffer)

    if benutzer_treffer == 3 or computer_treffer == 3:
        break

if benutzer_treffer > computer_treffer:
    print("Sie haben gewonnen")
else:
    print("Computer hat gewonnen")