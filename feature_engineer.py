import pandas as pd
ALPHA_BETA_TUMOR = 10.0

def add_bed_and_eqd2(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    n_fractions = df["radiotherapy_number_fractions_highriskgtv"]
    dose_per_fraction = df["radiotherapy_refgydose_perfraction_highriskgtv"]
    df["bed_gy"] = n_fractions * dose_per_fraction * (1 + dose_per_fraction/ALPHA_BETA_TUMOR)
    df["eqd2_gy"] = df["bed_gy"] / (1 + 2/ ALPHA_BETA_TUMOR)
    return df