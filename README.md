# radiotherapy-outcome-prediction
Engineering an end-to-end predictive machine learning pipeline to forecast patient responses to radiation therapy, bridging the gap between raw clinical data and actionable oncology decision making, by structuring a codebase using python object-orientation programming.

# Radiotherapy Treatment Response Planning 

## 1. Summary
The goal is to build a clinical decision-support pipeline that predicts how a tumor will respond to radiotherapy– either as a binary treatment success outcome or as a survival-time estimate – using clinical, dosimetric, and (maybe) imaging-derived features. The core deliverable is proposed to be a modular, version-controlled Python codebase that ingests raw clinical data, cleans it, tests statistical relationships, trains and compares survival models, and outputs per-patient predictions with SHAP explanations. I plan to keep the duration of this project at about 12-16 weeks, as a lot of the concepts involved with oncology still need to be better understood to properly create an accurate pipeline prediction. However, should there be more input from experts or professionals then I am willing to extend the timeline and transition the software development more professionally.

## 2. Main Objectives
1. The goal isn’t to just develop a software model that can use research to reiterate the same results we would normally get if we used Google.
2. Rather my goal is more so to do with demonstrating an end-to-end, reproducible clinical ML pipeline that can use data for highly accurate predictions.
3. To produce a model that is statistically justified and not just accurate – meaning every input feature should be backed by a hypothesis test or clear clinical rationale.
4. Support both classification (what responded / what didn’t respond) and oncology outcomes research almost always needs the latter.
5. Make predictions reasonable at the individual-patient level (SHAP), since clinicians will not adopt a “black box”.
6. Package the code so it reads as production-oriented software, not a one-off script.

## 3. Data Strategy (High Priority)
My biggest concern right now is being able to access the right dataset which I will use to train my model, so I’m going to seek out the best database organizations before I even start drafting the code.

| **Source** | **Output** | **Access Friction** | **Best use in this project** |
| --- | --- | --- | --- |
|Kaggle | Pre-cleaned, CSVs, similar to being subsets of SEER | None- instant download | Fastest path for the first version of the pipeline. |
|SEER Research Data | Millions of tabular records: demographics, tumor, morphology, treatment, survival time and vital status | I would need institutional validation which would be difficult unless I actually partnered with a government funded medical organization which is obviously unlikely given the time range. | Would be the primary tabular dataset for the statistical + ML phases. |
|TCIA (The Cancer Imaging Archive) |DICOM imaging (CT/PET/MRI) , dose plans + tumor contours and survival |Mainly free for public access. | This data might by used later as a stretch goal if later we can develop some sort of radiomics features to test whether imaging improves on clinical-only predictions. |
|cBioPortal (TCGA) |Clinical and genomic data<br>Clean, downloadable text files |free | <br> |

**Targeted Approach:** I’ll start with Kaggle SEER-derived CSV as the primary dataset for at least the first week of development since it is already cleaned and won’t require extensive application. Kaggle would also let me move to Phase 1 of project development immediately. If the Kaggle version of the data is too limited, we can potentially switch over the TCIA or TCGA rather than just blocking dependency.

# Project Plan

## 4. Methodology & Timeline

### Phase 1: Secure & Clean Data (Week 1 - 2)
* Finalize data set to be used; most probably Kaggle. 
* Handle missing data deliberately and understand why such values are missing (missing-at-random vs not) before choosing imputation vs deletion, natively dropping rows in clinical data can bias toward healthier or shorter-followup patients. 
* Normalize continuous features (radiation dose, tumor volume, age).
* Encode categoricals (stage, histology, treatment modality) – maybe use ordinal encoding where true clinical order exists (e.g. stage 1-IV) rather than one to preserve ordering for tree models. 

### Phase 2: Statistical Relationship Mapping (Week 3-5)
* Plot distributions (KDE/PDFs) of key covariates split by outcome group. 
* Run hypothesis tests (t-test/ Mann-Whitney for continuous, chi square for categorical) to confirm which variables actually separate responders from non-responders. 
* Check for multicollinearity (eg, dose and fractionation are usually correlated) before feeding everything into a model. 
* This phase's output should be a short “feature justification” table – a reviewer-facing artifact showing why each surviving feature was kept. 

