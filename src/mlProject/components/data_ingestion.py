import os
import urllib.request as request # With the help of request package we will download the data from the url
import zipfile # It will help to unzip the data
from mlProject import logger
from mlProject.utils.common import get_size # It will help to get the size of the data
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config=config
    

    # Downloading the data
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file # It will download the data and save it in local data file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    

    # Extract the zip file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path=self.config.unzip_dir # It will create the path which is present in config.yaml file
        os.makedirs(unzip_path, exist_ok=True)
        # Unzip the data.zip file which is already downloaded
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
