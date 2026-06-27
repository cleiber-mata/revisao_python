imposto_venda = 0.1
resposta = "S" 

while resposta == "S":
    print("\n========== CÁLCULO DE IMPOSTO SOBRE VENDAS ==========")
    print("Digite o valor da venda: ")
    valor_bruto_venda = float(input())
    
    valor_liquido_venda = valor_bruto_venda * (1 + imposto_venda)
    print(f"Valor da Venda com Imposto: R$ {valor_liquido_venda:.2f}")
    print(f"Valor do Imposto: R$ {valor_bruto_venda * imposto_venda:.2f}\n")
   
    resposta = input("Deseja calcular o valor líquido de outra venda? (S/N): ").strip().upper()

print("\nEncerrando o programa. Obrigado!\n")