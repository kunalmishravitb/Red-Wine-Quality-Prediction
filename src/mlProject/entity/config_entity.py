from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # frozen=True means it will not take any other variable here
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True) # frozen=True means it will not take any other variable here
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict # For reading schema.yaml file we have define this and it is always written in dictionary format


@dataclass(frozen=True) # frozen=True means it will not take any other variable here
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True) # frozen=True means it will not take any other variable here
class ModelTrainerConfig:
    root_dir: Path # loading data from config.yaml
    train_data_path: Path # loading data from config.yaml
    test_data_path: Path # loading data from config.yaml
    model_name: str # loading data from config.yaml
    alpha: float # loading data from params.yaml
    l1_ratio: float # loading data from params.yaml
    target_column: str # loading data from schema.yaml


@dataclass(frozen=True) # frozen=True means it will not take any other variable here
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
