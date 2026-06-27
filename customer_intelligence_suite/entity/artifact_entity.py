"""
artifact_entity.py
---------------------
Yahan hum ARTIFACT classes define karte hain - har step ka OUTPUT
kaisa dikhega (file paths jo next step ko milenge).

Agar config_entity "instructions" hain, to artifact_entity
"results/proof" hai ke kaam ho gaya. Jaise DataIngestionArtifact
batayega "train_file_path yeh hai, test_file_path yeh hai" - taake
DataValidation component isko use kar sake.

Example structure:

    @dataclass
    class DataIngestionArtifact:
        train_file_path: str
        test_file_path: str

    @dataclass
    class ModelTrainerArtifact:
        trained_model_file_path: str
        metric_artifact: dict   # MAE, RMSE, R2 etc.

Yeh pattern ek "chain" banata hai: Ingestion ka Artifact -> Validation
ka Input, Validation ka Artifact -> Transformation ka Input, aur aage.
"""
