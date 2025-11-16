# src/quality.py
import pandas as pd

class QualityReport:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy() if df is not None else pd.DataFrame()

    def summary(self):
        total = len(self.df)
        defects = self.df[self.df['status'].str.lower() == 'defeituoso'] if 'status' in self.df.columns else self.df
        count_defects = len(defects)
        per_lote = {}
        if 'lote_producao' in self.df.columns:
            per_lote = self.df['lote_producao'].value_counts().to_dict()
        return {
            'total': total,
            'defeituosas': count_defects,
            'per_lote': per_lote,
            'ok': total - count_defects
        }
