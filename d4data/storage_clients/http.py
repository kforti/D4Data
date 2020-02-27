import requests

from tqdm import tqdm
from ..core import StorageClient


class HTTPStorageClient(StorageClient):
    def download(self, uri, save_path):
        r = requests.get(uri, stream=True)
        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        t = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(save_path, 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()
        if total_size != 0 and t.n != total_size:
            print("ERROR, something went wrong")

