#Solicitação ao Usuário
peso_sacoRaçao = float(input("Insira o peso do saco de ração (em KG): "))
quantidade_fornecida = float(input("Insira a quantidade fornecida de ração aos gatos (em g): "))

# Calcula quanto restará de ração no saco após cinco dias
raçao_restante = peso_sacoRaçao * 1000 - (quantidade_fornecida * 2 * 5)

#Exibe o resultado
print("Restára {} gramas de ração, após 5 dias.".format(raçao_restante))