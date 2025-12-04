import numpy as np
import pandas as pd

def risk_of_identification(df):
    qis = ['idade', 'genero']
    combos = df[qis].astype(str).agg('-'.join, axis=1)
    unicidade = (combos.map(combos.value_counts()) == 1).mean()
    return unicidade


def apply_k_anonymity(df):
    df['faixa_idade'] = pd.cut(
        df['idade'],
        bins=[0, 25, 35, 45, 55, 70],
        labels=['18-25', '26-35', '36-45', '46-55', '56-70']
    )

    combos = df[['faixa_idade', 'genero']].astype(str).agg('-'.join, axis=1)
    kmin = combos.value_counts().min()

    return df, kmin


def laplace_mechanism(values, sensitivity=1.0, epsilon=1.0):
    noise = np.random.laplace(0, sensitivity / epsilon, len(values))
    return np.clip(values + noise, 0, 1)
