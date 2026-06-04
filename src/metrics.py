def create_metrics(df):
    df["lucro"] = (
        df["comissão"]
        - df["cashback"]
    )
    return df

def build_summary(df):


    summary = (
        df.groupby("Grupos de usuários")
        .agg({
            "compradores": "sum",
            "comissão": "sum",
            "cashback": "sum",
            "vendas totais": "sum",
            "lucro": "sum"
        })
    )

    summary["lucro_por_comprador"] = (
        summary["lucro"] /
        summary["compradores"]
    )

    summary["roi"] = (
        summary["lucro"] /
        summary["cashback"]
    )

    summary["cashback_rate"] = (
        summary["cashback"] /
        summary["vendas totais"]
    )

    return summary