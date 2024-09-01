# questão 4 faturamento distribuidora

# estados e valor do faturamento

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

total_faturamento = sum(faturamento.values())
print("Percentual de representação do faturamento mensal por estado:")
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")

