import pandas as pd

#Carrega o dataset CSV para análise
def load_dataset(file_path):
    return pd.read_csv(file_path)