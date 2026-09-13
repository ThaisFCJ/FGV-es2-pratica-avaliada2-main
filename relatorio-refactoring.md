# Relatório de Refactoring — Prática Avaliativa 2

## 1. Problemas encontrados

A função `calcular_folha()` concentrava a maioria dos cálculos da folha de pagamento. 
Havia muitos números diretamente nos cálculos e algumas variáveis com nomes abreviados, o que dificultava a leitura.
Os cálculos de INSS e IRRF possuíam vários `if` aninhados.

## 2. Refatorações realizadas

Mudanças:

* **Extract Method:** os cálculos de horas extras, INSS e IRRF foram separados em funções próprias.
* **Magic Numbers:** valores como `220`, `1.5` e as faixas de INSS e IRRF foram transformados em constantes com nomes explicativos.
* **Rename Variable:** nomes como `f`, `sb`, `sbr` e `ins` foram substituídos para ter clareza: `funcionario`, `salario_base`, `salario_bruto` e `inss`.
* **Melhoria dos condicionais:** os `if` aninhados foram reorganizados para entendimento.

