import os
from pathlib import Path
import zipfile
import urllib.request as request
from inproject.logging import logger
from inproject.utils.common import read_yaml, get_size
from kaggle.api.kaggle_api_extended import KaggleApi
from inproject.entity.config_entity import DataIngestionCOnfig
# import kaggle



class DataIngestion:
    def __init__(self, config:DataIngestionCOnfig):
        self.config = config

   
    def download_data_from_kaggle(self):
        if not os.path.exists(self.config.local_data_file):
            os.makedirs(self.config.root_dir, exist_ok=True)
            api = KaggleApi()
            api.authenticate()
            api.competition_download_files(self.config.comp_name, self.config.root_dir)

            logger.info(f'data downloaded succesfully ')

        else:
            logger.info(f'file already exist of size: {get_size(Path(self.config.local_data_file))}')


    def extract_zip_file(self):
        """
        zip_file_path: zip
        extract zip file into the directory
        function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)