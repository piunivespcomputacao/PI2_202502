# src/data_loader.py
import pandas as pd

class DataLoader:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load(self):
        # keep_default_na=False evita transformar strings vazias em NaN
        self.df = pd.read_csv(self.csv_path, dtype=str, keep_default_na=False)
        # converter colunas numéricas
        if 'pressao' in self.df.columns:
            self.df['pressao'] = pd.to_numeric(self.df['pressao'], errors='coerce').fillna(0)
        if 'temperatura' in self.df.columns:
            self.df['temperatura'] = pd.to_numeric(self.df['temperatura'], errors='coerce').fillna(0)
        return self.df

    def find_by_id(self, id_peca):
        if self.df is None:
            self.load()
        rows = self.df[self.df['id_peca'].astype(str) == str(id_peca)]
        if rows.empty:
            return None
        return rows.iloc[0]
