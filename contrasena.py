def password() :
    nom = raw_input ("Dime tu nombre: ")
    ape1 = raw_input ("Dime tu primer apellido: ")
    ape2 = raw_input ("Dime tu segundo apellido: ")
    nac = raw_input ("Dime tu ano de nacimiento: ")
    print("tu contrasena sera: " + nom[:3] + ape1[:3] + ape2[:3] + nac[:2] )

password()
