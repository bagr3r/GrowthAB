from pathlib import Path

#gera um relatório individual em Markdown com os resultados do experimento analisado
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

        # Escreve o cabeçalho do relatório
        file.write(
            f"# Análise do Teste A/B - {test_name}\n\n"
        )

        # Descreve o objetivo da análise
        file.write(
            "## Objetivo\n\n"
        )

        file.write(
            "Avaliar qual variante de cashback "
            "apresenta o melhor desempenho financeiro "
            "e deve ser considerada para expansão.\n\n"
        )

        # Exibbe o resumo consolidado das métricas
        file.write(
            "## Resumo dos Resultados\n\n"
        )

        summary_display = summary.copy()

        # Formatação amigável
        summary_display["lucro"] = (
            summary_display["lucro"]
            .map(lambda x: f"R$ {x:,.0f}")
        )

        summary_display["roi"] = (
            summary_display["roi"]
            .map(lambda x: f"{x:.2f}")
        )

        summary_display["cashback_rate"] = (
            summary_display["cashback_rate"]
            .map(lambda x: f"{x:.2%}")
        )

        summary_display["lucro_por_comprador"] = (
            summary_display["lucro_por_comprador"]
            .map(lambda x: f"R$ {x:.2f}")
        )

        # Mantém apenas métricas mais relevantes para tomada de decisão
        summary_display = summary_display[
            [
                "compradores",
                "lucro",
                "lucro_por_comprador",
                "roi",
                "cashback_rate"
            ]
        ]

        file.write(
            summary_display.to_markdown()
        )

        file.write("\n\n")

        # Grupo vencedor
        file.write(
            "## Grupo Vencedor\n\n"
        )

        file.write(
            f"**{winner}**\n\n"
        )

        # exibe os resultados dos testes estatísticos
        if stats:

            file.write(
                "## Análise Estatística\n\n"
            )

            for group, result in stats.items():

                significance = (
                    "Significativo"
                    if result["significant"]
                    else "Não significativo"
                )

                file.write(
                    f"### {winner} vs {group}\n\n"
                )

                file.write(
                    f"- p-value: {result['p_value']:.5f}\n"
                )

                file.write(
                    f"- Resultado: {significance}\n\n"
                )

        # Registra a recomendação final do experimento
        if recommendation:

            file.write(
                "## Recomendação\n\n"
            )

            file.write(
                f"{recommendation}\n"
            )