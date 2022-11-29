def recorrerParametrosArbitrarios(pFijo,*arbitrarios,**diccionario):
    print( pFijo)
    for argumento in arbitrarios:
        print (argumento)

    for clave in diccionario:
        print ("el valor es", clave,"es",diccionario[clave])
        

diccionario1 ={
        "year":1964,
        "color":"red"
        }
recorrerParametrosArbitrarios("fijo","arbi1","arbi2",diccionario1)

