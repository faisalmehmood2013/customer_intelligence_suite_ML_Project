"""
data_transformation.py  (tier2_churn)
------------------------------------
FEATURE ENGINEERING yahan hoti hai - raw/validated data ko is tier ke
liye specific features mein convert karta hai, aur Scaling apply karta hai.

Target/Goal: Churned (0/1, based on 90-day inactivity rule)

Yahan banayenge:
    def transform_data(dataframe):
        # 1. Tier-specific features banao (RFM, ya time-aggregates, etc.)
        # 2. Target variable banao (agar Supervised hai)
        # 3. StandardScaler fit/transform karo
        # 4. Transformed train/test arrays return karo
"""
