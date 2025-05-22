#creamos un programa  que busca llevar el registro de un inventario de una tienda.

#creamos la variable "inventario" donde se almacenaran los diccionarios con las claves y los valores.
# en este caso agregamos un ejemplo de posibles productos que nos ayudaran a validar quue el programa
# funciona correctamente. 
inventario = {"manzana":(1500, 10),
              "mango" : (1000, 5),
              "pera" : (1200, 5),
              "fresa" : (500, 5),
              }
#---------------funciones----------
#iniciamos definiendo las funciones que nos ayudaran a realizar cada tarea que se debe llevar en el inventario.
#-----------------opcion 1---------------

# Esta función se encarga de agregar un nuevo producto al inventario.
def nuevo_producto():
    #le pedimos al usuario que ingres el producto para validar si esta antes de agregarlo.
    producto= input("ingresa el nombre del producto: ")    
    if producto in inventario:
        print(f"\033[91m❌ El prodcuto: {producto} ya se encuentra en el inventario\033[0m")
        print(inventario[producto])
    else: #Si el producto no está en el inventario, vamos a pedirle el precio y la cantidad.
        try:
            precio = float(input("ingresa el precio, NOTA: deben ser digitos numericos mayores a cero: "))
            if precio <= 0:  # Verificamos que el precio que ingresó sea mayor que cero.
                print("Error, el precio debe ser mayor a 0")
            
            else:
                cantidad = int(input("ingresa la cantidad, NOTA: deben ser digitos numeriocos mayores a 0: "))
                if cantidad <= 0:  # Verificamos que la cantidad sea al menos 1.
                    print("Error, la cantidad debe ser igual o mayor a 1 unidad.")
                else: #si el precio y la cantidad son se ingresan bien, entonces agregamos el producto al inventario .
                    inventario2= {producto:(precio, cantidad)}
                    inventario.update(inventario2)
                    print(f"\033[92m✅ El producto: {producto} ha sido agregado correctamente\033[0m")
                    print(inventario)
        except ValueError: #si el usuario ingresa un caracter indevido le mostramos un mensaje de error.
            print("Error, ingresaste letras o caracteres invalidos. debes ingresar numeros")

#----------------opcion 2----------------
# Esta función permite buscar un producto en el inventario.
def buscar_producto():
    consultar = input("ingresa el producto que deseas buscar: ")
    if consultar in inventario:
        #validamos que el producto se encuentre en el inventario y le mostramos sus valores especificamente.
        print(f"\033[92m✅ El producto: {consultar} se encuentra en el inventario\033[0m")
        print(f"precio: {inventario[consultar][0]}")
        print(f"cantidad: {inventario[consultar][1]}")
    else:   #si el producto no se encuentra se lo hacemos saber al usuario.
        print(f"\033[91m❌ El producto: {consultar} no se encuentra en en inventario\033[0m")
       
#--------------opcion 3------------------
# Esta función permite cambiar el precio de un producto que ya existe.
def actualizar_precios(): # Primero, le mostramos al usuario los productos que hay en el inventario.
    print(f"Productos en el inventario:{inventario}")

    actualizar = input("Ingresa el producto al que vas a actualizar el precio: ")
    if actualizar in inventario.keys():
        #separamos los valores del producto a actualizar porque solo se va a actualizar el precio.
        for producto, precio_cant in inventario.values():
            p=producto
            c=precio_cant
        print(f"{actualizar}: precio = {p}, cantidad = {c}")
            
        try: # Le pedimos al usuario el nuevo precio.
            nuevo_precio = float(input("Nuevo precio: "))
            if nuevo_precio <= 0:  # Verificamos que el nuevo precio sea mayor que cero.
                print("Error, el precio debe terner digitos numericos mayores a 0.")
            
            else:
                _, cantidad = inventario[actualizar] 
                inventario[actualizar] = (nuevo_precio, cantidad) 
                print(f"\033[92m✅ Precio actualizado correctamente para {actualizar}\033[0m")
                # Mostramos un mensaje indicando que el precio se actualizó correctamente.        
        except ValueError:
            print("Error, ingresaste letras o caracteres invalidos. debes ingresar numeros")
            
    else: # Si el producto que ingresó no existe en el inventario, le mostramos un mensaje de error.
        print(f"\033[91m❌ El producto '{actualizar}' no se encuentra en el inventario.\033[0m")

#------------------opcion 4----------------
# Esta función permite eliminar un producto del inventario.
def eliminar_producto():
    print(inventario) # Primero, le mostramos al usuario el inventario actual para que decida que producto eliminar.
    eliminar = input("ingresa el producto que deseas eliminar: ")
    if eliminar in inventario: # Verificamos si el producto que quiere eliminar está en el inventario.
        inventario.pop(eliminar) # Si está, usamos la función 'pop()' para eliminar el producto del diccionario.
        print(f"\033[92m✅ El producto: {eliminar} se elimino correctamente.\033[0m")
        print(f"estado del inventario: {inventario}")
    else:
        print(f"\033[91m❌ El producto: {eliminar} no existe en el inventario\033[0m")
        print(inventario)

#------------------opcion 5-----------------
# Esta función calcula el valor total de todos los productos en el inventario.
def acumulado(): 

    contador = 0 # Creamos una variable para guardar la suma total, inicializada en cero.
# Recorremos todos los valores (precio y cantidad) que hay en el inventario.
    for precio, cantidad in inventario.values():
        P= precio
        C= cantidad
        #definimos una funcion pequeña "lambda" que se encargara de multiplicar el precio ṕr la cantidad.
        multiplicacion_p_c =lambda X , Y : X * Y 
        resultado_P_C = multiplicacion_p_c(P,C) 
        contador += resultado_P_C   # Sumamos el resultado de la multiplicación al contador total por cada producto en el inventario.
#le mostramos al usuario explicitamente los productos y sus valores con el resultado del precio de todos ellos.
    for id, valor in inventario.items():
        print(f"Producto: {id } - precio: {valor[0]} - cantidad: {valor[1]}")
    print( )
    print(f"Total de todos los productos en el inventario:\033[92m ${contador:.2f}\033[0m")

#-------------INICIA------------------
#creamos un ciclo while y le mostramos el menu en el que el usuario podra interactuar hasta que decida salir.
while True:
    print( )
    print("\033[92m---------INVENTARIO DIGITAL-----------\n\033[0m")
    print("Menu principal:\n")
    print("1: Añadir productos")
    print("2: Consultar productos")
    print("3: Actualizar precios")
    print("4: Eliminar productos")
    print("5: Calcular el valor del inventario")
    print("6: Salir\n")

    opcion= input("Elige una opcion entre 1 - 6: ") # Le pedimos al usuario que elija una opción.
    
    # Dependiendo de la opción que elija el usuario, llamamos a la función correspondiente.
    if opcion == "1":
        print("Añadir productos.")
        nuevo_producto()
        
    elif opcion == "2":
        print("Consultar producto")
        buscar_producto()

    elif opcion == "3":
        print("Actualizar precios")
        actualizar_precios()
    
    elif opcion == "4":
        print("Eliminar productos")
        eliminar_producto()
    
    elif opcion == "5":
        print("Calcular valor")
        acumulado()
        
    elif opcion == "6":
        print("Gracias por usar el inventario digital.\n" 
          "Feliz dia")
        break # Si elige la opción 6, mostramos un mensaje de despedida y usamos 'break'
        # para salir del bucle, terminando el programa.

    else:# Si el usuario ingresa una opción que no está en el menú,
        # le mostramos un mensaje de error.
        print("\033[91m❌ Opcion invalida, intenta de nuevo\033[0m")