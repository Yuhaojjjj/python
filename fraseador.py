def letras(frase):
    print str(len(frase))
def cyv(frase):
    i = 0
    voc = 0
    vocales = 'aeiouAEIOU'
    for i in range (0, len(frase)):
        if frase[i] in vocales :
            voc += 1
    print str(voc)
    print str(len(frase) - voc)
def pal(frase):
    i = 0
    pal = 1
    spc = ' '
    for i in range (0, len(frase)):
        if frase[i] == spc :
            pal += 1
    print str(pal)
def os(frase):
    no = 0
    i = 0
    for i in range (0, len(frase)):
        if frase[i] in 'oO' :
            no += 1
    print str(no)
def encriptar(frase):
    i = 0
    spc = ' '
    cfr = ""
    for i in range (0, len(frase)):
        if frase[i] == spc:
            cfr += ' '
        elif frase[i] == 'z':
            cfr += 'a'
        else:
            cfr += chr(ord(frase[i]) + 1)
    print (cfr)
def fraseador():
    frase = raw_input("Dime algo: ")
    letras(frase)
    cyv(frase)
    pal(frase)
    os(frase)
    encriptar(frase)
fraseador()
