from pathlib import Path


# Formata valores monetários para o padrão brasileiro
def format_brl(value):

    return (
        f"R$ {value:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


# Gera um resumo executivo consolidado com os principais resultados dos experimentos
def generate_executive_summary(results):

    # Calcula estatísticas gerais dos experimentos
    total_tests = len(results)

    scaled_tests = sum(
        1
        for result in results
        if "100%" in result["decision"]
    )

    collect_tests = (
        total_tests - scaled_tests
    )

    report_path = (
        Path("reports")
        / "executive_summary.md"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        # Cabeçalho do documento
        file.write(
            "# Resumo Executivo\n\n"
        )

        file.write(
            "Análise consolidada dos testes A/B de cashback.\n\n"
        )

        # Apresenta uma visão geral dos experimentos
        file.write(
            "## Visão Geral\n\n"
        )

        file.write(
            f"Foram analisados "
            f"{total_tests} experimentos.\n\n"
        )

        file.write(
            f"- Testes aprovados para escala: "
            f"{scaled_tests}\n"
        )

        file.write(
            f"- Testes que requerem mais dados: "
            f"{collect_tests}\n\n"
        )

        file.write(
            "---\n\n"
        )

        # Adiciona uma seção para cada experimento
        for result in results:

            file.write(
                f"## {result['test_name']}\n\n"
            )

            file.write(
                f"**Período:** {result['period']}\n\n"
            )

            file.write(
                f"**Grupo vencedor:** "
                f"{result['winner']}\n\n"
            )

            file.write(
                f"**Lucro:** "
                f"{format_brl(result['profit'])}\n\n"
            )

            file.write(
                f"**ROI:** "
                f"{result['roi']:.2f}\n\n"
            )

            # Resume os resultados estatísticos
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

            # Registra a recomendação final
            file.write(
                f"**Recomendação:** "
                f"{result['decision']}\n\n"
            )

            file.write(
                "---\n\n"
            )