# GrowthAB

Solução para análise automatizada de testes A/B de cashback.

O projeto processa datasets de experimentos, identifica a variante vencedora, realiza validação estatística, gera relatórios executivos e registra automaticamente os resultados em uma planilha Google Sheets.

---

## Objetivo

Responder à pergunta:

> Dado um teste A/B de cashback, qual variante deve ser escalada para 100% do tráfego?

---

## Funcionalidades

- Leitura automática de datasets CSV
- Limpeza e tratamento de dados monetários
- Cálculo de métricas de negócio
- Seleção da variante vencedora
- Teste de significância estatística (Welch's T-Test)
- Geração de relatórios individuais
- Geração de resumo executivo consolidado
- Exportação de histórico em CSV
- Registro automático dos resultados em Google Sheets

---

## Estrutura do Projeto

```text
GrowtAB/

├── analyze.py
├── requirements.txt
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

### Lucro por Comprador

```text
lucro_por_comprador = lucro / compradores
```

### ROI

```text
roi = lucro / cashback
```

### Cashback Rate

```text
cashback_rate = cashback / vendas_totais
```

---

## Análise Estatística

A solução utiliza o teste de Welch (Welch's T-Test) para comparar o grupo vencedor com as demais variantes.

Critério adotado:

```text
p-value < 0.05
```

Resultado:

- Significativo → pode escalar
- Não significativo → coletar mais dados

---

## Como Executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar todos os datasets:

```bash
python analyze.py data
```

Executar apenas um dataset:

```bash
python analyze.py data/dataset_01_parceiroA.csv
```

---

## Saídas Geradas

### Relatórios

```text
reports/
```

Relatórios individuais para cada teste.

### Resumo Executivo

```text
reports/executive_summary.md
```

Resumo consolidado dos resultados.

### Histórico

```text
output/test_history.csv
```

Histórico local de todos os testes analisados.

### Google Sheets

Os resultados também são registrados automaticamente em uma planilha Google Sheets para acompanhamento centralizado.

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- SciPy
- Google Sheets API
- GSpread