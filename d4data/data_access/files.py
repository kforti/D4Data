import shutil
from pathlib import Path
import os

from .base import BaseDataAccess


class LocalFileURLsDataAccess(BaseDataAccess):
    def __init__(self, base_path, extensions=None):
        self.base_path = Path(base_path)
        self.extensions = extensions or []

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

    def _get_path(self, name):
        path = self.base_path.joinpath(name)
        if path.exists():
            return path

        for ext in self.extensions:
            modified_name = f"{name}.{ext}" if '.' not in ext else f"{name}{ext}"
            path = self.base_path.joinpath(modified_name)
            if path.exists():
                return path


class LocalFilesDataAccess(BaseDataAccess):
    def __init__(self, base_path, extensions=None):
        self.base_path = Path(base_path)
        self.extensions = extensions or []

    def read(self, name, **kwargs):
        path = self._get_path(name)
        with open(path, **kwargs) as f:
            data = f.read()
        return data

    def update(self, name, data, **kwargs):
        return self.put(name, data, **kwargs)

    def put(self, name, data, **kwargs):
        path = self._get_path(name)
        with open(path, **kwargs) as f:
            f.write(data)
        return None

    def delete(self, name):
        path = self._get_path()
        os.remove(path)
        return None

    def _get_path(self, name):
        path = self.base_path.joinpath(name)
        if path.exists():
            return path

        for ext in self.extensions:
            modified_name = f"{name}.{ext}" if '.' not in ext else f"{name}{ext}"
            path = self.base_path.joinpath(modified_name)
            if path.exists():
                return path


