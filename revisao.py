# ==============================================================================
# DESAFIO: Sistema de Cadastro de Produto (Foco em Análise de Dados)
# ==============================================================================

# 1. Entrada de dados: Recebendo as informações do produto
nome_produto = input("Digite o nome do produto: ")

# CORRIJA AQUI: Converta para número inteiro (int)
quantidade = int(input("Digite a quantidade em estoque: "))

# CORRIJA AQUI: Converta para número decimal (float)
preco_unitario = float(input("Digite o preço unitário: R$ ")) 

# 2. Processamento: Calculando o valor total do estoque deste produto
# (Dica: Multiplique a quantidade pelo preço unitário)
valor_total_estoque = (quantidade * preco_unitario) # Substitua o 0 pela fórmula correta

# 3. Saída de dados: Exibindo o relatório formatado
print("\n--- RELATÓRIO DE ESTOQUE ---")
print(f"Produto: {nome_produto.strip().upper()}") # Limpa espaços e joga em maiúsculo
print(f"Quantidade: {quantidade} unidades")

# CORRIJA AQUI: Formate o valor total para exibir apenas 2 casas decimais (ex: R$ 150.50)
print(f"Valor Total em Estoque: R$ {valor_total_estoque:.2f}") # Substitua o 0.00 pela variável correta
print("----------------------------")