#Solicita ao Usuário
comprimento = float(input("Digite o comprimento do cômodo (em metros):"))
largura = float (input("digite a largura do cômodo em (metros):"))

#Calcula a área do cômodo e potência de iluminação
area = comprimento * largura
potencia = area * 18

#Exibe o resultado
print("A área do comodo é de {:.0f} m²". format(area))
print("A potência de iluminação necessária é de {:0.0f}W".format(potencia)) 
