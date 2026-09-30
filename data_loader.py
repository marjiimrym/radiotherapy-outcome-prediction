import pandas as pd

REQUIRED_COLUMNS = [
    "age_at_diagnosis",
    "biological_sex",
    "clin_t",
    "clin_n"
    "ajcc_stage",
    "overral_hpv_p16_status",
    "radiotherapy_refgydose_total_highriskgtv",
    "radiotherapy_refgysoe_prefraction_highriskgtv",
    "radiotherapy_number_fractions_highriskgtv",
    "overall_surivival_in_days",
    "event_overall_survival",
]

class DataLoader:
    def __init__(self, csv_path: str):
        self.csvpath = csv_path

    def load(self) -> pd.DataFrame: 
        df = pd.read_csv(self.csv_path)
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing: 
            raise ValueError(f"CSV is missing required column(s): {missing}")
        print(f"Loaded {len(df)} patients, {len(df.columns)} columns.")
        return df[REQUIRED_COLUMNS].copy()