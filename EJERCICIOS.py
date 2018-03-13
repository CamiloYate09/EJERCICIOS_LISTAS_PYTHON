

#EJERCICIO 1

"""
Diseña un método que reciba como parámetro una lista de 5 números
y retorne una lista con la suma, resta, multiplicación y división de todos.
"""





#EJERCICIO 2

"""
Diseña un método que reciba como parámetro 5 números y los retorne en otra lista ordenados de forma ascendente.
"""



def lista_ordenada():
    lista = [1,5,7,8,9,3]

    lista.sort()
    print(chr(27)+"[1;33m",lista)




#EJERCICIO 3

"""
Diseña un método que reciba como parámetro dos listas,
 cada una con 5 numeros, el método debe retornar una sola lista con los 10 números.
"""

def dos_listas():
    lista1 = []
    lista2 = []
    listatotal = []
    indice = 5

    print(chr(27)+"[1;33m"+"Por favor ingresa tu primera lista de 5 numeros \n")
    #n = input("Por favor ingresa tu primera lista de 5 numeros \n")
    #z = input("Por favor ingresa tu segunda lista de 5 numeros \n")
    for i in range(0,indice):
        print("\033[4;35;47m"+"Ingresa el elemento del indice ", i, "\n")
        elmento = input()
        lista1.insert(i,elmento)
        print(lista1)
    print("\n")
    print(chr(27)+"[1;33m"+ "Por favor ingresa tu segunda lista de 5 numeros \n")
    for j in range(0,indice):
        print()
        print("\033[4;35;47m"+"Ingresa el elemento del indice ", j, "\n")
        elmento2 = input()
        lista2.insert(j, elmento2)
        print(lista2)

        listatotal = lista1+lista2

    print(chr(27)+"[1;33m"+"Tus dos listas con los elementos son ", listatotal, "\n")




#EJERCICIO 4
"""
Diseña un método que reciba como parámetro 5 números y retorne una lista nueva con estos 5 números multiplicados por 2.
"""

#REVISAR
def lista_multiplicadora():
    lista = [1,2,3,4,5]

    multiplicador = 2

    r = range(1, lista+1)

    for i in r:
        print("\033[4;35;47m" + "", i , multiplicador*i,multiplicador*i)



#EJERICIO 5

"""
Diseña un método que reciba como parámetro 10 números, los almacene en una lista y retorne la media de estos.
"""

def media_lista():
    lista = [1,3,5,7,9,10]
    suma = 0
    for i in lista:
         suma = suma+i
    return print(suma/len(lista))

#EJERCICIO 6

"""
Diseña un método que reciba como parámetro una lista de 10 letras,
 y retorna el número total de vocales que hay dentro de esta.
"""

def total_vocales():
    lista = ['a','e','i','o','o','u','u','u','u','u','u']
    vocal1 = 0
    vocal2 = 0
    vocal3 = 0
    vocal4 = 0
    vocal5 = 0

    for vocales in lista:
        if (vocales == 'a'):
            vocal1 +=1
        if (vocales == 'e'):
            vocal2 +=1
        if (vocales == 'i'):
            vocal3 += 1
        if (vocales == 'o'):
            vocal4 += 1
        if (vocales == 'u'):
            vocal5 += 1
    return print("\033[4;35;47m" +'Existen: ','\n', vocal1, 'a','\n', vocal2, 'e','\n', vocal3, 'i','\n', vocal4,'0','\n', vocal5, 'u','\n')



#EJERCICIO 7

"""
Diseña un método que reciba como parámetro una lista de 10 letras, y retorne una lista nueva con el código ASCII de cada letra ingresada.
"""

def codigo_Ascii():
    lista = ['a','b','c','d','f','g','h','i','j','k']

    print(chr(27) + "[1;33m" + "Lista de Codigos ASCII  de tu lista \n")
    for i in lista:
        print("\033[4;35;47m" , 'Codigo  ASCII de :', i, '\t', 'Es ', ord(i), '\n')
        #print(str(lista[i]))



