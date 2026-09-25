# Relevant Definitions

| Column Field | Classification & Range | Definition |
| :--- | :--- | :--- |
| **id** | Numerical factor "characters: HN1[0-9][0-9][0-0]" | The ID number of the patient in the dataset |
| **performance_status_ecog** | Categorical factor of 6 levels in range of integers (0-5) | The performance status according to the ECOG scale. |
| **index_tumor_location** | Categorical factor of 2 levels | The location of the tumor: larynx or oropharynx.<br>- *Larynx*: The hollow organ in the upper neck that connects the throat to the windpipe and helps you breath, talk and swallow.<br>- *Oropharynx*: The middle part of the throat, located directly behind the mouth. |
| **age_at_diagnosis** | Numerical in years | The age of the patient at the time of the diagnosis. |
| **biological_sex** | Categorical factor of 2 levels (male or female) | The biological sex of the patient. |
| **overall_hpv_p16_status** | Categorical factor of 2 levels (Positive or negative) | The presence or absence of the tumor suppressor protein p16 used as a diagnosis marker for Human Papilloma Virus related oropharyngeal cancers. Missing values are possible, implying test not done or unknown. |
| **clin_t** | Categorical factor of 4 levels | Clinical T staging of the disease according to the AJCC 7th Edition. Allowed values are 1-4. |
| **clin_n** | Categorical factor of 4 levels | Clinical N staging of the disease according to the AJCC 7th Edition. Allowed values are 0-3. |
| **clin_m** | Categorical factor of 2 levels | Clinical M staging of the disease according to the AJCC 7th Edition. Allowed values are 0 or 1. |
| **ajcc_stage** | Categorical factor of 6 levels | Overall staging according to the AJCC 7th Edition based on the TMM category. Allowed values are i, ii, iii, iva, ivb or ivc. |
| **pretreat_hb_in_mmolperlitre** | Numerical | This is the pre-treatment haemoglobin levels measured in a blood sample test, in units of millimol per litre. Missing values are possible implying whether the test was not done or that there was no documentation after the test. |
| **cancer_surgery_performed** | Categorical factor of 2 levels (1-0) | Binary variable denoting if surgery was performed as part of treatment. "Yes" and 1 or 0 for no. |
| **chemotherapy_given** | Categorical factor of 3 levels (1-0) | Binary variable denoting if chemotherapy was performed as part of the treatment. "Concurrent" or "concomitant" $=1$ & "none" $=0$. |
| **radiotherapy_total_treat_time** | Numerical | The physical prescribed radiation dose per fraction to the total tumor. |
| **radiotherapy_refgydose_perfraction_highriskgtv** | Numerical | The physical prescribed radiation dose to the gross tumor. |
| **radiotherapy_refgydose_total_highriskgtv** | Numerical | The total physical prescribed radiation dose to the total tumor (all high-risk target volumes in units of Gray) |
| **radiotherapy_number_fractions_highriskgtv** | Numerical | The total number of prescribed delivery fractions to the entire tumor.
| **event_overrall_survival**| Categorical factor of 0 or 1 | The binary variable denoting if the patient survived the therapy, hence if they survived then the survival analysis would be 0 or if they are deceased then 1. |
| **overall_survival_in_days** | numerical | The interval between the first fraction of radiotherapy to the date of the last audit if they are alive, or the date of death. |





