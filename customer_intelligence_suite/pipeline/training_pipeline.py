"""
training_pipeline.py
-----------------------
MASTER orchestration file - SAB tiers ke training ko ek sequence mein
chalata hai (ya aap chahein to har tier ka apna run_training() call karein).

Yeh file basically "remote control" hai - jab aap
"python -m customer_intelligence_suite.pipeline.training_pipeline"
chalayenge, yeh andar se har tier ke components ko sahi order mein
call karega:

    1. Shared data ingestion (raw data load + clean)
    2. Tier1_CLV: feature engineering -> train -> evaluate -> save
    3. Tier2_Churn: feature engineering -> train -> evaluate -> save
    4. ... (aage jo tiers ban jayen)

Isko aap dheere-dheere banayenge - jab Tier 1 complete ho, sirf
Tier 1 ka call yahan add karein. Baad mein Tier 2 add karte jayen.
"""
