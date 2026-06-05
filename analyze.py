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


Path("reports").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)


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


results = []

csv_files = get_csv_files()

for csv_file in csv_files:

    print(f"\n{'=' * 60}")
    print(f"Analisando{csv_file.name}")
    print(f"{'=' * 60}")

    # 1. Load
    df = load_dataset(csv_file)

    print("\nColunas:")
    print(df.columns.tolist())

    # 2. Clean
    df = clean_dataset(df)

    # 3. Metrics
    df = create_metrics(df)

    # 4. Summary
    summary = build_summary(df)

    print("\nResumos:")
    print(summary)

    # 5. Winner
    winner = select_winner(summary)

    print(f"\nGrupo vencedor: {winner}")

    # 6. Statistical Analysis
    stats = significance_test(df, winner)

    print("\nAnálise Estatística:")

    all_significant = True

    for group, result in stats.items():

        print(f"\n{winner} vs {group}")
        print(f"p-value: {result['p_value']:.5f}")
        print(f"significant: {result['significant']}")

        if not result["significant"]:
            all_significant = False

    # 7. Business Recommendation
    if all_significant:
        decision = (
        f"Escalar {winner} para 100% do tráfego"
    )
    else:
        decision = (
        f"Coletar mais dados antes de escalar {winner}"
    )

    print(f"\nRecomendação: {decision}")

    # 8. Report
    save_report(
        test_name=csv_file.stem,
        summary=summary,
        winner=winner,
        stats=stats,
        recommendation=decision
    )

    # 9. History
    winner_profit = summary.loc[
    winner,
    "lucro"
    ]

    winner_roi = summary.loc[
        winner,
        "roi"
    ]

    results.append({
        "test_name": csv_file.stem,
        "partner": df["Parceiro"].iloc[0],
        "winner": winner,
        "profit": winner_profit,
        "roi": winner_roi,
        "decision": decision,
        "stats": stats
    })

print("\nRESULTADOS CONSOLIDADOS:")
print(results)

# Consolidated History
pd.DataFrame(results).to_csv(
    "output/test_history.csv",
    index=False
)

# Executive Summary
generate_executive_summary(
    results
)

update_google_sheet(results)

print("\nAnálise concluída!")