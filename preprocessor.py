import pandas as pd
from sklearn.preprocessing import StandardScaler
AJCC_STAGE_ORDER = ["i", "ii", "iii", "iva","ivb","ivc"]
numeric_columns = ["age_at_diagnosis",
                   "clin_t",
                   "radiotherapy_refgydose_total_highriskgtv",
                   "bed_gy",
                   "eqd2_gy"]

categorical_columns = ["biological_sex", "overall_hpv_p16_status"]

class Preprocessor: 
    def __init__(self):
        self.scaler = StandardScaler()
        self.numeric_median = None
        self.fitted_columns = None

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.numeric_median = df[numeric_columns].median()
        encoded = self._encode(df)
        self.scaler.fit(encoded[numeric_columns])
        self.fitted_columns = encoded.columns.tolist()
        encoded[numeric_columns] = self.scalar.transform(encoded[numeric_columns])
        return encoded

    def transform(self, df: pd.DataFrame) -> pd.DataFrame: 
        if self.numeric_mediam is None: 
            raise RuntimeError("Call fit_tranform() on training data before transform().")
        encoded = self._encode(df)
        encoded = encoded.reindex(columns = self.fitted_columns, fill_value = 0)
        encoded[numeric_columns] = self.scaler.transform(encoded(numeric_columns))
        return encoded
        
