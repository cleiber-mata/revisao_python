data_venda = "   26/06/2026   "
status_pagamento = "  pAgO_nO_pIx  "

taxa_plataforma = 15.00
desconto_cupom = 5.00

valor_bruto_venda = float(input("\nDigite o valor bruto da venda: "))

data_limpa = data_venda.strip()
status_limpo = status_pagamento.strip().upper()

valor_liquido_venda = (valor_bruto_venda - taxa_plataforma) - desconto_cupom

print("\n========== RELATÓRIO DE VENDAS ==========")
print(f"Data da Venda: {data_limpa}")
print(f"Status do Pagamento: {status_limpo}")
print(f"Valor Bruto da Venda: R$ {valor_bruto_venda:.2f}")
print(f"Valor Líquido da Venda: R$ {valor_liquido_venda:.2f}\n==========================================\n")





