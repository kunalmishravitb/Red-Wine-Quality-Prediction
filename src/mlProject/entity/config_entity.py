from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # frozen=True means it will not take any other variable here
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path