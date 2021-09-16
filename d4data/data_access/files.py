import shutil
from pathlib import Path
import os



class FilesDataAccess:
    def __init__(self, base_path):
        self.base_path = Path(base_path)

    def get_url(self, name=""):
        full_path = self.base_path.joinpath(name)
        url = full_path.absolute()
        return url

    def read(self, name=""):
        url = self.get_url(name)
        return str(url)

    def update(self, name, new_name):
        path = self.base_path.joinpath(name)
        path.rename(new_name)
        return str(path)

    def delete(self, name):
        url = self.get_url(name)
        os.remove(url)
        return None

    def put(self, name, src):
        url = self.get_url(name)
        shutil.copy2(src, url)
        return None
