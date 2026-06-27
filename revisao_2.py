# 1. Entradas
vendedor = input("Nome do vendedor: ")
total_vendas = float(input("Digite o total de vendas: R$ "))

# 2. Estrutura Condicional (Complete os espaços abaixo)
if total_vendas >= 12000:
    desempenho = "Excelente - Bônus Ouro"
elif total_vendas >= 7500:
    desempenho = "Bom - Bônus Prata"
elif total_vendas >= 3000:
    desempenho = "Bom - Bônus Bronze"
else:
    desempenho = "Abaixo da Meta - Sem Bônus"

# 3. Saída Formatada
print(f"\nColaborador: {vendedor.strip().title()}")
print(f"Total Vendido: R$ {total_vendas:.2f}")
print(f"Status do Desempenho: {desempenho}")