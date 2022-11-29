def display(**name):
    for key in name:
        print(key,":",name[key])


diccionario = {
        "nombre":"esteven",
        "Apellido":"calcina"
        }
display(diccionario,k="a")
#display(primerName = "Esteven",segundoName="Antonio",apellido="Calcina")
