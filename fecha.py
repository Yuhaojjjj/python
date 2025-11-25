def devuelve_dia(fecha):
    dia = ""
    i = 0
    while(i < len(fecha)):
        if(fecha[i] != " "):
            dia += fecha[i]
            i += 1
        else:
            i = len(fecha)
    return(dia)

def devuelve_mes(fecha):
    mes = ""
    i = 0
    nespacios = 0
    while(i < len(fecha)):
        if(fecha[i] == " "):
            nespacios += 1
        else:
            if(nespacios == 2):
                mes += fecha[i]
        i += 1
    return(mes)  


def fecha():
    fecha = raw_input("Introduce la fecha en el formato: 4 de enero de 2026: ")
    dia = devuelve_dia(fecha)
    mes = devuelve_mes(fecha)
    print(dia)
    print(mes)

fecha()
