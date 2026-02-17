import time  
import os

def operacion(opcion, a, b):     
    match opcion:          
        case 1:             
            return a + b    
        case 2:             
            return a - b    
        case 3:             
            return a * b    
        case 4:             
            return a / b     
        case 5:             
            return a % b     
        case 6:             
            return a ** b  

def limpiar():
    os.system("cls")

def captura(lista_id):     
    procesos = []      

    print("-----------------------------------------------------------")     
    while True:         
        try:             
            nombre = input("Ingrese el nombre del programador: ")             
            break         
        except:             
            print("Ingresaste un valor errroneo")         

    print("Escriba la operacion que desea aplicar (numero de operacion):\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Residuo\n6.Potencia")         

    while True:         
        opcion = int(input("opcion (con numero): "))         
        if opcion > 6 or opcion < 1:             
            print("Opcion no valida")         
        else:             
            break      

    while True:   
        a = int(input("ingrese el valor de a: "))             
        b = int(input("ingrese el valor de b: "))  
        if b==0:        
            print("b no puede valer 0, ingres otros valores")             
        else:
            break   

    resultado = operacion(opcion, a, b)      

    while True:         
        tiempo = int(input("Ingrese el tiempo maximo estimado (debe ser mayor a 0): "))         
        if tiempo <= 0 :             
            print("Tiempo no valido")         
        else:             
            break      

    while True:         
        Id = int(input("Ingrese el ID: "))         
        if Id in lista_id:             
            print("ID repetido, intenta otro")         
        else:             
            lista_id.append(Id)             
            break      

    procesos.append([nombre, opcion, a, b, resultado, tiempo, Id])     
    return procesos  

def crear_lotes(procesos):     
    lotes = []     
    for i in range(0, len(procesos), 5):   
        lotes.append(procesos[i:i+5])     
    return lotes  

def mostrar(lotes):     
    procesados = []     
    tiempo = 0     
    numero_de_lotes = 0         

    while numero_de_lotes < len(lotes):         
        lote = lotes[numero_de_lotes]         
        
        print("==============================================")
        print(f"LOTE EN EJECUCION: {numero_de_lotes + 1}")
        for p in lote:
            print(f"Nombre: {p[0]} | Tiempo Maximo: {p[5]}")
        print("==============================================")

        for i in lote:             
            tiempo_estimado = 0                         

            while tiempo_estimado < i[5]:         
                
                limpiar()        

                pendientes = len(lotes) - numero_de_lotes - 1  

                print("------------------------------------------------")                 
                print(f"Lotes pendientes: {pendientes}")                 
                print(f"Lote actual: {numero_de_lotes + 1}")                 
                print("------------------------------------------------")                  

                actual = [                     
                    f"Nombre: {i[0]}",                     
                    f"Operacion: {i[1]}  Valores: {i[2]} y {i[3]}",                     
                    f"Tiempo Maximo: {i[5]}",                     
                    f"ID: {i[6]}",
                    f"Tiempo avanzado: {tiempo_estimado}",                     
                    f"Tiempo restante: {i[5]-tiempo_estimado}"                 
                ]                  

                terminados = []                 
                for j in procesados:                     
                    terminados.extend([                         
                        f"",                         
                        f"ID: {j[6]}",                         
                        f"Operacion: {j[1]}  Valores: {j[2]} y {j[3]}",                         
                        f"Resultado: {j[4]}"                     
                    ])                  

                from itertools import zip_longest                 
                ancho = 45                 
                print(f"{'PROCESO ACTUAL':^{ancho}}|{'PROCESOS TERMINADOS':^{ancho}}")                 
                print("------------------------------------------------")                 
                for izq, der in zip_longest(actual, terminados, fillvalue=""):                     
                    print(f"{str(izq):<{ancho}}|{str(der):<{ancho}}")                                  

                print()                  
                print(f"Tiempo global: {tiempo+1}")                 
                print()                   

                time.sleep(1.5)                 
                tiempo += 1                 
                tiempo_estimado += 1             

            procesados.append(i)                 

        numero_de_lotes += 1     

    print("-------------------------------")     
    print("PROCESOS COMPLETOS FINALES")     
    for i in procesados:         
        print("----------------------------------------------------------")         
        print (f"Nombre: {i[0]}")         
        print (f"ID: {i[6]}")         
        print (f"Operacion: {i[1]} Valores: {i[2]} y {i[3]} Resultado: {i[4]}")  

    input("\nPresione ENTER para finalizar...")  


while True:     
    cantidad = int(input("Ingrese el numero de procesos que desea ingresar: "))     
    if cantidad > 0:         
        break     
    else:         
        print("Debe ser mayor a 0")  

procesos = [] 
lista_id = []  

for i in range(cantidad):     
    procesos.extend(captura(lista_id))  

lotes = crear_lotes(procesos) 
mostrar(lotes)