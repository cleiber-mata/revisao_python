nome_filial = str(input("Digite o nome da filial: "))
faturamento = int(input("Digite o faturamento da filial: R$ "))
metas_concluidas = int(input("Digite o número de metas concluídas: "))

kpi_filial = {
    "nome": nome_filial,
    "faturamento": faturamento,
    "metas_concluidas": metas_concluidas
}

if kpi_filial["faturamento"] >= 500000 and kpi_filial["metas_concluidas"] >= 10:
    print(f"\nDesempenho da Filial {nome_filial}: Excelente - Bônus liberado!.")
else:
    print(f"\nDesempenho da Filial {nome_filial}: Regular - Bônus não liberado.")

print(f"\n========== Lista Completa da Filial {nome_filial} ==========")
for chave, valor in kpi_filial.items():
    print(f"{chave.capitalize()}: {valor}\n")