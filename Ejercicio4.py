"Diseñe un algoritmo que calcule el factorial de un número ingresado desde teclado"
num=int(input("Ingrese número para calcular el factorial: ")) #Declara la variable número, le asigna un valor de tipo entero, y con el input imprime letrero y pide dato
fact = 1 #Se declara la variable que luego convierten en funcion, si pongo igual 0, por la forma en que más adelante se crea la función todo tambien se vuelve 0
if num<=0:
    print("Por favor ingresar números enteros positivos")
else: 
    for i in range(num+1):#se incrementa el num en una unidad porque python toma el range o rango como indice, por lo cual inicia contando la posición 0 como una unidad
        if i !=0:#condición para que no todo se vuelva 0
            fact = fact * i#vuelvo mi variable una función 
    print (fact)#imprimo el resultado