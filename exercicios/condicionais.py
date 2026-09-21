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
        return (2000 * 0.10) + ((salario - 4000)* 0.20)
    

#--------------------------------------Exercício 10 -----------------------------------

def e_bissexto (ano: int):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    return False
#--------------------------------------Exercício Bônus --------------------------------

def avaliar_estudante (p1: float, p2: float, frequencia: int, trabalho: bool ):
    media = (p1 + p2) / 2
    if frequencia < 75:
        return 'Reprovado por frequencia'
    if media < 5:
        return 'Reprovado por nota'
    if frequencia >= 75 and media>= 5 and media <=6.9:
        if trabalho:
            nova_media = media +1 
            if nova_media >= 7:
                return 'Aprovado com Trabalho Extra'
        return 'Exame Final'

#--------------------------------------Exercício Bônus --------------------------------

def localizar_ponto(x: int, y: int):
    if x==0 and y==0:
        return 'Origem'
    if x==0:
        return 'Eixo Y'
    if y==0:
        return 'Eixo X'
    if x>0 and y>0: 
        return 'Q1'
    if x<0 and y>0:
        return 'Q2'
    if x<0 and y<0:
        return 'Q3'
    return 'Q4'

#--------------------------------------Exercício Bônus --------------------------------

def calcular_fatura_telefone (minutos, gigas, e_estudante):
    p_base = 50

    if minutos> 100: 
        p_base = p_base + (minutos - 100) * 0.50
        
    if gigas > 5:
         p_base = p_base + (gigas - 5) * 10

    if e_estudante == True and p_base > 100:
        return f'Fatura Final: R$ {p_base - 20:.2f}'
    
    else:
        return f'Fatura Final: R$ {p_base:.2f}'


#--------------------------------------Exercício Bônus --------------------------------

def avaliar_seguro (idade: int, anos_carteira: int, historico_acidentes: int):
    if idade < 18 or anos_carteira < 1:
        return 'Não Elegível'

    if historico_acidentes > 2:
        return 'Risco Alto: Recusado'

    if historico_acidentes == 0:
        if idade >= 25 and anos_carteira >= 3:
            return 'Aprovado: Categoria VIP'
        return 'Aprovado : Categoria Padrão'
    
    if historico_acidentes ==1 or historico_acidentes == 2:
        return 'Aprovado: Categoria Alto Risco'

#--------------------------------------Exercício Bônus --------------------------------

def ordenar_tres (a: int, b: int, c: int):
    if a <= b <= c:
        return f'{a}, {b}, {c}'
    
    if a <= c <= b:
        return f'{a}, {c}, {b}'
    
    if b <= a <= c:
        return f'{b}, {a}, {c}'
    
    if b <= c <= a:
        return f'{b}, {c}, {a}'
    
    if c <= a <= b:
        return f'{c}, {a}, {b}'
    else:
        c <= b <= a
        return f'{c}, {b}, {a}'

#--------------------------------------Exercício Bônus --------------------------------

def validar_data_extenso(dia:int, mes: int, ano: int):
    
#valida o ano
    if ano < 1:
        return 'Data Inválida'
#valida o mes    
    if mes < 1 or mes >12:
        return 'Data Inválida'

    if mes == 1 or mes ==3 or mes ==5 or mes ==7 or mes ==8 or mes ==10 or mes ==12:
        if dia < 1 or dia > 31:
            return 'Data Inválida'
        
    if mes == 4 or mes ==6 or mes ==9 or mes ==11:
        if dia <1 or dia > 30:
            return 'Data Inválida'
    
    if mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia < 1 or dia > 29:
                return 'Data Inválida'

        elif dia < 1 or dia > 28:
            return 'Data Inválida'

    if mes == 1:
        nome_mes = 'Janeiro'
    if mes == 2:
        nome_mes = 'Fevereiro'
    if mes == 3:
        nome_mes = 'Março'        
    if mes == 4:
        nome_mes = 'Abril' 
    if mes == 5:
        nome_mes = 'Maio'
    if mes == 6:
        nome_mes = 'Junho'        
    if mes == 7:
        nome_mes = 'Julho'
    if mes == 8:
        nome_mes = 'Agosto'
    if mes == 9:
        nome_mes = 'Setembro'
    if mes == 10:
        nome_mes = 'Outubro'
    if mes == 11:
        nome_mes = 'Novembro'
    if mes == 12:
        nome_mes = 'Dezembro'

    return f'{dia} de {nome_mes} de {ano}'
    


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
    print (f'O número é {par}')

    print("\n[ Exercício 3 ]")
    print("-" * 50)

    neg_pos = classificar_numero (-5)
    print (f'O número é {neg_pos}')

    print("\n[ Exercício 4 ]")
    print("-" * 50)

    media = calcular_resultado (nota2=6.5, nota1=5)
    print(f'O resultado é {media}')

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

    print("\n[ Exercício Bônus ]")
    print("-" * 50)

    nota = avaliar_estudante(2, 4, 75, False)
    print(nota)

    print("\n[ Exercício Bônus 2]")
    print("-" * 50)

    ponto = localizar_ponto(-3, -5)
    print(ponto)

    print("\n[ Exercício Bônus 3]")
    print("-" * 50)

    fatura = calcular_fatura_telefone(200, 10, True)
    print (fatura)


    print("\n[ Exercício Bônus 4]")
    print("-" * 50)

    seguro = avaliar_seguro(22, 2, 2)
    print (seguro)

    print("\n[ Exercício Bônus 5]")
    print("-" * 50)

    ordenar_tres = ordenar_tres(2, 5, 5)
    print(ordenar_tres)

    print("\n[ Exercício Bônus 5]")
    print("-" * 50)

    data_extenso = validar_data_extenso(15, 9, 2026)
    print (data_extenso)