# Draft of Radiotherapy Treatment Response Planning Document

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
| Kaggle | Pre-cleaned, CSVs, similar to being subsets of SEER | None- instant download | Fastest path for the first version of the pipeline. |
| SEER Research Data | Millions of tabular records: demographics, tumor, morphology, treatment, survival time and vital status | I would need institutional validation which would be difficult unless I actually partnered with a government funded medical organization which is obviously unlikely given the time range. | Would be the primary tabular dataset for the statistical + ML phases. |
| TCIA (The Cancer Imaging Archive) | DICOM imaging (CT/PET/MRI) , dose plans + tumor contours and survival | Mainly free for public access. | This data might by used later as a stretch goal if later we can develop some sort of radiomics features to test whether imaging improves on clinical-only predictions. |
| cBioPortal (TCGA) | Clinical and genomic data<br>Clean, downloadable text files | free | <br> |

**Targeted Approach:** I’ll start with Kaggle SEER-derived CSV as the primary dataset for at least the first week of development since it is already cleaned and won’t require extensive application. Kaggle would also let me move to Phase 1 of project development immediately. If the Kaggle version of the data is too limited, we can potentially switch over the TCIA or TCGA rather than just blocking dependency.