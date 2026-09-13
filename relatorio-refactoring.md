# Relatório de Refactoring — Prática Avaliativa 2

O objetivo foi melhorar a organização e a legibilidade do arquivo `folha_pagamento.py`, mantendo os mesmos resultados do programa.

## 1. Problemas encontrados

No código original, a função `calcular_folha()` concentrava praticamente todos os cálculos da folha de pagamento. Também havia muitos números diretamente nos cálculos e algumas variáveis com nomes abreviados, o que dificultava a leitura.

Além disso, os cálculos de INSS e IRRF possuíam vários `if` aninhados.

## 2. Refatorações realizadas

Foram feitas as seguintes melhorias:

* **Extract Method:** os cálculos de horas extras, INSS e IRRF foram separados em funções próprias.
* **Magic Numbers:** valores como `220`, `1.5` e as faixas de INSS e IRRF foram transformados em constantes com nomes explicativos.
* **Rename Variable:** nomes como `f`, `sb`, `sbr` e `ins` foram substituídos por nomes mais claros, como `funcionario`, `salario_base`, `salario_bruto` e `inss`.
* **Melhoria dos condicionais:** os `if` aninhados foram reorganizados para deixar os cálculos mais fáceis de entender.

## 3. Testes

Depois das alterações, os testes fornecidos pelo professor foram executados com:

```bash
python -m pytest tests_professor_pratica2.py
```

O resultado foi:

```text
16 passed
```

Isso confirma que as alterações não modificaram o comportamento esperado do programa.
