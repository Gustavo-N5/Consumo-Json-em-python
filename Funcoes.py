def buscarMenor(lst):
    i = float("inf")
    j = 0
    a = []
    for nr in lst:
        a.append(nr)
        if nr < i and nr != 0:   
            j = a.index(nr) + 1 
            i = nr
    return f'O menor valor foi {i}, faturado no dia {j}'

def buscarMaior(lst):
    i = 0
    j = 0
    a = []
    for nr in lst:
        a.append(nr)
        if nr > i:
            j = a.index(nr) + 1
            i = nr
    return f'O maior valor foi {i}, faturado no dia {j}'

def buscarMaiorMedia(lst):
    suma = 0
    listaTemp = []
    listaDias = []
    listaValores = []

    for i in lst:
        if i > 0:
            suma += i
    
    media = suma / 30

    for j in lst:
        listaTemp.append(j)
        
        if j > media:
            listaDias.append(listaTemp.index(j) + 1 )
            listaValores.append(j)

    print(f'O total dia com os valores a cima da media foram {len(listaDias)}')
    print('Sendo eles:')
    
    k = 0
    while k < len(listaValores): 
        print(f"Dia {listaDias[k]}: {listaValores[k]}")
        k += 1