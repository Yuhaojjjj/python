def ululador() :
    fraseen = raw_input ("Dime algo coherente: ")
    frasesa = ""
    vocales = 'aeiouAEIOU'
    for i in range (0, len(fraseen)):
        if (fraseen[i] in vocales):
            frasesa = frasesa + 'u'
        else:
            frasesa = frasesa + fraseen[i]
    print (frasesa)
ululador()
