"""
data_transformation.py  (tier5_recommendation)
---------------------------------------------
FEATURE ENGINEERING yahan hoti hai - raw/validated data ko is tier ke
liye specific features mein convert karta hai, aur Scaling apply karta hai.

Target/Goal: None (traditional) - 'customers who bought X also bought Y'

Yahan banayenge:
    def transform_data(dataframe):
        # 1. Tier-specific features banao (RFM, ya time-aggregates, etc.)
        # 2. Target variable banao (agar Supervised hai)
        # 3. StandardScaler fit/transform karo
        # 4. Transformed train/test arrays return karo
"""
