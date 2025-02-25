import pandas as pd
import numpy as np

df = pd.DataFrame({
    'feature_1': np.random.rand(100),
    'feature_2': np.random.randint(0, 100, 100),
    'label': np.random.choice(['A', 'B'], 100)
})

print(df)