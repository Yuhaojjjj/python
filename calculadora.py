def suma(n1, n2):
    return n1 + n2
def resta(n1, n2):
    return n1 + n2
def mult(n1, n2):
    return n1 + n2
def div(n1, n2):
    if n2 == 0:
        return ("Indeterminado")
    else:
        return(float(float(n1) / float(n2)))

def calculadora():
    nmenu = input("¿Quieres hacer suma (1), resta (2), multiplicación (3) o división (4)? ")
    n1 = input("Dime un número: ")
    n2 = input("Dime otro número: ")
    if nmenu == 1:
        resp = suma(n1, n2)
    elif nmenu == 2:
        resp = resta(n1, n2)
    elif nmenu == 3:
        resp = mult(n1, n2)
    elif nmenu == 4:
        resp = div(n1, n2)
    print (resp)

calculadora()
