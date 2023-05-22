def main():
    valor_anterior = int(input())
    valor_atual = int(input())
    consumo = valor_atual - valor_anterior
    valor_faturado = 0
    talao_de_energia = calcular_talao(consumo, valor_faturado)
    bandeira = (consumo // 100) * 8
    valor_faturado = 0
    icms = valor_faturado * 0.25
    taxa_iluminacao = taxa(consumo, valor_faturado)
def calcular_talao(consumo, valor_faturado):
    if consumo > 0:
        if consumo < 31:
            valor_faturado = 0
        elif consumo < 101:
            valor_faturado = consumo * 0.59
        else:
            valor_faturado = consumo * 0.75
    
    return valor_faturado
    
def taxa(consumo, valor):
    if consumo > 80:
        return valor * 0.06
    else:
        return 'você não teve um consumo maior que 80 kwh'
main()