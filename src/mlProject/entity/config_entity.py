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



