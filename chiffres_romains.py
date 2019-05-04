"""I=1...."""

dict_nombres_romains = {"I":1, "V":5, "X":10, "L": 50, "M": 1000, "C": 100, "D": 500}

def RomanNumber (romains):

    resultat = 0

    for romain in reversed(romains):
        resultat = resultat + dict_nombres_romains[romain]
       

    return resultat

print "RomanNumber('I') == 1 : " + str(RomanNumber("I") == 1)
print "RomanNumber('II') == 2 : " + str(RomanNumber('II') == 2)
print "RomanNumber('III') == 3 : " + str(RomanNumber('III') == 3)
print "RomanNumber('V') == 5 : " + str(RomanNumber('V') == 5)
print "RomanNumber('X') == 10 : " + str(RomanNumber('X') == 10)
print "RomanNumber('MCMLXXVII') == 1977 : " + str(RomanNumber('MCMLXXVII') == 1977)