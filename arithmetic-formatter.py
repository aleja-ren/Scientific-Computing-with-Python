def arithmetic_arranger(problems, show_answers=False):
    arriba = []
    operador = []
    abajo = []
    resultado = []
    sol=''
    if len(problems) > 5:
        sol = "Error: Too many problems."
        return sol
    
    for problema in problems:
        partes = problema.split()
        arriba.append(partes[0])
        operador.append(partes[1])
        abajo.append(partes[2])
    #print(arriba)
    #print(operador)
    #print(abajo)


    for op in operador:
        if op not in ['+','-']:
            sol = "Error: Operator must be '+' or '-'."
            return sol
    for i in range(len(arriba)):
        if len(arriba[i])>4 or len(abajo[i])>4:
            sol = 'Error: Numbers cannot be more than four digits.'
            return sol
    for i in range(len(arriba)):
        if not (arriba[i].isdigit() and abajo[i].isdigit()):
            sol = 'Error: Numbers must only contain digits.'
            return sol
    #Ahora aqui ya estaría correcta la entrada
    for problema in problems:
        resultado.append(eval(problema))
    #print(resultado) #tenemos los resultados por si esta a true el param

    primera_linea=[]
    segunda_linea=[]
    linea_guion=[]
    cuarta_linea=[]


    for i in range(len(arriba)):
        if(len(arriba[i])>len(abajo[i])):
            primera_linea.append(" "*2 + arriba[i])
        else:
            primera_linea.append(" "*(len(abajo[i]) - len(arriba[i]) + 2) + arriba[i])
    

    for j in range(len(abajo)):
        if(len(abajo[j])>len(arriba[j])):
            segunda_linea.append(operador[j]+' '+abajo[j])
        else:
            segunda_linea.append(operador[j]+' '*(len(arriba[j])-len(abajo[j])+1)+abajo[j])

    
    for i in range(len(arriba)):
        linea_guion.append('-'*max(len(primera_linea[i]),len(segunda_linea[i])))

    sol="    ".join(primera_linea)+'\n'+"    ".join(segunda_linea)+'\n'+"    ".join(linea_guion)
    if show_answers:
        for i in range(len(arriba)):
            cuarta_linea.append(" "*(len(linea_guion[i])-len(str(resultado[i])))+str(resultado[i]))
        sol=sol+'\n'+"    ".join(cuarta_linea)
    return sol

print(arithmetic_arranger(["3 + 855", "988 + 40"], True))