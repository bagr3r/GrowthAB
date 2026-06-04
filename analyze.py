from pathlib import Path
import pandas as pd

from src.loader import load_dataset
from src.cleaner import clean_dataset
from src.metrics import create_metrics, build_summary
from src.decision import select_winner
from src.reporter import save_report
from src.statistics import significance_test
from src.summary_generator import generate_executive_summary

Path("reports").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)

DATA_DIR = Path("data")

results = []

for csv_file in DATA_DIR.glob("*.csv"):

    print(f"\n{'=' * 60}")
    print(f"Analyzing {csv_file.name}")
    print(f"{'=' * 60}")

    # 1. Load
    df = load_dataset(csv_file)

    print("\nColumns:")
    print(df.columns.tolist())

    # 2. Clean
    df = clean_dataset(df)

    # 3. Metrics
    df = create_metrics(df)

    # 4. Summary
    summary = build_summary(df)

    print("\nSummary:")
    print(summary)

    # 5. Winner
    winner = select_winner(summary)

    print(f"\nWinner: {winner}")

    # 6. Statistical analysis
    stats = significance_test(df, winner)

    print("\nStatistical Analysis:")

    all_significant = True

    for group, result in stats.items():

        print(f"\n{winner} vs {group}")
        print(f"p-value: {result['p_value']:.5f}")
        print(f"significant: {result['significant']}")

        if not result["significant"]:
            all_significant = False

    # Business recommendation
    if all_significant:
        decision = f"Scale {winner}"
    else:
        decision = f"Collect more data before scaling {winner}"

    print(f"\nRecommendation: {decision}")

    # 7. Report
    save_report(
        test_name=csv_file.stem,
        summary=summary,
        winner=winner,
        stats=stats,
        recommendation=decision
    )

    # 8. History
    results.append({
        "test_name": csv_file.stem,
        "winner": winner,
        "decision": decision
    })

# Save consolidated history
pd.DataFrame(results).to_csv(
    "output/test_history.csv",
    index=False
)

generate_executive_summary(
    results
)

print("\nFeito!")