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


    if valor_compra > 200 or e_cliente_vip == True:
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
        elif a==a and b==b and c==c:
            return "Equilátero"
        else:
            return "Isóceles"









if __name__ == '__main__':        
      
    numero = fizz_buzz (450)
    print (numero)


    idade= verificar_maioridade(12)
    print(idade)
      

    par = verificar_paridade (56)
    print (par)

    neg_pos = classificar_numero (-5)
    print(neg_pos)

    media = calcular_resultado (nota2=6.5, nota1=5)
    print(media)


    compara = maior_de_dois(b=4, a=4)
    print(compara)

    valor = calcular_desconto(150, True)
    print (f'Valor final: R$ {valor:.2f}')

    conceito = conceito_nota(4)
    print (conceito)

    triangulo = tipo_triangulo (1, 5, 5)
    print(triangulo)