def digitador():
    suma = 0
    num = raw_input("Dime un número: ")
    for i in range (0, len(num)):
        suma += int(num[i])
    print suma
digitador()
