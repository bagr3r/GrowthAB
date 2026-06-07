from pathlib import Path
import pandas as pd
import sys

from src.loader import load_dataset
from src.cleaner import clean_dataset
from src.metrics import create_metrics, build_summary
from src.decision import select_winner
from src.reporter import save_report
from src.statistics import significance_test
from src.summary_generator import generate_executive_summary
from src.google_sheets import update_google_sheet

# Cria diretórios de saída caso ainda não existam
Path("reports").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)


#permite selecionar a execução:
#python analyze.py (executa a pasta data completa)
#python analyze.py data/arquivo.csv(executa somente o arquivo mencionado)
def get_csv_files():

    if len(sys.argv) > 1:

        target = Path(sys.argv[1])

        if target.is_file():
            return [target]

        if target.is_dir():
            return list(
                target.glob("*.csv")
            )

    return list(
        Path("data").glob("*.csv")
    )

#Estrutura para consolidar os resultados de todos os experimentos
results = []

#processa cada teste A/B
csv_files = get_csv_files()

for csv_file in csv_files:

    print(f"\n{'=' * 60}")
    print(f"Analisando{csv_file.name}")
    print(f"{'=' * 60}")

    # carrega o dataset
    df = load_dataset(csv_file)

    print("\nColunas:")
    print(df.columns.tolist())

    # limpa e padroniza os dados recebidos
    df = clean_dataset(df)

    # Período do experimento
    start_date = df["Data"].min()
    end_date = df["Data"].max()

    # Calcula as métricas utilizadas na tomada de decisão
    df = create_metrics(df)

    # Consolida os resultados por grupo
    summary = build_summary(df)

    print("\nResumos:")
    print(summary)

    # Seleciona a variante com melhor desempenho financeiro
    winner = select_winner(summary)

    print(f"\nGrupo vencedor: {winner}")

    # Valida se a superioridade do vencedor é significativa 
    stats = significance_test(df, winner)

    print("\nAnálise Estatística:")

    all_significant = True

    for group, result in stats.items():

        print(f"\n{winner} vs {group}")
        print(f"p-value: {result['p_value']:.5f}")
        print(f"significant: {result['significant']}")

        if not result["significant"]:
            all_significant = False

    # Gera e Define a recomendação final
    if all_significant:
        decision = (
        f"Escalar {winner} para 100% do tráfego"
    )
    else:
        decision = (
        f"Coletar mais dados antes de escalar {winner}"
    )

    print(f"\nRecomendação: {decision}")

    # Gera relatório executivo individual por experimento analisado 
    save_report(
        test_name=csv_file.stem,
        summary=summary,
        winner=winner,
        stats=stats,
        recommendation=decision
    )

    # Extrai as métricsa finais do grupo vencedor
    winner_profit = summary.loc[
    winner,
    "lucro"
    ]

    winner_roi = summary.loc[
        winner,
        "roi"
    ]

    #Registra os resultados para geração do histórico consolidado, resumo executivo e atualização da planilha
    results.append({
        "test_name": f"Teste Cashback {df['Parceiro'].iloc[0]}",

        "period": (
            f"{start_date} até {end_date}"
        ),

        "description": (
            f"Comparação entre "
            f"{df['Grupos de usuários'].nunique()} "
            f"variantes de cashback"
        ),

    "result": (
        f"{winner} apresentou "
        f"o maior lucro e ROI do teste"
    ),

    "decision": decision,

    "partner": df["Parceiro"].iloc[0],

    "winner": winner,

    "profit": winner_profit,

    "roi": winner_roi,

    "stats": stats
})



print("\nRESULTADOS CONSOLIDADOS:")
print(results)

# Exporta histórico consolidado em CSV
pd.DataFrame(results).to_csv(
    "output/test_history.csv",
    index=False
)

# Gera visão executiva consolidada de todos os experimentos
generate_executive_summary(
    results
)

#Atualiza automaticamnete a planilha
update_google_sheet(results)

print("\nAnálise concluída!")