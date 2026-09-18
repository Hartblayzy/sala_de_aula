def fizz_buzz (numero: int):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Fizzbuzz'
    
    elif numero % 3 == 0:
        return 'Fizz'
    
    elif numero % 5 == 0:
        return 'Buzz'
    
    else:
        return numero
    
#--------------------------------------Exercício 1 -----------------------------------

def verificar_maioridade(idade:int):
    if idade >= 18:
        return 'Maior de idade'
    return 'Menor de idade'

#--------------------------------------Exercício 2 -----------------------------------

def verificar_paridade(numero: int):
    if numero % 2 == 0:
        return 'Par'
    return 'ímpar'

#--------------------------------------Exercício 3 -----------------------------------

def classificar_numero(numero: int):
    if numero < 0:
        return 'Negativo'
    elif numero > 0:
        return "Positivo"
    else:
        return 'zero'
    
#--------------------------------------Exercício 4 -----------------------------------

def calcular_resultado(nota1: float, nota2: float):
    media = (nota1 + nota2) / 2

    if media >= 7:
        return 'Aprovado'
    return 'Reprovado'

#--------------------------------------Exercício 5 -----------------------------------

def maior_de_dois (a: float, b: float):
    if a>b:
        return 'O primeiro é maior'
    elif a<b:
        return 'O segundo é maior'
    else:
        return 'São iguais'

#--------------------------------------Exercício 6 -----------------------------------

def calcular_desconto(valor_compra: float, e_cliente_vip: bool):
    desconto_maior = (valor_compra * 15) / 100
    desconto_menor = (valor_compra * 5) / 100

    if valor_compra > 200 or e_cliente_vip:
        return valor_compra - desconto_maior
    
    return valor_compra - desconto_menor
    
#--------------------------------------Exercício 7 -----------------------------------

def conceito_nota(nota: float):
    if nota >= 9 and nota <= 10:
        return "A"
    
    elif nota >=7 and nota <=8.9:
        return "B"
    
    elif nota >=5 and nota <=6.9:
        return "C"
    
    return "F"

#--------------------------------------Exercício 8 -----------------------------------

def tipo_triangulo (a: int, b: int, c: int):
    if a+b>c and a+c>b and b+c>a:
        if a!=b!=c:
            return "Escaleno"
        elif a==b==c:
            return "Equilátero"
        else:
            return "Isóceles"
    return "Não é um triângulo"
        
#--------------------------------------Exercício 9 -----------------------------------

def calcular_imposto (salario: float):
    if salario <= 2000:
        return 0
    
    elif salario <= 4000:
        return (salario - 2000) * 0.10
    
    else:
        salario > 4000
        return (2000 * 0.10) + ((salario - 4000)* 0.20)
    

#--------------------------------------Exercício 10 -----------------------------------

def e_bissexto (ano: int):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    return False

def avaliar_estudante (p1: float, p2: float, freq: float, trabalho: bool):
    media = (p1 + p2) / 2
    if freq < 75:
        return 'Reprovado por Frequência'
    if freq >= 75:
        if media >= 7.0:
            return 'Aprovado direto'
        if media >= 5 and media <= 6.9 and trabalho==True:
            nova_media = media + 1
            if nova_media >= 7:
                return 'Aprovado com Trabalho Extra'
            elif nova_media >= 5 and nova_media <= 6.9:
                return 'Exame Final'    
        return 'Reprovado por nota'


if __name__ == '__main__':        
      
    numero = fizz_buzz (450)
    print (numero)

    print("\n[ Exercício 1 ]")
    print("-" * 50)

    idade= verificar_maioridade(12)
    print(idade)

    print("\n[ Exercício 2 ]")
    print("-" * 50)
    
    par = verificar_paridade (56)
    print (par)

    print("\n[ Exercício 3 ]")
    print("-" * 50)

    neg_pos = classificar_numero (-5)
    print(neg_pos)

    print("\n[ Exercício 4 ]")
    print("-" * 50)

    media = calcular_resultado (nota2=6.5, nota1=5)
    print(media)

    print("\n[ Exercício 5 ]")
    print("-" * 50)

    compara = maior_de_dois(b=4, a=4)
    print(compara)

    print("\n[ Exercício 6 ]")
    print("-" * 50)

    valor = calcular_desconto(150, True)
    print (f'Valor final: R$ {valor:.2f}')

    print("\n[ Exercício 7 ]")
    print("-" * 50)

    conceito = conceito_nota(4)
    print (conceito)

    print("\n[ Exercício 8 ]")
    print("-" * 50)

    triangulo = tipo_triangulo (5, 5, 5)
    print(triangulo)

    print("\n[ Exercício 9 ]")
    print("-" * 50)

    imposto = calcular_imposto (5000)
    print (f'Valor do imposto: R$ {imposto:.2f}')

    print("\n[ Exercício 10 ]")
    print("-" * 50)

    ano = e_bissexto (2000)
    print (ano)


    nota_aluno = avaliar_estudante (6.0, 6.5, 80, False)
    print(nota_aluno)