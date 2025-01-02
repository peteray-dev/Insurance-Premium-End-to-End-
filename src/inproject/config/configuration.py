from inproject.constants import *
from inproject.utils.common import read_yaml, create_directories
from inproject.entity.config_entity import DataIngestionCOnfig

class ConfigurationManager:
    def __init__(self,
                 config_pathway = CONFIG_FILE_PATH,
                 param_pathway = PARAM_FILE_PATH,
                 schema_pathway = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_pathway)
        self.params = read_yaml(param_pathway)
        self.schema = read_yaml(schema_pathway)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionCOnfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionCOnfig(
            root_dir= config.root_dir,
            source_URL=config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir=config.unzip_dir,
            comp_name=config.comp_name
        )

        return data_ingestion_config