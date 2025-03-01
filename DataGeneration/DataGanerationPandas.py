import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Proline': np.random.rand(100),
    'Alcohol': np.random.randint(0, 100, 100),
    'label': np.random.choice(['A', 'B'], 100)
})

df.to_csv('wine', index=False)

print(df)