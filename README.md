# GrowthAB

Solução para análise automatizada de testes A/B de cashback.

O projeto processa datasets de experimentos, identifica a variante vencedora, realiza validação estatística, gera relatórios executivos e registra automaticamente os resultados em uma planilha Google Sheets.

---

## Planilha de Acompanhamento

Os resultados dos experimentos são registrados automaticamente em uma planilha Google Sheets.

Link público para visualização:

https://docs.google.com/spreadsheets/d/142oGyf8Gnpg7ffHNUcHhdWhUzXAXVquiQhfxNMoJ7Yw/edit?usp=sharing

A planilha contém:

* Nome do teste
* Período analisado
* Descrição do experimento
* Resultado obtido
* Decisão recomendada
* Parceiro
* Grupo vencedor
* Lucro
* ROI

Ela funciona como histórico consolidado dos experimentos analisados pela solução.

---

## Objetivo

Responder à pergunta de negócio:

> Dado um teste A/B de cashback, qual variante deve ser escalada para 100% do tráfego?

A solução foi desenvolvida para ser reutilizável e processar novos experimentos sem necessidade de alteração de código.

---

## Funcionalidades

* Leitura automática de datasets CSV
* Limpeza e tratamento de dados monetários
* Cálculo de métricas de negócio
* Seleção automática da variante vencedora
* Teste de significância estatística (Welch's T-Test)
* Geração de relatórios individuais em Markdown
* Geração de resumo executivo consolidado
* Exportação de histórico em CSV
* Registro automático dos resultados em Google Sheets

---

## Arquitetura da Solução

A solução foi construída de forma modular para facilitar manutenção, reutilização e integração com ferramentas de IA.

Fluxo de processamento:

```text
CSV → Carregamento → Limpeza → Cálculo de Métricas → Seleção do Vencedor → Teste Estatístico → Recomendação → Relatórios → Google Sheets
```

Responsabilidades dos módulos:

* loader.py: leitura dos datasets
* cleaner.py: tratamento e padronização dos dados
* metrics.py: cálculo das métricas de negócio
* statistics.py: testes estatísticos
* decision.py: definição da variante vencedora
* reporter.py: geração dos relatórios individuais
* summary_generator.py: geração do resumo executivo consolidado
* google_sheets.py: integração com Google Sheets

---

## Estrutura do Projeto

```text
GrowthAB/

├── analyze.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── dataset_01_parceiroA.csv
│   ├── dataset_02_parceiroB.csv
│   └── dataset_03_parceiroC.csv
│
├── reports/
│   ├── dataset_01_parceiroA.md
│   ├── dataset_02_parceiroB.md
│   ├── dataset_03_parceiroC.md
│   └── executive_summary.md
│
├── output/
│   └── test_history.csv
│
└── src/
    ├── loader.py
    ├── cleaner.py
    ├── metrics.py
    ├── statistics.py
    ├── decision.py
    ├── reporter.py
    ├── summary_generator.py
    └── google_sheets.py
```

---

## Métricas Calculadas

### Lucro

```text
lucro = comissão - cashback
```

Representa o retorno financeiro líquido da operação.

### Lucro por Comprador

```text
lucro_por_comprador = lucro / compradores
```

Mede a eficiência econômica por usuário convertido.

### ROI

```text
roi = lucro / cashback
```

Avalia o retorno obtido para cada real investido em cashback.

### Cashback Rate

```text
cashback_rate = cashback / vendas_totais
```

Indica a proporção do volume de vendas distribuída em cashback.

---

## Análise Estatística

A solução utiliza o teste de Welch (Welch's T-Test) para comparar o grupo vencedor com as demais variantes.

Critério adotado:

```text
p-value < 0.05
```

Interpretação:

* Significativo → diferença estatisticamente válida
* Não significativo → necessidade de coletar mais dados

A recomendação final considera tanto o desempenho financeiro quanto a significância estatística.

---

## Uso com Ferramentas de IA

A solução foi estruturada para ser facilmente acionada por ferramentas de IA como:

* ChatGPT
* Claude
* Cursor
* Gemini

Exemplos de uso:

```text
Analise o arquivo data/dataset_01_parceiroA.csv
```

```text
Execute a análise do novo teste A/B e gere os relatórios
```

```text
Atualize a planilha de acompanhamento com os resultados do experimento
```

Como a lógica está centralizada em módulos independentes e o ponto de entrada é o script analyze.py, a solução pode ser integrada facilmente em fluxos orientados por linguagem natural.

---

## Exemplo de Resultado

```text
Teste Cashback Parceiro A

Período:
01/01/2024 até 31/01/2024

Grupo vencedor:
Grupo 1

Lucro:
R$ 404.711,00

ROI:
1,73

Recomendação:
Coletar mais dados antes de escalar Grupo 1
```

---

## Como Executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar todos os datasets

```bash
python analyze.py data
```

### Executar apenas um dataset

```bash
python analyze.py data/dataset_01_parceiroA.csv
```

---

## Saídas Geradas

### Relatórios Individuais

```text
reports/
```

Um relatório detalhado é gerado para cada experimento analisado.

### Resumo Executivo

```text
reports/executive_summary.md
```

Contém uma visão consolidada dos experimentos analisados, incluindo:

* Período do teste
* Grupo vencedor
* Lucro obtido
* ROI
* Resultado das análises estatísticas
* Recomendação final

### Histórico Local

```text
output/test_history.csv
```

Registro consolidado dos experimentos analisados.

### Google Sheets

Além dos arquivos locais, os resultados também são registrados automaticamente em uma planilha Google Sheets.

Campos registrados:

* Nome do teste
* Período analisado
* Descrição do experimento
* Resultado obtido
* Decisão recomendada
* Parceiro
* Grupo vencedor
* Lucro
* ROI

A planilha funciona como histórico centralizado para acompanhamento dos experimentos realizados.

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* SciPy
* Google Sheets API
* GSpread

---

