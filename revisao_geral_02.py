def verificar_alerta(quantidade_estoque):
    if quantidade_estoque < 5:
        return "ALERTA: ESTOQUE CRÍTICO!"
    else:
        return "Estoque Regular."

almoxarifado = []

for i in range(2):
    print(f"\n--- Cadastro do Item {i + 1} ---")
    nome_produto = input(f"Digite o nome do produto: ").strip().upper()
    quantidade = int(input(f"Digite a quantidade em estoque do produto: "))

    verificar = verificar_alerta(quantidade)

    item = {
        "produto": nome_produto,
        "quantidade": quantidade,
        "status": verificar
    }

    almoxarifado.append(item)  


print("\n==================== CONTROLE DE ESTOQUE ====================")

# 1. Cabeçalho da Tabela com larguras fixas: Produto (18 espaços), Qtd (10 espaços), Status (20 espaços)
print(f"{'PRODUTO':<18} | {'QTD':^10} | {'STATUS':<20}")
print("-" * 57)  # Cria uma linha divisória pontilhada

# 2. O Loop aplicando EXATAMENTE as mesmas larguras do cabeçalho
for registro in almoxarifado:
    print(f"{registro['produto']:<18} | {registro['quantidade']:^10} | {registro['status']:<20}")

print("=============================================================\n")