#Calcula o lucro diário de cada observação
def create_metrics(df):
    df["lucro"] = (
        df["comissão"]
        - df["cashback"]
    )
    return df

#Consolida os resultados por grupo e calcula as métricas utilizadas na análise do experimento
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

    #mede o lucro médio gerado por comprador
    summary["lucro_por_comprador"] = (
        summary["lucro"] /
        summary["compradores"]
    )

    #mede o retorno obtido para cada real distribuído em cashback
    summary["roi"] = (
        summary["lucro"] /
        summary["cashback"]
    )

    #mede o percentual do GMV desenvolvido aos usuários em forma de cashback
    summary["cashback_rate"] = (
        summary["cashback"] /
        summary["vendas totais"]
    )

    return summary