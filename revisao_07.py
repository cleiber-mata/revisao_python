cotacao_dolar = float(input("Digite a cotação do dólar: R$ "))
valor_reais = float(input("Digite o valor em reais: R$ "))

def converter_para_dolar(valor_reais):
    valor_em_dolar = valor_reais / cotacao_dolar
    return valor_em_dolar

valor_em_dolar = converter_para_dolar(valor_reais)
print(f"\n========== CONVERSÃO DE MOEDA ==========")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Cotação do dólar: R$ {cotacao_dolar:.2f}")
print(f"O valor em dólares é: U$ {valor_em_dolar:.2f}\n")