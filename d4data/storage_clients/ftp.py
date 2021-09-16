import urllib.request as request
from contextlib import closing

from tqdm import tqdm
from ..sources import StorageClient


class FTPStorageClient(StorageClient):
    def download(self, src, dest):
        with closing(request.urlopen(src)) as r:
            file_size = r.length
            with open(dest, 'wb') as f:
                with tqdm(unit='blocks', unit_scale=True, leave=False, miniters=1, desc='Downloading......',
                          total=file_size) as tqdm_instance:
                    for line in r:
                        f.write(line)
                        tqdm_instance.update(len(line))
