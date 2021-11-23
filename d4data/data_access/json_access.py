import os
import json
import shutil
from pathlib import Path



class LocalJSONDataAccess:
    def __init__(self, base_path=""):
        self.base_path = Path(base_path)

    def _load_json(self, url):
        with open(url) as f:
            data = json.load(f)
        return data

    def _dump_json(self, url, data):
        with open(url, 'w') as f:
            json.dump(data, f)
        return None

    def get_url(self, name=""):
        full_path = self.base_path.joinpath(name)
        url = full_path.absolute()
        return url

    def read(self, name=""):
        url = self.get_url(name)
        data = self._load_json(url)
        return data

    def update(self, name, data):
        url = self.get_url(name)
        current_data = self._load_json(url)
        current_data.update(data)
        self._dump_json(url, current_data)
        return current_data

    def delete(self, name):
        url = self.get_url(name)
        os.remove(url)
        return None

    def put(self, name, data):
        url = self.get_url(name)
        self._dump_json(url, data)
        return None

    def copy(self, name, dest):
        src = self.get_url(name)
        shutil.copy2(src, dest)
        return None

    def __iter__(self):
        return self

    def __next__(self):
        pass


def load_json_data(path):
    dao = LocalJSONDataAccess(base_path="")
    data = dao.read(name=path)
    return data


def save_json_data(path, data):
    dao = LocalJSONDataAccess(base_path="")
    return dao.put(path, data)
