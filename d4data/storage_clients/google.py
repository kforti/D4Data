
from google.cloud import storage
from ..core import StorageClient

class GoogleStorageClient(StorageClient):
    def __init__(self):
        self.storage_client = storage.Client()

    def download(self, uri, save_path):
        with open(save_path, "wb") as file:
            self.storage_client.download_blob_to_file(blob_or_uri=uri, file_obj=file)

