"""
Nombre: Calculadora
Entradas: operacion, op1, op2
Salidas: Resultado de una operacion 
Restricciones: Parámetros de tipo entero. Parámetro operación solamente valores del 1 al 4.
               Operadores de tipo entero.
"""

def calculadora (operacion,op1,op2):
    if not isinstance (operacion, int):
        return "Error: El operadore debe ser de tipo entero"
    if not isinstance(op1,int):
        return "Error: El op1 debe ser entero"
    if not isinstance(op2,int):
        return "Error: El op2 debe ser entero"
    if (op1 and op2 < 1) and (op1 and op2 > 4):
        return "Op1 y Op2 deben estar en el rango de 1 a 4"

    return calculadora_Aux(operacion,op1,op2)

def calculadora_Aux(operacion,op1,op2):
    if (operacion == 1):
        return op1 + op2
    if (operacion == 2):
        return op1 - op2
    if (operacion == 3):
        return op1 * op2
    if (operacion == 4):
        if (op2 == 0):
            return "No es posible la división entre 0"
        return op1 / op2

"""
Nombre: contadorDigitos
Entradas: num, digito
Salidas: Retorna el número de veces que el dígito aparece en el número.
Restricciones: Parámetros de tipo entero. Parámetro digito debe ser menor
               a 10 y mayor igual a 0.
               
"""

def contadorDigitos(num,digito):
    if not isinstance(num,int):
        return "Error: El num debe ser entero"
    if not isinstance(digito,int):
        return "Error: El digito debe ser entero"
    if(digito < 0 or digito > 10):
        return "Error: El digito debe estar en el rango de 0 a 10" 
    if(num == 0):
        return 1

    return contadorDigitos_Aux(num,digito)

def contadorDigitos_Aux(num,digito):
    i = 0
    resultado = 0
    
    while (num > 0):
        resultado = num % 10
        if(resultado == digito):
            i += 1
        num = num // 10

    return i



"""
Nombre: sumatoria_V2
Entradas: inicio, fin, distancia, excepcion.
Salidas: suma total de los números desde el parámetro inicio hasta el final.
Restricciones: Todos parámetros deben ser de tipo entero.
Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0.
Los valores de inicio y fin deben ser positivos
Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
Si excepcion es igual a cero, se debe ignorar este valor.

"""
def sumatoria_V2(inicio, fin, distancia, excepcion):
    if not isinstance(inicio,int):
        return "Error: El inicio debe ser entero"
    if not isinstance(fin,int):
        return "Error: El fin debe ser entero"
    if not isinstance(distancia,int):
        return "Error: El fin debe ser entero"
    if not isinstance(excepcion,int):
        return "Error: El excepcion debe ser entero"
    if (distancia and excepcion < 0 or distancia and excepcion > 10):
        return "Error: La distancia y la excepcion deben estar en el rango de 0 a 10"
    if (distancia == -distancia):
        if(fin < inicio):
            return "Error: Fin debe ser menor a inicio"
        return "Error: "
    
     
     





