auditor = input("Nome do Auditor: ")
total_tabletes = int(input("Digite o total de tabletes vendidos: "))

caixas_cheias = total_tabletes // 6
tabletes_sobrando = total_tabletes % 6

if total_tabletes >= 100:
    status = "Lote crítico - Prioridade máxima no recolhimento"
elif total_tabletes >= 30:
    status = "Lote padrão - Fluxo Normal"
else:
    status = "Lote Reduzido - Reagrupar carga"

print("\n==============================================")
print("        RELATÓRIO DE AUDITORIA DE CARGA       ")
print("==============================================")
print(f"Auditor Responsável: {auditor.strip().title()}")
print(f"Total de Unidades: {total_tabletes} tablets")
print(f"Distribuição: {caixas_cheias} caixas cheias")
print(f"Sobras de Logística: {tabletes_sobrando} unidades fora da caixa")
print(f"Status para o Banco de Dados: {status}")
print("==============================================")