### Phase 3: Model Training (Week 6-9)
* Strict train/test split (and a validation fold or cross-validation) split before any preprocessing that touches the whole dataset, to avoid leakage. 
* Baseline: Logistic Regression (for classification) or Kaplan-Meier and log-rank test (for survival); always benchmark against the simplest reasonable model.
* Escalate to Random Forest / Gradient Boosting (XGBoost or LightGBM) for classification. 
* For time-to-event outcomes, implement Cox Proportional Hazards as the classical baseline, then a survival-adapted ensemble (Random Survival Forest or Gradient Boosted via scikit-survival), evaluated with the concordance index (C-index) rather than plain accuracy. 
* Address class imbalance if “poor responders” or “deaths” are a minority class (SMOTE, class weighting, or threshold tuning).

### Phase 4: Explainability (Week 10-11)
* Apply SHAP (TreeExplainer for tree models) to produce:
    * Global feature importance (ie which variables matter most across the cohort). 
    * Local, per-patient explanations (why this patient’s prediction came out this way). 
* Package the output as: predicted survival probability/outcome + top 3 contributing factors + direction of effect, in a format an oncologist or clinician could actually read and comprehend. 

### Phase 5: Codebase Packaging (Week 11-12)
* Refactor into classes: TBD
* Configuration-driven (JSON) rather than hardcoded paths and hyperparameters. 
* Unit tests for the data-clearing functions especially (silent bugs).
* Git repo with incremental, straight-to-the point commits. 
* A README and md file(s) that documents the data source, access requirements, and how to reproduce results, and also how the software can be used by clinicians and oncologists. 

## 5. Predicted and Probable Tech Stack Plan
* **Data/EDA:** pandas, numpy, matplotlib/seaborn
* **Stats:** scipy.stats, statsmodels
* **ML:** scikit-learn, XGBoost
* **Survival analysis:** 
    * **Scikit-survival:** Random Forest, C-indexing scoring
    * **lifelines:** easy to learn and already have solid understanding, Kaplan-Meier, Cox PH
* **Explainability:** SHAP
* **Packaging/testing:** pytest, git

## 6. Foreseen Challenges
* **Missing/censored data handling** – real clinical follow-up data is incomplete by nature; treating censored patients (i.e. still alive, or lost follow-up) as “did not respond” will bias the model, but this is a common mishap that will be accounted for since this is a self-funded survival analysis project. 
* **Class imbalance** – poor-outcome or death events are usually the minority class; plain accuracy will look artificially high while the model will ignore the cases that matter clinically. 
* **Data leakage** – variables like “total dose received” can implicitly encode outcome (for example for patients who died early may have received a less cumulative dose). Could possibly audit features for this before training. 
* **Small sample sizes** if narrowing by cancer subtype, which can make complex models (Random Forest and gradient boosting) overfit; a simple well-validated Cox model may outperform them and I guess that’s a valid defensible finding to report. 
* **Explainability vs accuracy trade-off.** More complex models often need more engineering effort in SHAP to produce clinically legible explanations so for Phase 4 in particular I may have to go overtime. 
* **Reproducibility across data pulls.** Obviously because the dataset being used will be stationary and not ever so changing there would need to be manual updates if Kaggle decides to add more data, meaning results would shift. I will probably just use the dataset version and data in the README. 

## Steps documentation 

**September 6-8:** 
* Download Kaggle SEER-derived CSV to begin Phase 1
* Confirm it contains the required survival analysis fields before committing to it. 
    * Time-to-event 
    * Censoring status
* Initialize git repo and src project skeleton
* Draft the feature list using (dose, stage, histology, age, treatment type and tumor volume); phase 1 cleaning has a clear target schema. 
* Regardless I will still submit a SEER Research Data application in parallel just so there’s a change of getting a clearer dataset if Kaggle is proven too limited later.