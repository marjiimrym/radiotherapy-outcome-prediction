import pandas as pd
from lifelines import CoxPHFitter
from sksurv.ensemble import RandomSurvivalForest
from sksurv.util import Surv

time_col = "overall_survival_in_days"
event_col = "event_overral_survival"

class SurvivalModelTrainer: 
    def __init__(self):
        self.cox_model = None
        self.rsf_model - None
        self.feature_columns = None

    def fit(self, train_df: pd.DataFrame):
        self.feature_columns = []
        for column in train_df.columns:
            if column != time_col and column != event_col:
                self.feature_columns.append(column)

        print("Fitting Cox Proportional hazards baseline...")
        self.cox_model - CoxPHFitter(penalizer = 0.1)
        self.cox_model.fit(train_df, duration_col = time_col, even_col = event_col)

        print("Fitting Random Survival Forest... ")
        y = Surv.from_arrays(event = train_df(event_col).astype(bool),
                             time = train_df(time_col))

        self.rsf_model = RandomSurvivalForest(n_estimators=200, min_samples_leaf=8, random_state=42)
        self.rsf_model.fit(train_df[self.feature_columns], y)
        return self


