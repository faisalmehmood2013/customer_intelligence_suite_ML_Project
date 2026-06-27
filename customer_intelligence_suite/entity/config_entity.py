"""
config_entity.py
------------------
Yahan hum CONFIG classes define karte hain - har tier/component ko
chalane ke liye kya settings chahiye (file paths, ratios, params).

Soch lein yeh "instruction cards" hain - jaise
DataIngestionConfig batayega "raw data kahan se aayega, processed
kahan jayega". Python mein @dataclass use karenge (clean aur readable).

Example structure (aap is tarah classes banayenge har component ke liye):

    @dataclass
    class DataIngestionConfig:
        raw_data_dir: str
        feature_store_file_path: str
        train_file_path: str
        test_file_path: str
        train_test_split_ratio: float

    @dataclass
    class CLVModelTrainerConfig:
        trained_model_file_path: str
        expected_score: float
        model_config_file_path: str

Aap har tier (CLV, Churn, Segmentation, etc.) ke liye alag Config
class banayenge jab us tier pe kaam shuru karein.
"""
