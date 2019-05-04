"""1=I
5=V
10=X
50=L
100=C
500=D
1000=M"""

def romanToNumbers(romains): 
    if romains == "I":                                      
        return 1
    if romains == "V":
        return 5

print "romanToNumbers('I'): 1 == " + str(romanToNumbers("I"))
print "romanToNumbers('V'): 5 == " + str(romanToNumbers("V"))
