#-----------------------------------Exercicio 1------------------------------------

def formatar_saudacao(nome: str, cidade: str):
    return f"Olá {nome}, seja bem vinda a {cidade}!"

if __name__ == '__main__':
        saudacao = formatar_saudacao("Alice", "Porto alegre")
        print(saudacao)

#------------------------------------Exercício 2------------------------------------
def calcular_perimetro(largura: float, altura: float):
      perimetro = 2 * (largura + altura)
      return perimetro

if __name__ == '__main__':
      perimetro = calcular_perimetro (5.0, 10.0)
      print (f"O preímetro é: {perimetro}")

#-----------------------------------Exercício 3--------------------------------------

def fahrenheit_para_celsius (temp_f: float, ):
      temp_celsius = (temp_f - 32) * (5 / 9)
      return temp_celsius

if __name__ == '__main__':
      temp_celsius = fahrenheit_para_celsius (68)
      print (f"A temperatura é: {temp_celsius}°C")

#-------------------------------------Exercicio 4 ------------------------------------

def calcular_gorjeta_por_pessoa (conta: float, porcentagem_gorjeta: float, pessoas: int):
      gorjeta_total = conta * (porcentagem_gorjeta / 100)
      gorjeta_individual = gorjeta_total / pessoas
      return  gorjeta_individual
      

if __name__ == '__main__':
      gorjeta_individual = calcular_gorjeta_por_pessoa(100.0, 15, 3)

      print(f"A porcentagem de gorjeta por pessoa é de {gorjeta_individual}%")