#EJERICIO 8

"""
Diseña un método que reciba como parámetro una lista de 5 números, los almacene en una lista y retorne el menor número.
"""

def menor_lista_1(lista):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor

    return ('El numero menor de tu lista es :',menor)



#EJERCICIO 9

"""
Diseña un método que reciba como parámetro una lista de 5 números, y retorne la suma del menor número con el mayor número.
"""
def suma_lista_numeros(lista):
    menor = lista[0]
    mayor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
        if valor > mayor:
            mayor = valor

    return ('La suma  de tu lista es :', menor+mayor, 'El numero mayor', mayor, 'El numero menor', menor)


#EJERCICIO 10

"""
Diseña un método que reciba como parámetro una lista de 10 números y retorne una lista sin los números que sean divisibles por 2.
"""

def lista_divisible(lista):
    lista_nueva = []
    contador = 2
    for i in lista:
        if (i%contador !=0):
            i = i#REVISAR GUARADADO DE ELEMENTO
            lista_nueva.append(i)
    print("\033[4;35;47m" +'Tus numeros de la lista  que no son divisibles por 2 :')
    return lista_nueva



#EJERCICIO 11

"""
Diseña un método que reciba dos parámetros, el primero es una lista con 10 números y el segundo un número (x) entre 1 y 10.
 Debe retornar la lista solo con los números que sean divisibles entre el segundo parámetro (x)
"""

def lista_divisible_dos(lista,x):
    lista_nueva = []
    for elemento in lista:
        if (x == 1):
             elemento = elemento
             lista_nueva.append(elemento)
        if (x == 2):
            if (elemento%x ==0):
                elemento = elemento
                #print(elemento)
                lista_nueva.append(elemento)
            #print(chr(27) + "[1;33m" + 'Tus numeros de la lista  que  son divisibles por  :', x)
        if (x == 3):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)
        if (x == 4):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)
        if (x == 5):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)
        if (x == 6):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)
        if (x == 7):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)
        if (x == 8):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)
        if (x == 9):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)
        if (x == 10):
            if (elemento%x ==0):
                elemento = elemento
                # print(elemento)
                lista_nueva.append(elemento)

    return lista_nueva




#EJERCICIO 12

def nueva_lista(lista):
    lista_nueva = []
    print("\033[4;35;47m" + 'Lista Original', lista)
    contador = 2
    for elemento in lista:
        if (elemento % contador == 0):
            elemento = elemento  # REVISAR GUARADADO DE ELEMENTO
            lista.remove(elemento)

    print()
    print("\033[4;35;47m" + 'Tus numeros de la lista  que  son divisibles por 2 fueron quitados:')
    return lista


#EJERCICIO 13






#EJERCICIO 14

"""
Diseña un método que reciba como parámetro una lista de 10 números, reemplace los múltiplos de 3 por una “x” y retorne misma lista.
"""

def multiplos_tres(lista):

    divisor = 3
    indice = 0

    for elemento in lista:
         if (elemento%divisor ==0):
            elemento = lista[elemento]#REVISAR ESTA LINEA DE CODIGO
            lista.insert(elemento, 'x')

    return lista




#EJERCICIO 15

"""
Diseña un método que reciba como parámetro una lista con 10 números, 
y retorne una lista nueva con solo los primeros 5 números de la lista original. 
(el método len() permite saber la cantidad de elementos en una lista).

"""


def lista_quince(lista):
    lista_nueva = []

    contador = lista[0]



    while (contador < lista.index(4)):
        contador = contador
        lista_nueva.append(contador)
    return lista_nueva










#dos_listas()

#lista_multiplicadora()
#media_lista()
#total_vocales()
#lista_ordenada()
#codigo_Ascii()

lista1 = [20,5,6,4,152,7,3,2,11]
#x = int(input("Ingresa tu valor x para saber "))
print (lista_quince(lista1))