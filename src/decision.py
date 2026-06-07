# Seleciona o grupo com maior lucro agregado
def select_winner(summary):
    return summary["lucro"].idxmax()