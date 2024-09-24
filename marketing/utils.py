# utils.py

import os

def ensure_data_directory():
    if not os.path.exists('data'):
        os.makedirs('data')

def save_to_csv(data, filename='data/content_ideen.csv'):
    import pandas as pd
    df = pd.DataFrame(data, columns=['Content-Ideen'])
    df.to_csv(filename, index=False)