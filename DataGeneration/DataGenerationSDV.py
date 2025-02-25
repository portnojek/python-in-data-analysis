from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import Metadata
import pandas as pd
import numpy as np

# Tworzenie przykładowych danych
your_real_data = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.randint(0, 100, 100),
    'label': np.random.choice(['A', 'B'], 100)
})

# Tworzenie i konfiguracja metadanych
metadata = Metadata.detect_from_dataframe(data=your_real_data, table_name='example_table')

# Zapisywanie metadanych do pliku JSON (opcjonalne, ale zalecane)
metadata.save_to_json('your_metadata.json')

# Tworzenie i trenowanie modelu
synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(your_real_data)

# Generowanie syntetycznych danych
synthetic_data = synthesizer.sample(num_rows=100)

print(synthetic_data)
