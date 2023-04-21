salario = float(input("Digite o valor do salario:"))
horas = float(input("Digite a quantidade de horas trabalhadas:"))


operaçao1 = salario * horas
reajuste = operaçao1 + (operaçao1 * 0.12)

print("O resultado do salario com reajuste é:", reajuste)

