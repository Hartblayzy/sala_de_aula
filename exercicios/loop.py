def dobrar (numeros: list):
    for num in numeros:
        num = num * 2
        print (num)
#--------------------------------------Exercício 1 -----------------------------------

def filtrar_pares (numeros: list):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append (num)
    return pares

#--------------------------------------Exercício 2 -----------------------------------

def contar_negativos (numeros: list):
    negativos = []
    for numero in numeros:
        if numero < 0:
            negativos.append(numero)

    return len(negativos)

#--------------------------------------Exercício 3 -----------------------------------

def somar_maiores_que (numeros: list, limite: int):
    soma = []
    
    for numero in numeros:
        if numero > limite:
            soma.append(numero)
            total = 0
            for numero in soma:
                total += numero
    return total

#--------------------------------------Exercício 4 -----------------------------------

def zerar_negativos (numeros: list):
    zero = numeros.copy()
    
    for numero in zero:
        if numero < 0:
            troca_por_zero = zero.index(numero)
            zero[troca_por_zero] = 0
    return zero

#--------------------------------------Exercício 5 -----------------------------------

def contem_valor(lista:list, alvo:str):
    while alvo in lista:
        return True
    return False

#--------------------------------------Exercício 6 -----------------------------------

def contar_aprovados (notas: list):
    aprovados = []
    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)

    return f'Aprovados : {len(aprovados)}'

#--------------------------------------Exercício 7 -----------------------------------

def filtrar_palavras_curtas(palavras: list, tamanho_maximo: int):
    palavras_curtas = []
    for palavra in palavras:
        if len(palavra) <= tamanho_maximo:
            palavras_curtas.append(palavra)
    return palavras_curtas

#--------------------------------------Exercício 8 -----------------------------------

def separar_pares_impares(numeros:list):
    pares = 0
    impares = 0 

    for numero in numeros:
        if numero % 2 != 0:
            impares += 1

        else:
            pares += 1
    
    return f'Pares: {pares} | Ímpares: {impares}'

#--------------------------------------Exercício 9 -----------------------------------

def encontrar_extremos(numeros: list):
    lista = numeros.copy()
    list_sort = lista.sort()

    menor_maior = lista[0] , lista [-1]
    return menor_maior

#--------------------------------------Exercício 10 -----------------------------------
    
def simular_saque(saldo_inicial: float, saques: list):
    i = 0
    while i < len(saques):
        if saldo_inicial >= saques[i]:
            saldo_inicial-= saques[i]
        i+= 1
    return saldo_inicial

#--------------------------------------Exercício 11 -----------------------------------

def remover_duplicados (lista: list):
    lista_sem_duplos = []
    for num in lista:
        if num not in lista_sem_duplos:
            lista_sem_duplos.append(num)
    
    return lista_sem_duplos

#--------------------------------------Exercício 12 -----------------------------------

def calcular_media_positivos(numeros: list):
    positivos = []
    valor = 0
    divisor = 0
    if not  numeros:
        return 0
    for num in numeros:
        if num > 0:
            positivos.append(num)
            valor += num
            divisor += 1      
    return valor / divisor

    
    
            






 






if __name__ == '__main__':

    dobra = dobrar([1, 2, 3, 4, 5])
    print (dobra)

    print("\n[ Exercício 1 ]")
    print("-" * 50)

    pares = filtrar_pares ([1, 2, 3, 4, 5, 6])
    print (pares)

    print("\n[ Exercício 2 ]")
    print("-" * 50)

    negativos = contar_negativos([10, -3, 0, -5, 8, -1])
    print(negativos)

    print("\n[ Exercício 3 ]")
    print("-" * 50)

    soma = somar_maiores_que([10, 5, 20, 3, 15], 8)
    print (soma)

    print("\n[ Exercício 4 ]")
    print("-" * 50)

    trocar_zeros = zerar_negativos ([4, -2, 7, -9, 0])
    print (trocar_zeros)

    print("\n[ Exercício 5 ]")
    print("-" * 50)

    contem_valor = contem_valor(["maçã", "banana", "uva"], "goiaba")
    print (contem_valor)

    print("\n[ Exercício 6 ]")
    print("-" * 50)

    conta_aprovado = contar_aprovados ([8.5, 5.0, 7.0, 6.5, 9.0])
    print(conta_aprovado)

    print("\n[ Exercício 7 ]")
    print("-" * 50)

    palavras_curtas = filtrar_palavras_curtas (["sol", "computador", "python", "mar"], 6)
    print (palavras_curtas)

    print("\n[ Exercício 8 ]")
    print("-" * 50)

    separar_par_impar = separar_pares_impares ([1, 2, 3, 4, 5])
    print (separar_par_impar)

    print("\n[ Exercício 9 ]")
    print("-" * 50)

    lista_maior_menor = encontrar_extremos([14, 2, 35, -4, 20])
    print (lista_maior_menor)

    print("\n[ Exercício 10 ]")
    print("-" * 50)

    saldo = simular_saque (200, [50, 100, 80, 30])
    print (saldo)

    print("\n[ Exercício 11 ]")
    print("-" * 50)

    sem_duplos = remover_duplicados ([1, 3, 2, 3, 1, 4, 2])
    print (sem_duplos)

    print("\n[ Exercício 12 ]")
    print("-" * 50)

    media_positivos = calcular_media_positivos([-5, 10, -2, 20, 30])
    print (media_positivos)