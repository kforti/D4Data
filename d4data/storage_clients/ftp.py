import urllib.request as request
from contextlib import closing

from tqdm import tqdm
from ..core import StorageClient


class FTPStorageClient(StorageClient):

    def download(self, uri, save_path):

        with closing(request.urlopen(uri)) as r:
            file_size = r.length
            with open(save_path, 'wb') as f:
                with tqdm(unit='blocks', unit_scale=True, leave=False, miniters=1, desc='Downloading......',
                          total=file_size) as tqdm_instance:
                    for line in r:
                        f.write(line)
                        tqdm_instance.update(len(line))
