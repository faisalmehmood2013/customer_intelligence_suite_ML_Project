"""
data_ingestion.py  (tier1_clv)
-----------------------------
Raw dataset (Online Retail II) ko load karta hai aur is TIER ke liye
relevant raw slice nikalta hai (zyada tar sab tiers SAME raw data se
shuru honge - yeh shared cleaning ke baad ka data hoga).

Target/Goal: Monetary (future/total customer spend)

Yahan function banayenge jaise:
    def initiate_data_ingestion() -> DataIngestionArtifact:
        # 1. Cleaned data load karo (shared cleaning module se)
        # 2. Train/Test split karo
        # 3. train.csv, test.csv save karo artifacts/ folder mein
        # 4. DataIngestionArtifact return karo (file paths ke sath)
"""
