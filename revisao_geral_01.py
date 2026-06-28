

def calcular_faturamento():
    mensalidade_bruta    = float(input("Digite o valor da mensalidade bruta: "))
    quantidade_meses     = int(input("Digite a quantidade de meses: "))
    faturamento_liquido = (mensalidade_bruta * quantidade_meses) * 0.95
    manutencao_servidor = mensalidade_bruta * 0.05
    return faturamento_liquido, manutencao_servidor

resposta = "S"
while resposta == "S":

    nome_usuario = input("Digite o nome do usuário: ").strip().title()
    email_usuario = input("Digite o e-mail do usuário: ").strip().lower()
    mensalidade = float(input("Digite o valor da mensalidade: "))
    meses_ativos = int(input("Digite a quantidade de meses ativos: "))

    faturamento, manutencao = calcular_faturamento()

    cliente_data = {
        "nome": nome_usuario,
        "email": email_usuario,
        "faturamento_liquido": faturamento
    }

    print("\n========== RESUMO DO CLIENTE ==========")
    for chave, valor in cliente_data.items():
        print(f"{chave.capitalize()}: {valor}")
    if faturamento >= 500:
        print(f"nome: {cliente_data['nome']}: CLIENTE VIP - SUPORTE PREMIUM CORRESPONDENTE")
    else:
        print(f"nome: {cliente_data['nome']}: CLIENTE PADRÃO - SUPORTE BÁSICO")

    resposta = input("\nDeseja cadastrar outro cliente (S/N)? ").strip().upper()

print("\nEncerrando o programa. Obrigado!\n")