historico_vendas = []

print("\n========== HISTÓRICO DE VENDAS ==========")
for i in range(1, 4):
    venda = float(input(f"Digite o valor da venda {i}: R$ "))
    historico_vendas.append(venda)
print(f"Total de vendas: R$ {sum(historico_vendas):.2f}\n")