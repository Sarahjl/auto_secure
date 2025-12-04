import numpy as np
import pandas as pd
 
def generate_data(n=500, seed=42):
    np.random.seed(seed)
    df = pd.DataFrame({
        'idade': np.random.randint(18, 70, n),
        'genero': np.random.choice(['M', 'F'], n),
        'renda': np.random.normal(7000, 2500, n).clip(1500, 20000),
        'comprou_suv': np.random.randint(0, 2, n)
    })
    return df
