from pathlib import Path

def format_brl(value):

    return (
        f"R$ {value:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

def generate_executive_summary(results):

    report_path = (
        Path("reports")
        / "executive_summary.md"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "# Resumo Executivo\n\n"
        )

        file.write(
            "Análise consolidada dos testes A/B de cashback.\n\n"
        )

        for result in results:

            file.write(
                f"## {result['test_name']}\n\n"
            )

            file.write(
                f"**Grupo vencedor:** {result['winner']}\n\n"
            )

            file.write(
                f"**Lucro:** {format_brl(result['profit'])}\n\n"
            )

            file.write(
                f"**ROI:** {result['roi']:.2f}\n\n"
            )

            file.write(
                "**Análise Estatística**\n\n"
            )

            for group, stat in result["stats"].items():

                significance = (
                    "Significativo"
                    if stat["significant"]
                    else "Não significativo"
                )

                file.write(
                    f"- Comparação com {group}: "
                    f"p-value={stat['p_value']:.5f} "
                    f"({significance})\n"
                )

            file.write("\n")

            file.write(
                f"**Recomendação:** "
                f"{result['decision']}\n\n"
            )

            file.write(
                "---\n\n"
            )