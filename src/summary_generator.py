from pathlib import Path


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
            "# Executive Summary\n\n"
        )

        for result in results:

            file.write(
                f"## {result['test_name']}\n\n"
            )

            file.write(
                f"Winner: {result['winner']}\n\n"
            )

            file.write(
                f"Decision: {result['decision']}\n\n"
            )

            file.write(
                "---\n\n"
            )