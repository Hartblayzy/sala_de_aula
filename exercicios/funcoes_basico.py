#--------------------------------------Exercício 1 -----------------------------------

def formatar_saudacao(nome: str, cidade: str):
    return f"Olá {nome}, seja bem vinda a {cidade}!"

#--------------------------------------Exercício 2 -----------------------------------

def calcular_perimetro(largura: float, altura: float):
      perimetro = 2 * (largura + altura)
      return perimetro

#--------------------------------------Exercício 3 -----------------------------------

def fahrenheit_para_celsius (temp_f: float, ):
      temp_celsius = (temp_f - 32) * (5 / 9)
      return temp_celsius

#--------------------------------------Exercício 4 -----------------------------------

def calcular_gorjeta_por_pessoa (conta: float, porcentagem_gorjeta: float, pessoas: int):
      gorjeta_total = conta * (porcentagem_gorjeta / 100)
      gorjeta_individual = gorjeta_total / pessoas
      return  gorjeta_individual

#--------------------------------------Exercício 5 -----------------------------------

def resumo_circulo (raio: float):
      area = 3.14 * (raio ** 2)
      return area

#--------------------------------------Exercício 6 -----------------------------------

def resumo_juros_compostos (capital: float, taxa: float, anos: int):
       montante = capital * (1 + taxa / 100) ** anos
       return montante

#--------------------------------------Exercício 7 -----------------------------------

def metricas_cilindro (raio: float, altura: float):
      volume = 3.14 * (raio ** 2) * altura
      area_superficie = 2 * 3.14 * (raio ** 2) + 2 * 3.14 * raio * altura
      return volume, area_superficie

#--------------------------------------Exercício 8 -----------------------------------

def gerar_item_fatura(nome_item: str, preco: float, porcentagem_desconto: float):
      preco_final = (preco * porcentagem_desconto) / 100
      valor_desconto = preco - preco_final
      
      return valor_desconto, nome_item, preco_final

#--------------------------------------Exercício 9 -----------------------------------

def resumo_emprestimo(capital: float, taxa_anual: float, anos: int):
      #A taxa precisa estar em meses, logo 
      meses = anos * 12
      taxa_por = taxa_anual / 100
      taxa_mensal = ((1 + taxa_por) ** (1/12)) - 1



      pmt = capital * (taxa_mensal *(1 + taxa_mensal) ** meses) / ((1 + taxa_mensal) ** meses -1)

      
      total_pago = pmt * meses
      return pmt, total_pago





if __name__ == '__main__':

      print("=" * 50)
      print("            EXERCÍCIOS DE PYTHON")
      print("=" * 50)

#RESULTADO 1

      print("\n[ Exercício 1 ]")
      print("-" * 50)


      saudacao = formatar_saudacao("Alice", "Porto alegre")
      print(saudacao)


#RESULTADO 2

      print("\n[ Exercício 2 ]")
      print("-" * 50)

      
      perimetro = calcular_perimetro (5.0, 10.0)
      print (f"O preímetro é: {perimetro}")

#RESULTADO 3

      print("\n[ Exercício 3 ]")
      print("-" * 50)

      temp_celsius = fahrenheit_para_celsius (68)
      print (f"A temperatura é: {temp_celsius}°C")

#RESULTADO 4

      print("\n[ Exercício 4 ]")
      print("-" * 50)


      gorjeta_individual = calcular_gorjeta_por_pessoa(100.0, 15, 3)
      print(f"A porcentagem de gorjeta por pessoa é de {gorjeta_individual}%")

#RESULTADO 5

      print("\n[ Exercício 5 ]")
      print("-" * 50)

      area = resumo_circulo (3)
      print (f"Um círculo com raio 3 tem uma área de {area}.")

#RESULTADO 6

      print("\n[ Exercício 6 ]")
      print("-" * 50)

      juros = resumo_juros_compostos(taxa=5.0, capital=1000.0, anos=3)
      print(f"Após 3 anos, R$ 1000 cresce para R${juros:.2f}")

 #RESULTADO 7

      print("\n[ Exercício 7 ]")
      print("-" * 50)     

      volume, area_superficie = metricas_cilindro(altura=5.0, raio=2.0)
      print (f"Volume do Cilindro: {volume:.2f} | Área de superfície: {area_superficie:.2f}")

#RESULTADO 8

      print("\n[ Exercício 8 ]")
      print("-" * 50)  

      fatura, nome_item, economia = gerar_item_fatura(nome_item="Teclado", porcentagem_desconto= 15.0, preco= 80.0 )
      print (f"Item: {nome_item} | Preço final: R${fatura} (Você economizou R$ {economia})")
      
#RESULTADO 9

      print("\n[ Exercício 9 ]")
      print("-" * 50)  

      emprestimo, parcela_mensal, total_pago = resumo_emprestimo(capital= 10000.0, anos=3, taxa_anual=6.0)
      print(f"Emprestimo: R$ {emprestimo} | Parcela Mensal: R$ {parcela_mensal} | Total Pago: R$ {total_pago}")
