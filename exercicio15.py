#Solicita os dados
salarioBase = float(input("Digite o valor do salário (em R$): "))

#Calcula o salário liquido 
salario_liquido = salarioBase - (salarioBase * 0.07)

#Calcula o bônus
bonus = (salarioBase * 0.05)

#Calcula o salário final
salario_final = salario_liquido + bonus

#Exibe o resultado
print("O valor do salário final a receber é: R$", salario_final)
