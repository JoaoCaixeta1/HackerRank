def timeConversion(h):
    periodo = h[-2:] #AM ou PM
    lista_horas = h[:-2].split(":") #vai criar uma lista com as horas ["07", "30", "10"]
    horas = int(lista_horas[0])
    minutos = lista_horas[1]
    segundos = lista_horas[2]

    if periodo == "AM":
        if horas >= 12: #17:30:10AM
            hour =  horas - 12
        else: #07:30:10AM
            hour = horas
    if periodo == "PM":
        if horas >= 12: #17:30:10PM
            hour = horas
        else: #07:30:10PM
            hour = horas + 12
    
    print(f"{hour:02}:{minutos}:{segundos}")


#h = 07:30:10PM
h = input()
timeConversion(h)
