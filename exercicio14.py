#Solicita os dados
valor_total = float(input("Insira o valor total da compra:"))

#Calcula o valor à vista
valor_aVista = valor_total - (valor_total * 0.10) 

#Calcula o valor parcelado em 3x
valor_parcelado = valor_total / 3

#Exibe o resultado
print("O valor à vista com desconto é de R$ {:.2f}".format(valor_aVista))
print("O valor de cada parcela em 3x sem juros é de R$ {:.2f}".format(valor_parcelado))