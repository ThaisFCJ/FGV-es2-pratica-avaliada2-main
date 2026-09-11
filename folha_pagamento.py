"""Calculadora de Folha de Pagamento - VERSAO INICIAL (com smells).

Este arquivo funciona corretamente, mas contém vários problemas de
qualidade que o aluno deve identificar e refatorar.
"""

# este modulo calcula o salario liquido do funcionario considerando
# horas extras descontos de INSS e IRRF e bonus de produtividade
# CUIDADO ao alterar pq muita coisa depende disso aqui

HORAS_MENSAIS = 220
ADICIONAL_HORA_EXTRA = 1.5

INSS_FAIXA_1 = 1412
INSS_FAIXA_2 = 2666.68
INSS_FAIXA_3 = 4000.03
INSS_TETO = 7786.02

INSS_ALIQUOTA_1 = 0.075
INSS_ALIQUOTA_2 = 0.09
INSS_ALIQUOTA_3 = 0.12
INSS_ALIQUOTA_4 = 0.14

DEDUCAO_DEPENDENTE = 189.59

IRPF_FAIXA_1 = 2259.20
IRPF_FAIXA_2 = 2826.65
IRPF_FAIXA_3 = 3751.05
IRPF_FAIXA_4 = 4664.68

IRPF_ALIQUOTA_1 = 0.075
IRPF_ALIQUOTA_2 = 0.15
IRPF_ALIQUOTA_3 = 0.225
IRPF_ALIQUOTA_4 = 0.275

IRPF_DEDUCAO_1 = 169.44
IRPF_DEDUCAO_2 = 381.44
IRPF_DEDUCAO_3 = 662.77
IRPF_DEDUCAO_4 = 896.00

def calcular_horas_extras(salario_base, horas_extras):
    valor_hora = salario_base / HORAS_MENSAIS
    return horas_extras * valor_hora * ADICIONAL_HORA_EXTRA

def caclular_inss(salario_bruto):
    if salario_bruto <= INSS_FAIXA_1:
        return salario_bruto * INSS_ALIQUOTA_1
        
    if salario_bruto <= INSS_FAIXA_2:
        return (
            INSS_FAIXA_1 * INSS_ALIQUOTA_1
            + (salario_bruto - INSS_FAIXA_1) * INSS_ALIQUOTA_2
        )

    if salario_bruto <= INSS_FAIXA_3:
        return (
            INSS_FAIXA_1 * INSS_ALIQUOTA_1
            + (INSS_FAIXA_2 - INSS_FAIXA_1) * INSS_ALIQUOTA_2
            + (salario_bruto - INSS_FAIXA_2) * INSS_ALIQUOTA_3
        )

    if salario_bruto <= INSS_TETO:
        return (
            INSS_FAIXA_1 * INSS_ALIQUOTA_1
            + (INSS_FAIXA_2 - INSS_FAIXA_1) * INSS_ALIQUOTA_2
            + (INSS_FAIXA_3 - INSS_FAIXA_2) * INSS_ALIQUOTA_3
            + (salario_bruto - INSS_FAIXA_3) * INSS_ALIQUOTA_4
        )

    return (
        INSS_FAIXA_1 * INSS_ALIQUOTA_1
            + (INSS_FAIXA_2 - INSS_FAIXA_1) * INSS_ALIQUOTA_2
            + (INSS_FAIXA_3 - INSS_FAIXA_2) * INSS_ALIQUOTA_3
            + (INSS_TETO - INSS_FAIXA_3) * INSS_ALIQUOTA_4
    )

def calcular_folha(f):
    # f eh um dicionario com os dados do funcionario
    # campos: nome, salario_base, horas_extras, dependentes, tem_bonus, valor_bonus
    # retorna outro dicionario com salario_bruto inss irrf liquido etc

    # calcula horas extras (50% a mais)
    sb = f["salario_base"]
    he = f["horas_extras"]

    valor_he = calcular_horas_extras(sb,he)

    # bonus
    if f["tem_bonus"] == True:
        b = f["valor_bonus"]
    else:
        b = 0

    # salario bruto
    sbr = sb + valor_he + b

    #INSS
    ins = caclular_inss(sbr)

    # IRRF - usa base de calculo (salario bruto - INSS - deducao por dependentes)
    dep = f["dependentes"]
    base = sbr - ins - dep * 189.59  # 189.59 = deducao por dependente
    if base <= 2259.20:
        irrf = 0
    else:
        if base <= 2826.65:
            irrf = base * 0.075 - 169.44
        else:
            if base <= 3751.05:
                irrf = base * 0.15 - 381.44
            else:
                if base <= 4664.68:
                    irrf = base * 0.225 - 662.77
                else:
                    irrf = base * 0.275 - 896.00
    if irrf < 0:
        irrf = 0

    # liquido
    liq = sbr - ins - irrf

    return {
        "nome": f["nome"],
        "salario_bruto": round(sbr, 2),
        "valor_horas_extras": round(valor_he, 2),
        "bonus": round(b, 2),
        "inss": round(ins, 2),
        "irrf": round(irrf, 2),
        "salario_liquido": round(liq, 2),
    }
