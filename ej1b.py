def curvi(palabra):
    j = 0
    suma = 0
    curv = True
    respuestac = 0
    curvis = "QRUOPSDGJÑCB"
    for j in range(1, len(palabra)):
        if palabra[j] in curvis:
            suma += 1
    return suma

def mayusc(palabra):
    i = 0
    mayusc = "QWERTYUIOPASDFGJHKLÑZXCVMBN"
    for letra in palabra:
        if letra not in mayusc:
            return 1
    return 0

def programa_2():
    palabra = raw_input("Introduce una palabra: ")
    if mayusc(palabra) == 0:
        print("La palabra tiene mayúsculas.")
        print("Tu palabra contiene " + str(curvi(palabra)) + " letras curvas.")
    else:
        print("La palabra contiene minúsculas.")
programa_2()
