# ==============================================================================
# DESAFIO 4: Limpeza de Dados e Expressões Matemáticas
# ==============================================================================

# 1. Dados Brutos (Simulando uma entrada do usuário com erros de digitação)
nome_cliente = "   cLeIbEr MaTa   "
email_cliente = "CLEIBER.MATA@EMPRESA.COM.BR   "

# Simulando valores de compras que o cliente fez em 3 meses
compra_mes1 = float(input("Digite o valor da compra do Mês 1: ")) # Teste com: 150.00
compra_mes2 = float(input("Digite o valor da compra do Mês 2: ")) # Teste com: 250.00
compra_mes3 = float(input("Digite o valor da compra do Mês 3: ")) # Teste com: 200.00

# 2. LIMPEZA DOS DADOS (Complete aplicando as funções corretas nas variáveis)
# O nome deve ficar sem espaços nas pontas e com as iniciais maiúsculas
nome_limpo = nome_cliente.strip().title()

# O e-mail deve ficar sem espaços nas pontas e TODO em minúsculo
email_limpo = email_cliente.strip().lower()

# 3. PROCESSAMENTO MATEMÁTICO (Precedência de Operadores)
# CORRIJA A LINHA ABAIXO: Adicione parênteses para o Python somar tudo ANTES de dividir por 3
ticket_medio = (compra_mes1 + compra_mes2 + compra_mes3) / 3

# 4. EXIBIÇÃO DO RELATÓRIO LIMPO
print("\n========== DADOS TRATADOS PARA O BI ==========")
print(f"Cliente: {nome_limpo}")
print(f"E-mail Cadastrado: {email_limpo}")
print(f"Faturamento Médio Mensal: R$ {ticket_medio:.2f}")
print("==============================================")