from pathlib import Path


def save_report(
    test_name,
    summary,
    winner,
    stats=None,
    recommendation=None
):

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / f"{test_name}.md"

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(f"# {test_name}\n\n")

        file.write("## Summary\n\n")

        file.write(summary.to_string())

        file.write("\n\n")

        file.write(f"## Winner\n\n{winner}\n\n")

        if stats:

            file.write("## Statistical Analysis\n\n")

            for group, result in stats.items():

                file.write(
                    f"- {winner} vs {group}\n"
                )

                file.write(
                    f"  - p-value: {result['p_value']:.5f}\n"
                )

                file.write(
                    f"  - significant: {result['significant']}\n\n"
                )

        if recommendation:

            file.write("## Recommendation\n\n")

            file.write(
                f"{recommendation}\n"
            )