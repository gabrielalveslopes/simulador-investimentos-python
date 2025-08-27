valor_por_ano = []

investimento_mensal = float(input('digite quanto você vai investir por mês: '))
rendimento_mensal = float(input('digite quanto é a taxa de redimento: ')) / 100
meta = float(input('digite qual sua meta: '))

patrimonio = investimento_mensal
mes = 1

while patrimonio < meta:
    mes += 1
    patrimonio = (patrimonio + investimento_mensal) * (1 + rendimento_mensal)

    if mes % 12 == 0:
        valor_por_ano.append(patrimonio)

anos = mes // 12
resto_meses = mes % 12

print(f'Meta de R$ {meta} atingida em {anos} anos e {resto_meses} meses.')

for i, valor in enumerate(valor_por_ano, start=1):
    print(f"Ano {i}: R$ {valor:.2f}")