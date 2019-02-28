parametre_entre = raw_input(‘Entrer un chiffre: ’)

def transforme(romain):
   chiffres = { “I”: 1, “II”: 2, “III”:3, “IV” : 4, “V”: 5, “X”: 10 }
   return chiffres[romain]

resultat = transforme (parametre_entre)
print resultat