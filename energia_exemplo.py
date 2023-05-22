def calcular_talao_energia(leitura_atual, leitura_anterior):
    consumo = leitura_atual - leitura_anterior
    valor_faturado = 0
    bandeiras = 0
    icms = 0
    pis_cofins = 0
    taxa_iluminacao = 0

    if consumo > 0:
        if consumo <= 30:
            valor_faturado = 0
        elif consumo <= 100:
            valor_faturado = consumo * 0.59
        else:
            valor_faturado = consumo * 0.75

        if consumo > 80:
            taxa_iluminacao = valor_faturado * 0.06

        bandeiras = (consumo // 100) * 8
        icms = valor_faturado * 0.25
        pis_cofins = valor_faturado * 0.15

    valor_total = valor_faturado + bandeiras + icms + pis_cofins + taxa_iluminacao

    # Exibir os resultados
    print(f"Consumo: {consumo} KWh")
    print(f"Valor Faturado: R$ {valor_faturado:.2f}")
    print(f"Bandeira: R$ {bandeiras:.2f} ({consumo // 100} bandeira(s))")
    print(f"ICMS: R$ {icms:.2f}")
    print(f"PIS/CONFIS: R$ {pis_cofins:.2f}")
    print(f"Taxa Iluminação: R$ {taxa_iluminacao:.2f}")
    print(f"Valor Total a ser pago: R$ {valor_total:.2f}")


# Exemplo de uso
calcular_talao_energia(350, 200)
