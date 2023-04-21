#Solicita ao Usuário
salario = float(input("Insira o valor do salário: "))
conta1 = float(input("Insira o valor da primeira conta: "))
conta2 = float(input("Insira o valor da segunda conta: "))

#Calcula o que vai sobrar do salário
restante_salario = salario - ((conta1 * 1.02) + (conta2 * 1.02)) 

#Exibe o resultado
print("O restante do salário é de: R$",restante_salario)