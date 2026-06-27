valor_bonificacao = 10503
quantidade_analistas = 4
valor_por_analista = valor_bonificacao // quantidade_analistas
fundo_reserva = valor_bonificacao % quantidade_analistas
verificacao_bonificacao = valor_por_analista * quantidade_analistas + fundo_reserva

print("\n---Relatório de Bonificação---")
print(f"\nValor da bonificação: R$ {valor_bonificacao:.2f}")
print(f"Valor por analista: R$ {valor_por_analista:.2f}")
print(f"Fundo de reserva: R$ {fundo_reserva:.2f}")
if valor_bonificacao == verificacao_bonificacao:
    print("A verificação da bonificação está correta.\n")

