from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionCOnfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path
    comp_name: str