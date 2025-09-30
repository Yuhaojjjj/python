def cuentavocales ():
    cad = raw_input ("Dime una palabra: ")
    voc = 0
    for i in range (0, len(cad)):
        if cad[i] == 'a':
            voc = voc + 1
        elif cad[i] == 'e':
            voc = voc + 1
        elif cad[i] == 'i':
            voc = voc + 1
        elif cad[i] == 'o':
            voc = voc + 1
        elif cad[i] == 'u':
            voc = voc + 1
        elif cad[i] == 'A':
            voc = voc + 1
        elif cad[i] == 'E':
            voc = voc + 1
        elif cad[i] == 'I':
            voc = voc + 1
        elif cad[i] == 'O':
            voc = voc + 1
        elif cad[i] == 'U':
            voc = voc + 1
    con = len(cad) - voc
    print( "Tu palabra tiene " + str(voc) + " vocales y " + str(con) + " consonantes.")
cuentavocales()
