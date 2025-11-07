def alt_digitador():
    suma = 0
    numi = input("Dime un número: ")
    for i in range (1, len(str(numi)) + 1):
        dig = numi % 10
        suma += dig
        numi = numi / 10
    print suma
alt_digitador()
