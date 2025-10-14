def letras(frase):
    i = 0
    letras = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    let = 0
    for i in range (0, len(frase)):
        if frase[i] in letras:
            let += 1
    print ("Tu frase tiene " + str(let) + " letras.")
def consonantes(frase):
    i = 0
    cons = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    con = 0
    for i in range (0, len(frase)):
        if frase[i] in cons :
            con += 1
    print ("Tu frase tiene " + str(con) + " consonantes.")
def vocales(frase):
    i = 0
    voc = 0
    vocales = 'aeiouAEIOU'
    for i in range (0, len(frase)):
        if frase[i] in vocales :
            voc += 1
    print ("Tu frase tiene " + str(voc) + " vocales.")
def pal(frase):
    i = 0
    pal = 1
    spc = ' '
    for i in range (0, len(frase)):
        if frase[i] == spc :
            pal += 1
    print ("Tu frase tiene " + str(pal) + " palabras.")
def os(frase):
    no = 0
    i = 0
    for i in range (0, len(frase)):
        if frase[i] in 'oO' :
            no += 1
    print ("Tu frase tiene " + str(no) + " o(s).")
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
    print ("Tu frase encriptada es: " + cfr + ".")
def fraseador():
    frase = raw_input("Digame algo: ")
    print("Menu del dia:\n1. Número de letra\n2. Número de consonantes\n3. Número de vocales vocales\n4. Número de palabras\n5. Número de veces que aparece la letra o\n6. Encripta el mensaje sustituyendo cada letra por la siguiente en elabecedario")
    menu = raw_input("¿Qué quiere comer hoy? ")
    if '1' in menu:
        letras(frase)
    if '2' in menu:
        consonantes(frase)
    if '3' in menu:
        vocales(frase)
    if '4' in menu:
        pal(frase)
    if '5' in menu:
        os(frase)
    if '6' in menu:
        encriptar(frase)
fraseador()
