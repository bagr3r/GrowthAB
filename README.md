# GrowtAB

Motor de análise de testes A/B para campanhas de cashback.

## Objetivo

Analisar automaticamente experimentos de cashback e recomendar qual variante deve ser escalada para 100% do tráfego com base em métricas de negócio e significância estatística.

---

## Funcionalidades

- Leitura automática de múltiplos datasets CSV
- Limpeza e tratamento dos dados
- Cálculo de métricas de negócio
- Cálculo de lucro por grupo
- Cálculo de ROI
- Cálculo da taxa de cashback
- Escolha automática da variante vencedora
- Teste de significância estatística (Welch T-Test)
- Geração de relatórios em Markdown
- Geração de resumo executivo
- Histórico consolidado dos testes

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

├── src/
│   ├── cleaner.py
│   ├── decision.py
│   ├── loader.py
│   ├── metrics.py
│   ├── reporter.py
│   ├── statistics.py
│   └── summary_generator.py

├── reports/
│   ├── dataset_01_parceiroA.md
│   ├── dataset_02_parceiroB.md
│   ├── dataset_03_parceiroC.md
│   └── executive_summary.md

└── output/
    └── test_history.csv
```

---

## Instalação

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Como executar

Para analisar todos os datasets da pasta `data`:

```bash
python analyze.py
```

---

## Métricas Utilizadas

A solução avalia cada grupo utilizando:

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

## Significância Estatística

A comparação entre os grupos é realizada utilizando o teste:

- Welch's T-Test

Critério:

```text
p-value < 0.05
```

Quando a diferença não é estatisticamente significativa, a recomendação é coletar mais dados antes de escalar uma variante.

---

## Saídas Geradas

### Relatórios

Gerados automaticamente em:

```text
reports/
```

### Resumo Executivo

Gerado automaticamente em:

```text
reports/executive_summary.md
```

### Histórico Consolidado

Gerado automaticamente em:

```text
output/test_history.csv
```

---

## Exemplo de Decisão

A solução responde à seguinte pergunta:

> "Dado esse teste A/B, qual variante de cashback devemos escalar para 100% do tráfego?"

A recomendação é baseada em:

- Rentabilidade
- ROI
- Eficiência do cashback
- Significância estatística

