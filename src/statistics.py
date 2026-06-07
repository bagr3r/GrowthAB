from scipy.stats import ttest_ind

#Separa os valores da métrica escolhida por grupo 
def compare_groups(df, metric="lucro"):

    groups = {}

    for group_name in df["Grupos de usuários"].unique():

        groups[group_name] = (
            df[
                df["Grupos de usuários"] == group_name
            ][metric]
        )

    return groups


#compara o grupo vencedor com as demais variantes utilizando o teste t de welch
def significance_test(df, winner):

    winner_data = df[
        df["Grupos de usuários"] == winner
    ]["lucro"]

    results = {}

    for group in df["Grupos de usuários"].unique():

        if group == winner:
            continue

        challenger = df[
            df["Grupos de usuários"] == group
        ]["lucro"]

        #avalia se a diferença observada entre os grupos é estatisticamente significativa
        statistic, p_value = ttest_ind(
            winner_data,
            challenger,
            equal_var=False
        )

        results[group] = {
            "p_value": p_value,
            "significant": p_value < 0.05
        }

    return results