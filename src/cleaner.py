#Converte valores monetários para float
def parse_currency(value):

    value = str(value)

    value = value.replace("R$", "")
    value = value.replace(".", "")
    value = value.replace(",", ".")

    return float(value.strip())

#Padroniza as colunas monetárias do dataset antes do cálculo das métricas de negócio
def clean_dataset(df):

    currency_columns = [
        "comissão",
        "cashback",
        "vendas totais"
    ]

    for column in currency_columns:
        df[column] = df[column].apply(parse_currency)

    return df