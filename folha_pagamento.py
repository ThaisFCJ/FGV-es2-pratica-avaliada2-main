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

IRRF_FAIXA_1 = 2259.20
IRRF_FAIXA_2 = 2826.65
IRRF_FAIXA_3 = 3751.05
IRRF_FAIXA_4 = 4664.68

IRRF_ALIQUOTA_1 = 0.075
IRRF_ALIQUOTA_2 = 0.15
IRRF_ALIQUOTA_3 = 0.225
IRRF_ALIQUOTA_4 = 0.275

IRRF_DEDUCAO_1 = 169.44
IRRF_DEDUCAO_2 = 381.44
IRRF_DEDUCAO_3 = 662.77
IRRF_DEDUCAO_4 = 896.00

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

def calcular_irrf(salario_bruto, inss, dependentes):
    base_calculo = (
        salario_bruto
        - inss
        - dependentes * DEDUCAO_DEPENDENTE
    )

    if base_calculo <= IRRF_FAIXA_1:
        irrf = 0

    elif base_calculo <= IRRF_FAIXA_2:
        irrf = (
            base_calculo * IRRF_ALIQUOTA_1
            - IRRF_DEDUCAO_1
        )

    elif base_calculo <= IRRF_FAIXA_3:
        irrf = (
            base_calculo * IRRF_ALIQUOTA_2
            - IRRF_DEDUCAO_2
        )

    elif base_calculo <= IRRF_FAIXA_4:
        irrf = (
            base_calculo * IRRF_ALIQUOTA_3
            - IRRF_DEDUCAO_3
        )
    
    else:
        irrf = (
        base_calculo * IRRF_ALIQUOTA_4
        - IRRF_DEDUCAO_4
    )

    return max(irrf, 0)

def calcular_folha(funcionario):
    # f eh um dicionario com os dados do funcionario
    # campos: nome, salario_base, horas_extras, dependentes, tem_bonus, valor_bonus
    # retorna outro dicionario com salario_bruto inss irrf liquido etc

    # calcula horas extras (50% a mais)
    salario_base = funcionario["salario_base"]
    horas_extras = funcionario["horas_extras"]

    valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)

    # bonus
    if funcionario["tem_bonus"]:
        bonus = funcionario["valor_bonus"]
    else:
        bonus = 0

    # salario bruto
    salario_bruto = salario_base + valor_horas_extras + bonus

    # INSS
    inss = caclular_inss(salario_bruto)

    # IRRF - usa base de calculo (salario bruto - INSS - deducao por dependentes)
    dependentes = funcionario["dependentes"]
    irrf = calcular_irrf(salario_bruto, inss, dependentes)

    # liquido
    salario_liquido = salario_bruto - inss - irrf

    return {
        "nome": funcionario["nome"],
        "salario_bruto": round(salario_bruto, 2),
        "valor_horas_extras": round(valor_horas_extras, 2),
        "bonus": round(bonus, 2),
        "inss": round(inss, 2),
        "irrf": round(irrf, 2),
        "salario_liquido": round(salario_liquido, 2),
    }
